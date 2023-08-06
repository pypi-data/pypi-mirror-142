"""This module defines classes for Bayesian analysis of paired-comparison data.
This hierarchical version includes a prior representing the distribution of model parameters
in the population from which test subjects were recruited.
It also includes a simple hyper-prior for the population model.

The population model, as well as individual subject models, are adapted to
observed paired-comparison data.
Individual subject models are weakly regularized by the population model.

In addition to the learned posterior individual models,
these learned models are used to derive three types of predictive distributions:
*:  a random individual in the Population from which participants were recruited,
    but for whom no data have been collected
*:  mean (=median) across individuals in the Population
*:  a random individual in a Group, for whom paired-comp data are available

All results are estimated
*A: separately for each Group and each Attribute
*B: for a combined Overall Group including all subjects from all groups,
    stored as an additional merged Group with key = tuple of group keys

*** Main Classes:

PairedCompResultSet: analysis results for a complete paired-comparison experiment,
    including PairedCompGroupModel instances for
    one or more GROUPs of test participants (subjects),
    tested for one or more perceptual ATTRIBUTES,
    in all selected TEST CONDITIONS.
    A single PairedCompResultSet instance includes all statistical analysis results.
    All input data for learning a PairedCompResultSet are provided by a
    pc_data.PairedCompDataSet instance.

PairedCompGroupModel: probability distribution of quality parameters for
    all individuals in ONE Group of test subjects for ONE perceptual Attribute,
    AND a prior model for the population from which the test subjects were recruited.

pc_subject.PairedCompIndModel: probability distribution of quality parameters for
    two or more sound-presentation objects, as judged by
    ONE SUBJECT, for ONE perceptual attribute, in ALL selected test conditions.
    Models may be joined later to include data from several subjects,
    thus representing a single mixture distribution for all individuals in a group.

PopulationModel: a GaussianRV prior and posterior model for population parameters.

PopulationPredictiveModel: Parametric predictive model for
    the marginal distribution of parameters in the population.

Bradley:   Bradley-Terry-Luce model: logistic probability distribution for decision variables
Thurstone: Thurstone Case V model: Gaussian probability distribution for decision variables

*** Reference:
Leijon et al (2019) Bayesian Analysis of Paired-comparison Sound Quality Ratings.
    J Acoust Soc Amer, 146(5), 3174-3183. doi: 10.1121/1.5131024
    Appendices describe the probabilistic model in detail.

*** Version History:
** Version 2.0.1:
2022-03-12, subject entropy calculation from PairedCompGroupModel -> PairedCompIndModel.adapt()
2022-03-10, PairedCompIndModel -> separate module pc_subject
2022-03-10, simplified logger.info output during iterative learning

** Version 2.0:
2021-08-26, logger.info output to follow learning
2021-08-28, new method PairedCompGroupModel.pred_population_mean, for new pc_display
2021-08-28, new method PairedCompGroupModel.pred_population_ind,  for new pc_display
2021-09-13, class PredictiveResultSet deleted, not needed
2021-09-13, methods PairedCompResultSet.predictive_*** deleted, not needed
2021-09-13, removed warning about unreliable population estimates from too small group

** Version 1.0:
2017-12-29, first plain-prior functional version
2018-03-27, corrected some doc-strings
2018-03-27, class name change to PairedCompIndModel, to allow other model variants
2018-03-28, PairedCompResultSet.models[g][a] is now a PairedCompGroupModel instance,
            with attribute subjects = dict with (subject_id, PairedCompIndModel) items
            to allow extension to hierarchical population prior
2018-04-02, METHODS PairedCompResultSet.predictive_...
2018-04-05, hierarchical prior model structure
2018-04-12, hierarchical model tested, similar results as older plain-prior variant
2018-05-15, renamed METHODS PairedCompResultSet.predictive_xxx
2018-07-08, changed from Wishart to gauss_gamma.py for population model
2018-08-02, fixed PairedCompMdata likelihood calc for Binary Forced-choice data
2018-08-14, adapted to simplified PairedCompDataSet structure
2018-10-08, method cat_limit_samples in PopulationPredictiveModel
2018-11-27, can learn NULL model with population mean quality params forced to zero, for model comparison
"""
# GroupModel -> separate module pc_group ??? Not necessary ************
# *** multi-processing subject models in parallel ? ***

# perhaps integrate out population mean and prec and use Student-t distribution directly,
# with ML type II point estimation of hyperparameters (beta, a, b) ???
# or perhaps fixed beta = N, and free (a, b) only ???
# *** but present VI approximation seems already quite OK

import numpy as np
from scipy.special import expit, ndtr

from collections import OrderedDict, Counter
import logging
import copy

from PairedCompCalc import gauss_gamma, gauss_gamma_null
from PairedCompCalc.pc_subject import PairedCompIndModel
from PairedCompCalc.pc_subject import cat_limits_transform, d_cat_limits_transform

PopulationModel = gauss_gamma.GaussianRV
PopulationNullModel = gauss_gamma_null.GaussianNullRV
# an alternative model might be gauss_wishart.GaussianRV
# with correlated quality parameters
# OR perhaps better, a GMM population model, like EmaCalc ?

N_SAMPLES = 1000  # number of samples for each subject model

# ------------------------- prior population distribution parameters:
PRIOR_WEIGHT = 0.2

PRIOR_QUALITY_SCALE = 1.
# = prior scale of quality parameters in Thurstone d-prime units
# = typical prior scale of inter-individual quality distribution
# *** should be modified for equivalent effect with Bradley model ***

PRIOR_CAT_WIDTH_SCALE = 1.
# = prior scale for log response-interval width parameters
#   used to restrict ratio between interval widths
# typical width ratio = cw_big / cw_small = exp(2 * PRIOR_CAT_WIDTH_SCALE)

# 2018-07-11, gives OK empirical coverage of cred.interval for population mean
# initial sampler epsilon = 0.1 seems generally OK, several tests

# ------------------------------------------------------------------------


logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)  # test


# ------------------------------------------------------------------
class Bradley:
    """Distribution of decision variable in the Bradley-Terry-Luce model.
    """
    unit_label = 'BTL unit'
    # for axis label in quality plots

    @staticmethod
    def log_cdf_diff(a, b):
        """log prob( a < Z <= b)
        where Z is a standard logistic random variable
        :param a: = array with LOWER interval limits
        :param b: = arrays with UPPER interval limits
            a.shape == b.shape
            all( a < b )
        :return: log_p = array with log probabilities, element-wise
            log_p.shape == a.shape == b.shape
        """
        return np.log(expit(b) - expit(a))

    @staticmethod
    def d_log_cdf_diff(a, b):
        """Element-wise partial derivatives of log_cdf_diff(a, b)
        :param a: = array with LOWER interval limits
        :param b: = arrays with UPPER interval limits
            a.shape == b.shape
            all( a < b )
        :return: tuple (dll_da, dll_db) of arrays, where
            dll_da[...] = d log_cdf_diff(a[...], b[...]) / d a[...]
            dll_db[...] = d log_cdf_diff(a[...], b[...]) / d b[...]
            dll_da.shape == dll_db.shape == a.shape == b.shape
        Arne Leijon, 2017-12-08, tested by finite-diff comparison
        """
        return (1. / np.expm1(a - b) + expit(-a),
                1. / np.expm1(b - a) + expit(-b))

    def __repr__(self):
        return '<class Bradley>'


class Thurstone:
    """Distribution of decision variable in the Thurstone Case V model.
    NOTE: Thurstone.scale is now included in all calculations.
    This is different from corresponding MatLab code.
    """
    unit_label = 'd-prime unit'

    sqrt_2pi = np.sqrt(2. * np.pi)
    scale = np.sqrt(2.)

    @staticmethod
    def cdf_diff(a, b):
        """prob( a < Z <= b)
        where Z is a Gaussian standard random variable with variance = 2.
        :param a: = array with LOWER interval limits
        :param b: = arrays with UPPER interval limits
            a.shape == b.shape
            all( a < b )
        :return: log_p = array with log probabilities, element-wise
            log_p.shape == a.shape == b.shape
        2018-04-24, include Thurstone.scale factor
        """
        a_s = a / Thurstone.scale
        b_s = b / Thurstone.scale
        cdf_diff = ndtr(b_s) - ndtr(a_s)
        ch_sign = a_s >= 0.  # and (b > a) always
        cdf_diff[ch_sign] = ndtr(-a_s[ch_sign]) - ndtr(-b_s[ch_sign])
        # better precision of difference in case of large positive a, b
        return cdf_diff

    @staticmethod
    def log_cdf_diff(a, b):
        """log cdf_diff(a, b)
        :param a: = array with LOWER interval limits
        :param b: = arrays with UPPER interval limits
            a.shape == b.shape
            all( a < b )
        :return: log_p = array with log probabilities, element-wise
            log_p.shape == a.shape == b.shape
        """
        return np.log(Thurstone.cdf_diff(a, b))

    @staticmethod
    def d_log_cdf_diff(a, b):
        """Element-wise partial derivatives of log_cdf_diff(a, b)
        :param a: = array with LOWER interval limits
        :param b: = arrays with UPPER interval limits
            a.shape == b.shape
            all( a < b )
        :return: tuple (dll_da, dll_db), where
            dll_da[...] = d log_cdf_diff[a[...], b[...]) / d a[...]
            dll_db[...] = d log_cdf_diff[a[...], b[...]) / d b[...]
            dll_da.shape == dll_db.shape == a.shape == b.shape
        Arne Leijon, 2017-12-08, tested by finite-diff comparison
        2018-04-24, include Thurstone.scale factor
        """
        def norm_pdf(x):
            """Gaussian density function = derivative of ndtr(x / scale)
            """
            return np.exp(- (x / Thurstone.scale)**2 / 2) / Thurstone.sqrt_2pi / Thurstone.scale
        # ----------------------------------------------------
        cdf_diff = Thurstone.cdf_diff(a, b)
        return - norm_pdf(a) / cdf_diff, norm_pdf(b) / cdf_diff

    def __repr__(self):
        return '<class Thurstone>'


# ------------------------------------------------------------------
class PairedCompResultSet:
    """Defines probabilistic models for all selected data
    from a paired-comparison experiment.
    """
    def __init__(self, pcf, models, rv_class):
        """Create a PairedCompResultSet from pre-learned attributes.
        :param pcf: single PairedCompFrame instance,
            specifying common aspects of a paired-comparison experiment,
            which are common for all subjects.
        :param models: nested dict with PairedCompGroupModel instances, stored as
            models[group][attribute] = one PairedCompGroupModel instance
            models[group][attribute].subjects = dict with (subject_id, PairedCompIndModel instance)
            where
            group, attribute, subject are string-valued keys,
            for all attribute values in pcf.attributes, for every subject.
        :param rv_class: a class for the distribution of model decision variables, with methods
            rv_class.log_cdf_diff, rv_class.d_log_cdf_diff
            rv_class distribution is Gaussian for rv_class=Thurstone, and
            logistic for rv_class=Bradley
        """
        self.pcf = pcf
        self.models = models  # **** rename to self.groups ???
        self.rv_class = rv_class

    def __repr__(self):
        return self.__class__.__name__ + f'(pcf=pcf, models=models, rv_class={repr(self.rv_class)})'

    @classmethod
    def learn(cls, ds, rv_class=Thurstone, null_quality=False):
        """Create and learn PairedCompGroupModel instances
        for each group and attribute
        defined by a given PairedCompDataSet instance
        :param ds: a single PairedCompDataSet instance
        :param rv_class: a class for the model latent variable,
            either Thurstone or Bradley
        :param null_quality: (optional) boolean => population model with quality param == 0.
        :return: a single cls instance containing all analysis results

        2018-03-30, adapted to changed nesting order in ds
        2018-05-19, single population prior for all groups and attributes
        2018-05-19, merge all subject groups into a single group, for each attribute
        2018-11-27, allow learning with NULL population model
        """
        ds.ensure_complete()
        # check that subjects have sufficiently complete data
        pcf = ds.pcf
        pcm = OrderedDict((g, dict()) for g in ds.pcd)  # ****** use dict()?
        # model objects will be organized as
        # pcm[group][attribute] = one PairedCompGroupModel instance with
        # pcm[group][attribute].subjects = dict with elements
        # pcm[group][attribute].subjects[subject_ID] = a PairedCompIndModel instance
        population_prior = _make_population_prior(pcf, null_quality)
        # = single hyper-prior used for all groups and all attributes
        for (g, g_attributes) in ds.pcd.items():
            for (a, ga_subjects) in g_attributes.items():
                pcm[g][a] = PairedCompGroupModel.learn(pcf, ga_subjects, rv_class, population_prior)
                logger.info(f'Learned group {repr(g)}, attribute {repr(a)}, for {len(ga_subjects)} subjects')
        if len(pcm) > 1:
            # create separate new group including all groups merged
            # Includes all subject models unchanged, but a new population model
            # Warning if same subject_id appears in separate groups
            merged_g = tuple(g for g in pcm.keys())
            ag_models = {a: PairedCompGroupModel.merge([g_models[a]
                                                        for g_models in pcm.values()])
                         for a in pcf.attributes}
            pcm[merged_g] = ag_models
            logger.info(f'Merged group {repr(merged_g)} with \n\t'
                        + f'\n\t'.join(f'attribute {repr(a)}, '
                                       + f'for {len(a_g.subjects)} subjects,'
                                       for (a, a_g) in ag_models.items()))
        return cls(pcf, pcm, rv_class)


# ------------------------------------------------------------
class PopulationPredictiveModel:
    """Parametric predictive model for population quality parameters,
    represented by ONE GROUP of subjects for ONE ATTRIBUTE,
    OR for all groups pooled, and ONE attribute.
    Needed to transform raw samples into model quality and cat_limits.
    """
    def __init__(self, pred_model, pcf, rv_class):
        """
        :param pred_model: a single StudentRV instance, from which samples can be generated
        :param pcf: a PairedCompFrame instance.
        :param rv_class: class for the decision latent variable, Thurstone or Bradley
        """
        self.pred_model = pred_model
        self.pcf = pcf
        self.rv_class = rv_class

    def __repr__(self):
        return ('PopulationPredictiveModel(' +
                '\n\tpcf=pcf,' +
                f'\n\tpred_model={repr(self.pred_model)},' +
                f'\n\trv_class={repr(self.rv_class)})')

    @property
    def quality_samples(self):
        """Samples of quality parameters from predictive distribution
        of mean vector in a population represented by a group of subjects.
        :return: 3D array q, with quality samples stored as
            q[n, t, s] = n-th sample of quality estimated for
            pcf.test_conditions()[t], pcf.objects[s],
            i.e., same format as PairedCompIndModel.quality_samples
        """
        n_q = self.pcf.n_quality_params
        # = number of quality elements in parameter vector
        q = self.pred_model.rvs(size=10 * N_SAMPLES)[:, :n_q]
        q = q.reshape((-1,
                       self.pcf.n_test_conditions,
                       self.pcf.n_objects - 1))
        zero_shape = (*q.shape[:-1], 1)
        # include fixed q == 0. for self.objects[0]
        return np.concatenate((np.zeros(zero_shape), q), axis=-1)

    @property
    def cat_limit_samples(self):
        """extract UPPER response-interval boundaries from self.pred_model
        """
        n_q = self.pcf.n_quality_params
        # = number of quality elements in parameter vector
        ln_c = self.pred_model.rvs(size=10 * N_SAMPLES)[:, n_q:]
        return cat_limits_transform(ln_c)


# -------------------------------------------------------------------
class PairedCompGroupModel:
    """A PairedCompGroupModel instance includes PairedCompIndModel instances,
    for ONE group of test subjects,
    and ONE perceptual attribute.

    Arne Leijon, 2018-04-05
    2018-07-09, include pcf= PairedCompFrame reference
    """
    def __init__(self, pcf, subjects, population, population_prior, rv_class=None):
        """
        :param pcf: a PairedCompFrame instance.
        :param subjects: dict with (subject_label, PairedCompIndModel) elements
        :param population: a single GaussianRV instance
            representing learned distribution of population quality parameters
        :param population_prior: reference to a single GaussianRV instance
            representing a weakly informative prior for all population models.

        Arne Leijon, 2018-04-05
        2018-07-09, modified signature, include pcf reference
        2021-08-28, modified signature, include rv_class reference
        """
        self.pcf = pcf
        self.rv_class = rv_class
        self.subjects = subjects  # **** OrderedDict to allow matched subjects across Attributes ?
        self.population = population
        self.population_prior = population_prior
        self.LL = []  # list with lower-bound log-likelihood values obtained during VI learning

    def __repr__(self):
        return (self.__class__.__name__ + '('+
                '\n\tpcf=pcf,' +
                f'\n\trv_class={repr(self.rv_class)},' +
                f'\n\tpopulation={repr(self.population)},' +
                f'\n\tpopulation_prior={repr(self.population_prior)})'
                )

    @classmethod
    def learn(cls, pcf, ga_subjects, rv_class, population_prior):
        """Learn one PairedCompIndModel for each subject,
        and a single GaussianRV prior for the population represented by the subjects,
        in ONE group of test subjects tested for ONE perceptual attribute.

        :param pcf: a PairedCompFrame object defining experimental layout
        :param ga_subjects: a nested dict with elements (subject_id, s_learn_data)
            where s_learn_data is a dict with elements (tc-tuple, result-list)
        :param rv_class: class for the model latent variable,
            either Thurstone or Bradley
        :param population_prior: externally pre-calculated single prior,
            same for all groups and attribute models
        :return: a PairedCompGroupModel instance

        Arne Leijon, 2018-07-09
        """
        m_data = {s: PairedCompMdata(learn_data, pcf)
                  for (s, learn_data) in ga_subjects.items()}
        # = all subject results in format suitable for learning
        ga_model = cls.init_learn(pcf, m_data, rv_class, population_prior)
        ga_model._learn(m_data)
        logger.debug('Learned LL= [' + ', '.join(f'{ll_i:.1f}' for ll_i in ga_model.LL) + ']')
        logger.debug('Population loc = ' + np.array_str(ga_model.population.loc,
                                                        precision=3))
        logger.debug('Population individual var =\n' +
                     np.array_str(ga_model.population.predictive.var,
                                  precision=3, suppress_small=True))
        logger.debug('Population mean var =\n' +
                     np.array_str(ga_model.population.mean.predictive.var,
                                  precision=3, suppress_small=True))
        return ga_model

    @classmethod
    def init_learn(cls, pcf, m_data, rv_class, population_prior):
        """
        Create initial version of the cls instance,
        to be adapted to data later, by VI learning

        :param pcf: a PairedCompFrame object defining experimental layout
        :param m_data: observed data for one group of subjects and one attribute
        :param rv_class: class for the model latent variable, Thurstone or Bradley
        :param population_prior: externally pre-calculated single prior,
            same for all groups and attribute models

        :return: a cls instance, initialized to correct internal structure,
            with non-informative parameters, not yet learned

        Arne Leijon, 2018-07-09, slightly modified for gauss_gamma population model
        """

        nq = pcf.n_quality_params
        # = n quality params
        nr = pcf.n_difference_grades
        nx = nq + nr
        # = length of parameter vector
        population = copy.deepcopy(population_prior)

        # set smaller mean precision for the first subject learning step
        # to make the population mean get nearly correct from start
        # population.prec.scale[:nq, :nq] /= 100.  # gauss_wishart version
        population.prec.b[:nq] *= 100.  # gauss_gamma version
        subjects = {s: PairedCompIndModel(pcf,
                                          x_samples=np.zeros((1, nx)),
                                          x_map=np.zeros((1, nx)),
                                          rv_class=rv_class)
                    for s in m_data}
        return cls(pcf, subjects, population, population_prior, rv_class=rv_class)

    def _learn(self, m_data,
               min_iter=5, min_step=0.01,
               max_iter=np.inf, callback=None):
        """Learn self from observed data,
        using Variational Inference (VI).

        This method adapts all model parameters towards a local maximum of
        a lower bound to the total likelihood of the training data.

        :param m_data: observed data for ONE group of subjects and ONE attribute
        :param min_iter= (optional) minimum number of learning iterations
        :param min_step= (optional) minimum data log-likelihood improvement,
                 over the latest min_iter iterations,
                 for learning iterations to continue.
        :param max_iter= (optional) maximum number of iterations, regardless of result.
        :param callback= (optional) function to be called after each iteration step.
            If defined, called as callback(self, previousLowBound)
            where previousLowBound == VI lower bound BEFORE last update
        :return: LL = list of log-likelihood values, one after each iteration.
            The resulting sequence is theoretically guaranteed to be non-decreasing.

        Result: adapted self properties.
        """
        min_iter = np.max([min_iter, 1])
        log_probs = []
        while (len(log_probs) <= min_iter
               or (log_probs[-1] - log_probs[-1-min_iter] > min_step
                   and (len(log_probs) < max_iter))):
            log_probs.append(self.one_learn_step(m_data))
            if callback is not None:
                callback(self, log_probs[-1])
            logger.info(f'Done {len(log_probs)} iterations. LL = {log_probs[-1]:.2f}')
        self.LL = log_probs
        logger.debug('learned LL = ' + np.array_str(np.asarray(log_probs),
                                                    precision=2))
        return log_probs

    def one_learn_step(self, m_data):
        """One VI learning step.
        :param m_data: observed data for one group of subjects and one attribute
        :return: scalar LL = current VI lower bound of log-likelihood

        Arne Leijon, 2018-07-09, eliminate arbitrary common constant in log(cat_width)
        """
        LL_sum_ind = sum(s_model.adapt(m_data[s], self.population)
                         for (s, s_model) in self.subjects.items())
        x_samples = np.array([s_model.x_samples
                              for (s, s_model) in self.subjects.items()])
        # ensure sum( log(cat_width) ) == 0, because gauss_gamma uses diagonal covariance
        n_q = self.pcf.n_quality_params
        x_samples[..., n_q:] -= np.mean(x_samples[..., n_q:],
                                        axis=-1, keepdims=True)
        self.population.adapt(x_samples, self.population_prior)
        pop_KLdiv = self.population.relative_entropy(self.population_prior)
        # -------------------------------------------- only for logger output:
        mean_x_map = np.mean([s_model.x_map
                              for s_model in self.subjects.values()], axis=(0,1))
        logger.debug(f'mean(x_map) = {mean_x_map}')
        logger.debug(f'group.population.loc = {self.population.loc}')
        logger.debug(f'group.population.prec.mean_inv = {self.population.prec.mean_inv}')
        logger.debug(f'LL_sum_ind={LL_sum_ind}; -KLdiv={- pop_KLdiv}')
        # ---------------------------------------------------
        return LL_sum_ind - pop_KLdiv

    @classmethod
    def merge(cls, models):
        """Merge a sequence of group models into a single such model.
        :param models: iterable of cls instances
        :return: single cls instance

        2018-07-09, remove arbitrary constant in log(cat_width) params, for gauss_gamma population
        2021-09-09, fix and warning if same subject id in several groups
        """
        # **** arg attr_label for use in logger warning **************
        def join(subject_dicts):
            """Gather several subject dicts into a single dict
            :param subject_dicts: sequence of dicts, each with (s_id, PairedCompIndModel) elements
            :return: all_subjects = single dict with (s_id, PairedCompIndModel) elements,
                union of all s_dicts
            """
            all_subjects = dict()
            # space for result, stored as all_subjects[subject_id] = subject PairedCompIndModel instance
            for s_dict in subject_dicts:
                for (s, s_model) in s_dict.items():
                    if s in all_subjects:
                        # subject s has been found in previous group model
                        # must make new copy so we do not modify the original group model
                        logger.warning(f'Subject {repr(s)} found in more than one group')
                        all_subjects[s] = copy.copy(all_subjects[s])  # shallow copy
                        all_subjects[s].add(s_model)
                    else:  # this s is unique, just use ref to original model
                        all_subjects[s] = s_model
            return all_subjects
        # ----------------------------------------------------

        population_prior = models[0].population_prior  # copy reference
        pcf = models[0].pcf  # copy reference
        population = copy.deepcopy(population_prior)  # new population model
        subjects = join(m.subjects for m in models)
        x_samples = np.array([s_model.x_samples for s_model in subjects.values()])

        n_q = pcf.n_quality_params
        # remove any arbitrary constant from log(cat_width) params:
        x_samples[..., n_q:] -= np.mean(x_samples[..., n_q:], axis=-1, keepdims=True)
        population.adapt(x_samples, population_prior)
        return cls(pcf, subjects, population, population_prior)

    def pred_population_mean(self):
        """Predictive model for population mean,
        for the MEAN quality params in the POPULATION from which the group was recruited.
        :return: res = single PopulationPredictiveModel instance,
                which can generate quality_samples from distribution of population mean quality.

        Arne Leijon, 2021-08-28, new method for new pc_display version
        """
        return PopulationPredictiveModel(self.population.mean.predictive,
                                         self.pcf, self.rv_class)

    def pred_population_ind(self):
        """Predictive model for random (unseen) individual in self.population,
        for the MEAN quality params in the POPULATION from which the group was recruited.
        :return: res = single PopulationPredictiveModel instance,
                which can generate quality_samples from distribution of population mean quality.

        Arne Leijon, 2021-08-28, new method for new pc_display version
        """
        return PopulationPredictiveModel(self.population.predictive,
                                         self.pcf, self.rv_class)


# --------------------------------------------------- general module helper stuff

def _make_population_prior(pcf, null_quality=False):
    """Create a single prior model to be used in all learned models,
    using global scale constants.

    :param pcf: single PairedCompFrame object defining experimental layout
    :param null_quality: (optional) boolean => model with all quality params == 0.
    :return: single PopulationModel instance (or PopulationNullModel)

    Arne Leijon, 2018-07-08, modified for gauss-gamma population model
    2018-11-27, can also generate NULL model for population-model comparison
    """
    nq = pcf.n_quality_params
    # = n quality params
    nr = pcf.n_difference_grades
    nx = nq + nr
    # = length of parameter vector
    x_scale = np.concatenate((np.ones(nq) * PRIOR_QUALITY_SCALE,  # rv_class
                              np.ones(nr) * PRIOR_CAT_WIDTH_SCALE))
    # return gauss_gamma.GaussianRV(loc=np.zeros(nx), scale=x_scale, learned_weight=PRIOR_WEIGHT)
    if null_quality:
        return PopulationNullModel(n_null=nq,
                                   loc=np.zeros(nx), scale=x_scale, learned_weight=PRIOR_WEIGHT)
    else:
        return PopulationModel(loc=np.zeros(nx), scale=x_scale, learned_weight=PRIOR_WEIGHT)


class PairedCompMdata:
    """Help class for PairedCompIndModel learning.
    The PairedCompMdata object is used only temporarily during the learning procedure,
    to provide a representation of all paired-comparison results for ONE subject, stored in
    a PairedCompDataSet instance ds, as ds.pcd[group][attribute][subject]
    The ratings are re-organized more compactly to facilitate learning calculations.
    """
    def __init__(self, s_res, pcf):
        """Recode paired-comparison results to facilitate learning.
        :param s_res: a list of StimRespItem objects, obtained from
            some ds.pcd[group][attribute][subject]
        :param pcf: a PairedCompFrame instance; determines how to store s_res data

        2018-08-14, simplified s_res, because of simplified PairedCompDataSet structure
        """
        counter = Counter()
        n_objects = len(pcf.objects)
        tct = list(pcf.test_conditions())
        for ((a, b), r, tc) in s_res:
            i_tc = tct.index(tc)
            tc_offset = i_tc * (n_objects - 1)
            if r < 0:  #
                # swap so response is positive, quality(b >= quality(a)
                (a, b) = (b, a)
                r = - r
            # recode ia, ib as indices into PairedCompIndModel parameter vector x, such that
            # mu_a = x[:, self.ia] if ia >= 0 else Mu_a = 0.
            # similar for mu_b
            ia = pcf.objects.index(a)
            ia = -1 if ia == 0 else tc_offset + ia - 1
            ib = pcf.objects.index(b)
            ib = -1 if ib == 0 else tc_offset + ib - 1
            counter[(ia, ib, r)] += 1

        self.n_q = pcf.n_quality_params
        self.n_cat = pcf.n_difference_grades
        # remaining elements in parameter vectors define response-category interval widths
        self.forced_choice = pcf.forced_choice
        # must be saved to determine lowest response category limits
        # copy counter results into self:
        self.a_index = []
        self.b_index = []
        self.cat_index = []
        self.count = []
        for ((ia, ib, r), n) in counter.items():
            self.a_index.append(ia)
            self.b_index.append(ib)
            # quality means found in q_a = x[:, self.ia] if ia >= 0 else q_a = 0.
            # similarly for q_b
            if pcf.forced_choice:
                r -= 1
                # recode category indices for origin zero,
                # because r == 0 never occurs if forced_choice
            self.cat_index.append(r)
            # interval width parameters for pcf.response_label[m]
            # stored in x[:, self.n_q + m]
            self.count.append(n)
        self.a_index = np.array(self.a_index)
        self.b_index = np.array(self.b_index)
        self.cat_index = np.array(self.cat_index)
        self.count = np.array(self.count)

    def q_diff(self, x):
        """extract quality-parameter differences from given model samples
        Input:
        x = 1D or 2D array with model parameter ROW vector(s)
            x[n, i] = n-th sample of i-th internal model parameter
        Returns:
        1D or 2D array d with elements
            d[..., p] = b - a for p-th paired-comparison (a, b) stored in self
        d.shape[-1] == number of paired-comparison trials
        """
        a = x[..., self.a_index]
        b = x[..., self.b_index]
        a[..., self.a_index == -1] = 0.
        b[..., self.b_index == -1] = 0.
        return b - a

    def cat_limits(self, x):
        """extract low and high interval limits for each response case in self.
        :param x: 2D array with tentative model parameter sample ROW vectors
            x[n, i] = n-th sample of i-th internal model parameter
        :return: tuple (b_low, b_high), where b_low and b_high are 2D arrays,
            b_low[n, p] = n-th sample of lower interval bound at p-th response case
            b_high[n,p] = similarly, higher interval bound.

        2018-08-03, simplified, with cat_limits_transform giving highest +inf limit
        """
        b = cat_limits_transform(x[..., self.n_q:])
        # = UPPER interval limits
        l_index = np.maximum(0, self.cat_index - 1)
        b_low = b[..., l_index]
        if self.forced_choice:
            b_low[..., self.cat_index == 0] = 0.
        else:
            b_low[..., self.cat_index == 0] *= -1.
        # h_index = np.minimum(b.shape[-1] - 1, self.cat_index)
        b_high = b[..., self.cat_index]
        # b_high[..., b.shape[-1] == self.cat_index] = np.inf
        return b_low, b_high

    def cdf_args(self, x):
        """extract arguments for model probability calculation
        :param x: 1D or 2D array with model parameter sample ROW vectors
            x[..., i] = ...-th sample of i-th internal model parameter
        :return: tuple( (arg_low, arg_high) arguments for probabilistic model, such that
            P[ p-th paired-comparison response | n-th model-parameter sample ] =
            = rv_class.cdf(arg_high[n, p]) - rv_class.cdf(arg_low[n, p])
        """
        d = self.q_diff(x)
        (b_low, b_high) = self.cat_limits(x)
        return b_low - d, b_high - d

    def log_likelihood(self, x, rv):
        """log P{self | x} given model parameters x
        :param x: 1D or 2D array with model parameter sample ROW vectors
            x[n, i] = n-th sample of i-th internal model parameter, OR
            x[i] = i-th model parameter of a single parameter vector
            x[..., :self.n_q] are quality parameters,
            x[..., self.n_q:] are transformed response-interval width parameters
        :param rv: Latent-variable class, Thurstone or Bradley
        :return: 1D array (or scalar) ll, with one element for each row vector in x
            ll[n] = - log prob(md | x[n,:] ) if x is 2D, OR
            ll = - log prob(md | x ) if x is a single 1D parameter vector
            ll.shape == x.shape[:-1]

        Method:
        For the k-th paired-comparison response_magnitude = m[k], with choice b > a,
        the probability is
        P[ response[k] | mu_a[k], mu_b[k] ] =
        = rv.cdf(b_high - mu_diff) ) - rv.cdf(b_low - mu_diff), where
            (b_low, b_high) = (lower, upper) limits of m-th latent-variable interval
            The cdf arguments are calculated by self.cdf_args, given parameter vectors x, and
            self.count is an array of number of trials with the same pair and response.
        """
        ll = rv.log_cdf_diff(*self.cdf_args(x))
        # ll[n, k] = log ll for k-th trial category, given n-th x-sample
        # ll.shape == (n_samples, n trial categories)
        return np.dot(ll, self.count)

    def grad_log_likelihood(self, x, rv):
        """gradient of log P[self | x]
        :param x: 1D or 2D array with model parameter sample ROW vectors
            x[n, i] = n-th sample of i-th internal model parameter, OR
            x[i] = i-th model parameter of a single parameter vector
            x[..., :self.n_q] are quality parameters,
            x[..., self.n_q:] are transformed response-interval width parameters
        :param rv: Latent-variable class, Thurstone or Bradley
        :return: array dll_dx, with
            dll_dx[..., i] = d ll[...] / d x[..., i]
            dll_dx.shape == x.shape
        """
        dll_dx = np.zeros_like(x)
        # = space for result
        dll_db = np.zeros_like(x[..., self.n_q:-1])
        # = space for derivative w.r.t. intermediate interval limits, except lowest and highest
        (d_ll_low, d_ll_high) = rv.d_log_cdf_diff(*self.cdf_args(x))
        # d_ll_low[n, k] = d ll[n, k] / d cdf_args[0][n, k]; n-th sample k-th pair
        # d_ll_high[n, k] = d ll[n, k] / d cdf_args[1][n, k]; n-th sample k-th pair
        d_ll_low *= self.count
        d_ll_high *= self.count

        # cdf_args = (b_low - (q_b - q_a), b_high - (q_b - q_a))
        # thus, q_b and q_a have equal effects in d_ll_low and d_ll_high

        # gradient w.r.t q parameters in x:
        d_ll = d_ll_low + d_ll_high
        for i in range(self.n_q):
            # i = index of q_a and q_b in x
            dll_dx[..., i] = (np.sum(d_ll[..., i == self.a_index], axis=-1) -
                              np.sum(d_ll[..., i == self.b_index], axis=-1))

        # gradient w.r.t b_low and b_high parameters:
        db_dx = d_cat_limits_transform(x[..., self.n_q:])
        # db_dx[..., m, i] = grad of UPPER limit of m-th interval w.r.t x[:, self.n_q+i]
        # db_dx.shape[-1] == self.n_cat
        # db_dx.shape[-2] == self.n_cat-1

        for m in range(self.n_cat-1):
            # m = index of interval boundary,  i.e., upper limit of m-th category interval
            dll_db[..., m] = (np.sum(d_ll_high[..., m == self.cat_index], axis=-1) +
                              np.sum(d_ll_low[..., (m + 1) == self.cat_index], axis=-1))
        if not self.forced_choice:
            # special case for low limit of zero interval
            dll_db[..., 0] -= np.sum(d_ll_low[..., 0 == self.cat_index], axis=-1)  # *******, keepdims=True)
        # dll_dx[..., self.n_q:] = dll_db @ db_dx
        # dll_dx[..., self.n_q:] = np.einsum('...m, ...mi -> ...i',
        #                                    dll_db, db_dx)
        dll_dx[..., self.n_q:] = np.sum(dll_db[..., :, None] * db_dx, axis=-2)
        return dll_dx


# --------------------------------------------------------------- TEST:
if __name__ == '__main__':

    a = np.array([2.])
    # b = np.array([np.inf])
    b = np.array([3.])

    print('Thurstone log_cdf_diff = ', Thurstone.log_cdf_diff(a, b))
    (da, db) = Thurstone.d_log_cdf_diff(a,b)
    print('dll_da =', da)
    print('dll_db =', db)
    eps = 1e-6
    print('approx dll_da: ', (Thurstone.log_cdf_diff(a+eps/2, b) -
                              Thurstone.log_cdf_diff(a-eps/2, b)) / eps)
    print('approx dll_db: ', (Thurstone.log_cdf_diff(a, b+eps/2) -
                              Thurstone.log_cdf_diff(a, b-eps/2)) / eps)
    # -------------------------------------- OK
