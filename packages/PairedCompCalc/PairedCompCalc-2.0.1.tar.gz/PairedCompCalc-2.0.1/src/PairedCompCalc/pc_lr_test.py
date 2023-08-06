"""This module defines a function to do a likelihood ratio test
for the statistical significance of any quality parameters deviating from zero,
in the MEAN for the population from which test subjects were recruited.

The NULL hypothesis is that the mean quality parameters are EQUAL
for all tested objects in all test conditions,
in the population fromm which test subjects were recruited.

A separate test is done for each perceptual Attribute
and each Group of subjects.

NOTE: the resulting p-value is calculated using Wilks' theorem
for the ASYMPTOTIC Chi-2 distribution of the test statistic,
and may therefore be incorrect for small samples.

* Reference:
S. S. Wilks. The large-sample distribution of the likelihood ratio for testing composite hypotheses.
The Annals of Mathematical Statistics, 9(1):60–62, 1938.


* Main Result Class:
LikelihoodRatioResult: tuple (statistic, df, pvalue)

Arne Leijon, 2018-12-06
"""
from scipy.stats import chi2
from collections import namedtuple

import logging
logger = logging.getLogger(__name__)


LikelihoodRatioResult = namedtuple('LikelihoodRatioResult', 'statistic df pvalue')
# storage of result from a Likelihood Ratio test
# statistic = 2 * Log-likelihood difference between tested model and NULL model
# df = number of parameters in the tested model that are forced to zero in the NULL model
# pvalue = approximate significance value
# The test statistic is asymptotically Chi-2-distributed with df degrees of freedom
# according to Wilks' theorem.
# NOTE: the pvalue is approximate


def likelihood_ratio_test(pcr0, pcr1):
    """Likelihood-ratio test
    :param pcr0: PairedCompResultSet instance learned with NULL population quality params
    :param pcr1: PairedCompResultSet instance learned with full freedom
    :return: res = nested dict with elements
        res[group][attribute] = LikelihoodRatioResult instance
        for the NULL hypothesis that
        the mean quality parameters in the population are EQUAL
        for all tested objects in all test conditions.
        p_values smaller than, e.g., 0.05 indicate that pcr1 shows significant differences.

    Method: The lower bounds to the data log-likelihood is used to calculate
        a likelihood-ratio that is asymptotically Chi-2-distributed,
        according to Wilk's theorem.
    """
    res = dict()
    for (g, g_models) in pcr1.models.items():
        res[g]= dict()
        for (a, ga_model) in g_models.items():
            LL_1 = ga_model.LL[-1]
            df = pcr0.models[g][a].population.n_null
            LL_0 = pcr0.models[g][a].LL[-1]
            LLR = 2 * (LL_1 - LL_0)  # Wilks: asymptotically chi2-distributed
            p = chi2.sf(LLR, df=df)
            res[g][a] = LikelihoodRatioResult(LLR, df, p)
    return res

