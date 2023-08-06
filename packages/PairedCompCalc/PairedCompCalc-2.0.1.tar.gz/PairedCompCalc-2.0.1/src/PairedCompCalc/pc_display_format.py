"""This module includes functions to format output displays of
PairedCompResultSet data,
in either graphic or textual form.

Some formatting details are defined by module global variables,
which can be modified by user.

*** Version History:
* Version 2.0:
2021-09-03, generalized function tab_percentiles for arbitrary dimensionality
2021-09-11, generalized function fig_percentiles with input similar to tab_percentiles
2021-09-11, modified function fig_indiv_boxplot input

* Version 1.0:
2018-02-06, simplified table generation, generate only one selected table type
2018-02-18, use module variable FMT['table_format'] where needed
2018-04-19, minor changes to include population quality params
2018-08-11, minor cleanup

2018-08-29, fix percent sign switch by table_format
2018-10-02, use general FMT dict, fix table file suffix
2018-10-08, allow cat_limits in fig_percentiles and fig_indiv_boxplot
2018-11-24, changed 'x_label' to 'tested_objects' in FMT params
2019-03-27, include marginal credibility values in percentile tables
"""

# *** NEED format switches for all special chars differing between latex and tab variants
# *** perhaps utf-8 already solves this ?


import numpy as np
from itertools import cycle, product
import matplotlib.pyplot as plt
import logging

plt.rcParams.update({'figure.max_open_warning': 0})
# suppress warning for many open figures

logger = logging.getLogger(__name__)


# --------------------------- Default format parameters:
FMT = {'colors': 'rbgk',    # to separate results in plots, cyclic
       'markers': 'oxs*_',  # corresponding markers, cyclic use
       'table_format': 'latex',  # or 'tab' for tab-delimited tables
       'figure_format': 'pdf',   # or 'jpg', 'eps', or 'png', for saved plots
       'show_intervals': True,  # include median response thresholds in plots
       'probability': 'Probability',  # heading in tables
       'attribute': 'Attribute',  # heading in tables
       'group': 'Group',  # heading in tables
       'correlation': 'Correlation',  # heading in tables
       'significance': 'Signif.',  # heading in Likelihood Ratio result table
       'scale_unit': '',  # scale unit for attribute plot axis
       }
# = module-global dict with default settings for display details
# that may be changed by user

TABLE_FILE_SUFFIX = {'latex': '.tex', 'tab': '.txt'}
# = mapping table_format -> file suffix


def set_format_param(**kwargs):
    """Set / modify module-global format parameters
    :param kwargs: dict with format variables
        to replace the default values in FMT
    :return: None
    """
    for (k, v) in kwargs.items():
        k = k.lower()
        if k not in FMT:
            logger.warning(f'Format setting {k}={repr(v)} is not known, not used')
        FMT[k] = v


def _percent():
    """Percent sign for tables
    :return: str
    """
    return '\\%' if FMT['table_format'] == 'latex' else '%'


# ---------------------------- Main Result Classes
class FigureRef:
    """Reference to a single graph instance
    """
    def __init__(self, ax, path=None, name=None):
        """
        :param ax: Axes instance containing the graph
        :param path: Path to directory where figure has been saved
        :param name: (optional) updated name of figure file
        """
        self.ax = ax
        self.path = path
        self.name = name

    def __repr__(self):
        return (f'FigureRef(ax= {repr(self.ax)}, ' +
                f'path= {repr(self.path)}, name= {repr(self.name)})')

    @property
    def fig(self):
        return self.ax.figure

    def save(self, path, name=None):
        """Save figure to given path
        :param path: Path to directory where figure has been saved
        :param name: (optional) updated name of figure file  **** never used ? ****
        :return: None
        Result: updated properties path, name
        """
        if name is None:
            name = self.name
        path.mkdir(parents=True, exist_ok=True)
        f = (path / name).with_suffix('.' + FMT['figure_format'])
        self.fig.savefig(str(f))
        self.path = path
        self.name = f.name


class TableRef:
    """Reference to a single table instance,
    formatted in LaTeX OR plain tabulated txt versions
    """
    def __init__(self, text=None, path=None, name=None):
        """
        :param text: single string with all table text
        :param path: (optional) Path to directory where tables are saved
        :param name: (optional) updated file name, with or without suffix
            suffix is determined by FMT['table_format'] anyway
        """
        # store table parts instead *****???
        self.text = text
        self.path = path
        self.name = name

    def __repr__(self):
        return (f'TableRef(text= text, ' +    # fmt= {repr(self.fmt)}, ' +
                f'path= {repr(self.path)}, name= {repr(self.name)})')

    def save(self, path, name=None):
        """Save table to file.
        :param path: Path to directory where tables are saved
        :param name: (optional) updated file name, with or without suffix
            suffix is determined by FMT['table_format'] anyway
        :return: None
        Result: updated properties path, name
        """
        if name is None:
            name = self.name
        path.mkdir(parents=True, exist_ok=True)   # just in case
        f = (path / name).with_suffix(TABLE_FILE_SUFFIX[FMT['table_format']])
        if self.text is not None and len(self.text) > 0:
            f.write_text(self.text, encoding='utf-8')
        self.path = path
        self.name = f.name


# ---------------------------------------- Formatting functions:

def fig_percentiles(q_perc,
                    y_label,
                    case_labels,  # same input as tab_percentiles
                    # case_order=None,
                    cat_limits=None,
                    x_offset=0.1,
                    x_space=0.5, **kwargs):
    """create a figure with quality percentile results
    :param q_perc: primary percentile data,
        2D or 3D array with quality percentiles, arranged as
        q_perc[p, c, i] = p-th percentile for object_tuple[..., i] result, c-th case variant, OR
        q_perc[p, i] if no case variants are included
    :param y_label: string for y-axis label
    :param cat_limits: 1D array with response-interval limits (medians)
    :param case_labels: sequence with elements (case_factor_i, case_labels_i), where
        case_factor_i is key string for i-th case dimension,
        case_labels_i is list of string labels for i-th case dimension
        in the same order as the index order of q_perc, i.e.,
        q_perc[p].size == prod_i len(case_labels_i)
        Thus, q[p, ...,c_i,...] = percentiles for case_labels_i[c_i], i = 0,...,
        **** NOTE: currently only ONE or TWO case dimensions are allowed ***
        Plot will display case_list[-1] along x axis, and case_list[:1] as sub-variants
    :param x_offset: (optional) space between case-variants of plots for each x_tick
    :param x_space: (optional) min space outside min and max x_tick values
    :param kwargs: (optional) dict with any additional keyword arguments for plot commands.
    :return: FigureRef instance with plot axis with all results

    2021-09-11, New version with case_list input like tab_percentiles
        Fixed case_label format, different case_order not allowed
    """
    # *** generalize for several case dimensions i.e., (c_1,..,c_i,...) ?
    # *** allow user to switch main / sub- dimensions by case_order input ?
    # -------------------------------- check input formats:
    # n_perc = q_perc.shape[0]
    case_shape = tuple(len(c_list) for (c_key, c_list) in case_labels)
    object_labels = case_labels[-1][-1]  # ***********
    assert q_perc[0].size == np.prod(case_shape, dtype=int), 'mismatching size of q_perc vs. case_list'
    assert q_perc.shape[-1] == case_shape[-1], 'mismatching shape of q_perc vs case_list[-1]'
    if q_perc.ndim == 2:
        q_perc = q_perc[np.newaxis, ...]
        (case_head, case_list) = ('', [''])
    else:
        q_perc = q_perc.transpose((1, 0, 2))
        (case_head, case_list) = case_labels[0]
    # q_perc now indexed as q_perc[case, p, object], prepared to plot one case at a time
    x_label = case_labels[-1][0]
    # ------------------------------------------------------------------
    fig, ax = plt.subplots()
    x = np.arange(0., len(object_labels)) - x_offset * (len(case_list) - 1) / 2
    for (y, c_label, c, m) in zip(q_perc, case_list,
                                  cycle(FMT['colors']), cycle(FMT['markers'])):
        label = case_head + '=' + c_label
        if y.shape[0] == 1:
            ax.plot(x, y[0, :],  # marker at single point percentile,
                    linestyle='',
                    marker=m, markeredgecolor=c, markerfacecolor='w',
                    label=label,
                    **kwargs)
        elif y.shape[0] == 2:  # plot min,max line, with marker at ends
            line = ax.plot(np.tile(x, (2, 1)),
                           y,
                           linestyle='solid', color=c,
                           marker=m, markeredgecolor=c, markerfacecolor='w',
                           **kwargs)
            line[0].set_label(label)
        else:
            ax.plot(np.tile(x, (2, 1)),
                    y[[0, -1], :],  # plot min, max line, no markers
                    linestyle='solid', color=c,
                    **kwargs)
            line = ax.plot(np.tile(x, (y.shape[0] - 2, 1)),
                           y[1:-1, :],
                           linestyle='solid', color=c,  # markers only at inner percentiles
                           marker=m, markeredgecolor=c, markerfacecolor='w',
                           **kwargs)
            line[0].set_label(label)
            # set only ONE label, even if several points
        x += x_offset
    (x_min, x_max) = ax.get_xlim()
    x_min = min(x_min, -x_space)
    x_max = max(x_max, len(object_labels) - 1 + x_space)
    ax.set_xlim(x_min, x_max)
    if cat_limits is not None and FMT['show_intervals']:
        _plot_response_intervals(ax, cat_limits)
    ax.set_xticks(np.arange(len(object_labels)))
    ax.set_xticklabels(object_labels)
    y_unit = FMT['scale_unit']
    if len(y_unit) > 0:
        ax.set_ylabel(y_label + ' (' + y_unit + ')')
    else:
        ax.set_ylabel(y_label)  # plain without unit
    ax.set_xlabel(x_label)
    if np.any([len(cl) > 0 for cl in case_list]):
        ax.legend(loc='best')
    f_name = y_label + '_' + '_'.join(c_key for (c_key, c_val) in reversed(case_labels))
    return FigureRef(ax, name=f_name)


def fig_indiv_boxplot(q,
                      y_label,
                      object_tuple,
                      cat_limits=None,
                      case_tuple=None,
                      x_space=0.5,
                      **kwargs):
    """create a figure with boxplot of individual results
    :param q: 2D array or sequence of 2D arrays,
        with point-estimated quality values, stored as
        q[c][n, i] = n-th individual result for s_labels[i], in c-th case variant, OR
        q[n, i] if no case variants
    :param y_label: string for y-axis label
    :param object_tuple: tuple (object_key, object_labels)
        object_key = string to become x_label in plot
        object_labels = list of strings with labels for x_ticks, one for each value in rows q[..., :]
        len(object_labels) == q.shape[-1]
    :param cat_limits: (optional) 1D array with response-interval limits (medians)
    :param case_tuple: (optional) tuple (case_order, case_list) for case variants
        len(case_list) == q_perc.shape[-2] if q_perc.ndim == 3 else case_list not used
    :param x_space: (optional) min space outside min and max x_tick values
    :param kwargs: (optional) dict with any additional keyword arguments for boxplot command.

    :return: FigureRef object with single plot axis with all results

    2018-10-08, new cat_limits parameter
    2021-09-11, input object_tuple = (x_label, object_labels)
    """
    if len(q) <= 1:
        return None  # boxplot does not work
    (x_label, object_labels) = object_tuple
    fig, ax = plt.subplots()
    if case_tuple is None:
        assert q.ndim == 2, 'Input must be 2D if no case variants'
        case_tuple = ('', [''])
        q = [q]
        # make it a list with ONE 2D array
    (case_head, case_labels) = case_tuple
    x_offset = min(0.2, 0.8 / len(case_labels))
    if len(case_labels) > 1:
        box_width = 0.8 * x_offset
    else:
        box_width = 0.5
    x_pos = np.arange(len(object_labels)) - x_offset * (len(case_labels) - 1) / 2
    for (y, c_label, c, m) in zip(q, case_labels, cycle(FMT['colors']), cycle(FMT['markers'])):
        boxprops = dict(linestyle='-', color=c)
        label = case_head + '=' + c_label
        # flierprops = dict(marker=m, markeredgecolor=c, markerfacecolor='w', # *** markersize=12,
        #                   linestyle='none')
        whiskerprops = dict(marker='', linestyle='-', color=c)
        capprops = dict(marker='', linestyle='-', color=c)
        medianprops = dict(linestyle='-', color=c)
        ax.boxplot(y, positions=x_pos,
                   widths=box_width,
                   sym='',  # ******** no fliers
                   boxprops=boxprops,
                   medianprops=medianprops,
                   whiskerprops=whiskerprops,
                   capprops=capprops,
                   **kwargs)
        median = np.median(y, axis=0)
        ax.plot(x_pos, median, linestyle='',
                marker=m, markeredgecolor=c, markerfacecolor='w',
                label=label)
        x_pos += x_offset

    (x_min, x_max) = ax.get_xlim()
    x_min = min(x_min, -x_space)
    x_max = max(x_max, len(object_labels) - 1 + x_space)
    ax.set_xlim(x_min, x_max)
    if cat_limits is not None and FMT['show_intervals']:
        _plot_response_intervals(ax, cat_limits)
    ax.set_xticks(np.arange(len(object_labels)))
    ax.set_xticklabels(object_labels)
    y_unit = FMT['scale_unit']
    if len(y_unit) > 0:
        ax.set_ylabel(y_label + ' (' + y_unit + ')')
    else:
        ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    if np.any([len(cl) > 0 for cl in case_labels]):
        ax.legend(loc='best')
    f_name = y_label + '-box' + '_' + x_label + ('_' + case_head if len(case_head) > 0 else '')
    return FigureRef(ax, name=f_name)


def _plot_response_intervals(ax, c_lim):
    """plot horizontal lines to indicate response-category intervals
    :param ax: axis object
    :param c_lim: 1D array with scalar interval limits
    :return: None
    """
    (x_min, x_max) = ax.get_xlim()
    y = list(c_lim) + list(-c_lim)
    return ax.hlines(y, x_min, x_max,
                     linestyle='solid',
                     colors='k',
                     linewidth=0.2)


# ----------------------------------------- table displays:

def tab_percentiles(q_perc,
                    cdf,
                    perc,
                    y_label,
                    case_labels,
                    case_order=None):
    """Create table with quality percentile results.
    This function is general and can handle any dimensionality of the data.
    :param q_perc: min 2D array with quality percentiles, stored as
        q_perc[p, c0,...,ci,...] = p-th percentile in (c0,...,ci,...)-th case condition
        OR any other array indexing with same size and same element order
        q_perc.shape[0] == len(perc)
        q_perc.size == len(perc) * n_rows; with n_rows as defined by case_list
    :param cdf: min 1D array with cumulative distribution values at zero,
        cdf[c0,...,ci,...] = probability that quality <= 0 in (c0,...,ci,...)-th case
        OR any other array indexing with same size and same element order
        cdf.size == number of rows as defined by case_list
    :param perc: list of percentage values in range 0-100
        len(perc) == q_perc.shape[0]
    :param y_label: single string with label of tabulated percentiles
    :param case_labels: sequence OR dict with elements (case_factor_i, case_labels_i), where
        case_factor_i is key string for i-th case dimension,
        case_labels_i is list of string labels for i-th case dimension
        in the same order as the index order of q and cdf, i.e.,
        len(case_labels_i) == q.shape[i+1] == cdf.shape[i], if full multi-dim index is used
        Thus, q[p, ...,c_i,...] = percentiles for case_labels_i[c_i], i = 0,...,
    :param case_order: (optional) sequence of case_label keys, one for each case column
        len(case_order) == len(case_list)
        Table columns are ordered as defined by case_order, if specified,
        otherwise columns are ordered as case_list.keys()
    :return: TableRef object, with header + one line for each combination of case labels.
        Number of table rows == prod q.shape[:-1] == prod_i len(case_labels_i)

    2021-09-09, new function to replace old specialized 2D and 3D
    2021-09-10, tested generalized version for user-selectable column order
    """
    def make_row(c, q, p_0):
        """make cells for one table row
        :param c: case tuple
        :param q: percentile quality values
        :param p_0: scalar probability q <= 0
        :return: row = list with cells
            len(row) == 1 + len(c) + len(q) + 2
        """
        c_dict = dict(c)
        # already in right order, need only c.values() ******
        return ([c_dict[c_head] for c_head in case_order]
                + [f'{p:.2f}' for p in q]
                + [f'{p_0*100:.0f}' + _percent(),
                   f'{(1.-p_0)*100:.0f}' + _percent()])

    # --------------------------------------------------------------------
    case_labels = dict(case_labels)  # just in case it was a list
    if case_order is None:
        case_order = [*case_labels.keys()]
    assert len(case_order) == len(case_labels), 'Incompatible len(case_order) != len(case_list)'
    assert all(c in case_labels for c in case_order), 'Some case_order not in case_list'
    case_shape = tuple(len(c_labels) for c_labels in case_labels.values())
    n_rows = np.prod(case_shape, dtype=int)
    # = number of table rows as defined by case_list
    assert len(perc) == q_perc.shape[0], 'Incompatible q_perc.shape[0] != n of percentiles'
    assert n_rows == np.prod(q_perc.shape[1:], dtype=int), 'Incompatible size of case_list and q_perc'
    assert n_rows == cdf.size, 'Incompatible size of case_list and cdf'
    # -------------------------------------------------------------------
    # transpose q_perc, cdf to case_order index order:
    q_perc = np.moveaxis(q_perc, 0, -1)
    q_perc = q_perc.reshape((*case_shape, len(perc)))
    cdf = cdf.reshape(case_shape)
    # q_perc[c_0, ..., c_i, ..., p] = p-th percentile in (c0,...,ci,...)-th case
    # cdf[c_0, ..., c_i, ...] = prob(quality <=0) in (c0,...,ci,...)-th case
    case_keys = [*case_labels.keys()]
    case_axes = tuple(case_keys.index(c) for c in case_order)
    q_perc = q_perc.transpose((*case_axes, -1))
    cdf = cdf.transpose(case_axes)
    q_perc = q_perc.reshape((n_rows, len(perc)))
    cdf = cdf.reshape((-1,))
    # --------------------------------------------------------------------
    align = [len(case_order) * 'l', len(perc) * 'r', 2 * 'r']
    h = [*case_order] + [f'{p:.0f}' + _percent() for p in perc] + ['<= 0', '> 0']
    case_rows = product(*(product([c_i], case_labels[c_i])
                          for c_i in case_order))
    rows = [make_row(c, p, cdf_0)
            for (c, p, cdf_0) in zip(case_rows,
                                     q_perc,
                                     cdf)
            ]
    f_name = y_label + '_' + '_'.join(case_order)
    return TableRef(_make_table(h, rows, align), name=f_name)


def tab_credible_diff_2d(diff,
                         y_label,
                         diff_list,
                         diff_head):
    """create table with credible differences among quality results
    :param diff: list of tuples ((i,j), p) defining jointly credible differences, indicating that
        prob{ quality of diff_list[i] > quality of diff_list[j] } AND all previous pairs } == p
    :param y_label: string with label of tabulated quality attribute
    :param diff_head: single string printed over column with pairs of object_tuple
    :param diff_list: list of strings with labels of compared random-vector elements,
        len(object_tuple) == diff.shape[-1]
    :return: TableRef object with header lines + one line for each credible difference,
    """
    if len(diff) == 0:
        return None
    align = ['l', 'l', 'c', 'l', 'r']
    h = ['', diff_head, '>', diff_head, FMT['probability']]
    rows = [['AND', diff_list[i], '>', diff_list[j], f'{100 * p:.1f}']
            for ((i, j), p) in diff]
    rows[0][0] = ''  # No AND on first row
    f_name = y_label + '-diff'
    return TableRef(_make_table(h, rows, align), name=f_name)


def tab_credible_diff_3d(diff,
                         y_label,
                         diff_head,
                         diff_list,
                         case_head,
                         case_list):
    """create table with credible differences among quality results
    in LaTeX tabular and in simple tab-separated text format
    :param diff: list of tuples ((i, j, c), p) defining jointly credible differences, indicating that
        prob{ quality of diff_list[i] > quality of diff_list[j] in case_label[c]
            AND same for all previous tuples in the lise } = p
    :param y_label: string with label of tabulated quality attribute
    :param diff_head: list of column headings for factors compared
    :param diff_list: list of dicts, one for each credible difference (each table row)
        each with elements (diff_head, diff_label) with categories
    :param case_head: list of case_key strings, for column headings of background factors
    :param case_list: list of dicts, one for each credible difference (each table row)
        each with elements (case_key, case_label) with case categories
        for which the credible difference was found.
    :return: TableRef object with header lines + one line for each credible difference
    """
    def make_cells(i, j, c):
        row = ([diff_list[i][d_head]
                for d_head in diff_head] + ['>'] +
               [diff_list[j][d_head]
                for d_head in diff_head] +
               [case_list[c][c_head]
                for c_head in case_head])
        return row
    # --------------------------------------------------------------------------------
    if len(diff) == 0:
        return None
    align = ('l' + len(diff_head) * 'l' + 'c' + len(diff_head) * 'l' +
             len(case_head) * 'l' + 'r')
    h = ['', *diff_head, '>', *diff_head, *case_head, FMT['probability']]
    rows = [['AND', *make_cells(i, j, c), f'{100*p:.1f}']
            for ((i, j, c), p) in diff]
    rows[0][0] = ''  # no 'AND' on first row
    f_name = y_label + '-diff_' + '_'.join(diff_head)
    return TableRef(_make_table(h, rows, align), name=f_name)


def tab_credible_corr(c, a_labels):
    """create table of credible correlations
    :param c: list of tuple((i, j), p, md_corr), where
        (i, j) are indices into a_labels,
        p is joint credibility,
        md_corr = median conditional correlation value, given all previous
    :param a_labels: list with string labels for correlated attributes
    :return: TableRef object with header + one row for each credible correlation
    """
    if len(c) == 0:
        return None
    align = ['l', 'l', 'c', 'l', 'r', 'r']
    h = [_make_cell(FMT['attribute'], 4, FMT['table_format']),
         FMT['correlation'], FMT['probability']]
    rows = []
    col_0 = ''
    for ((i, j), p, mdc) in c:
        rows.append([col_0, a_labels[i], '*', a_labels[j], f'{mdc:.2f}', f'{100*p:.1f}'])
        col_0 = 'AND'
    return TableRef(_make_table(h, rows, align), name='Correlation')


def tab_lr_test(lr_result):
    """Create TableRef with all likelihood ratio test results
    :param lr_result: nested dict with elements
        lr_result[group][attr] = pc_lr_test.LikelihoodRatioResult
    :return: TableRef instance
    """
    align = 'llrrrr'
    h = [FMT['group'], FMT['attribute'], 'Chi-2', 'df', 'p', FMT['significance']]
    rows = []
    for (g, g_result) in lr_result.items():
        for (a, lr) in g_result.items():
            p = f'{100*lr.pvalue:.1f}' + _percent()
            if lr.pvalue < 0.001:
                p = f'{lr.pvalue:.2g}'
                s = '***'
            elif lr.pvalue < 0.01:
                s = '**'
            elif lr.pvalue < 0.05:
                s = '*'
            else:
                s = '-'
            ga = f'Group {repr(g)}, Attribute {a}: '
            logger.info(ga + f'chi2(df={lr.df}) = {lr.statistic:.3f}: p= {p}. Signif.: {s}')
            rows.append([g, a, f'{lr.statistic:.2f}', f'{lr.df}', p, s])
    return TableRef(_make_table(h, rows, align), name='LR_significance_test')


# ------------------------------------------ internal help functions:
# more variants may be added for other table formats

table_begin = {'latex': lambda align: '\\begin{tabular}{' + ' '.join(c for c in align) + '}\n',
               'tab': lambda align: ''}
table_head_sep = {'latex': '\\hline\n',
                  'tab': ''}
table_cell_sep = {'latex': ' & ',
                  'tab': ' \t '}
table_row_sep = {'latex': '\\\\ \n',
                 'tab': '\n'}
table_end = {'latex': '\\hline\n\\end{tabular}',
             'tab': ''}


def _make_cell(text, col_span, fmt):
    """Format multi-column table cell, usually only for header line
    :param text: cell contents
    :param col_span: number of columns to span
    :param fmt: str key for table format
    :return: string with latex or plain cell contents
    """
    if fmt == 'latex' and col_span > 1:
        return '\\multicolumn{' + f'{col_span}' + '}{c}' + '{' + text + '}'
    else:
        return text


def _make_table(header, rows, col_alignment):
    """Generate a string with table text.
    Input:
    :param header: list with one string for each table column
    :param rows: list of rows, ehere
        each row is a list of string objects for each column in this row
    :param col_alignment: list of alignment symbols, l, r, or c
        len(col_alignment) == len(header) == len(row), for every row in rows

    :return: single string with complete table
    """
    def make_row(cells, fmt):
        return table_cell_sep[fmt].join(f'{c}' for c in cells) + table_row_sep[fmt]
    # ------------------------------------------------------------------------

    fmt = FMT['table_format']  # module global constant
    t = table_begin[fmt](col_alignment)
    t += table_head_sep[fmt]
    t += make_row(header, fmt)
    t += table_head_sep[fmt]
    t += ''.join((make_row(r, fmt) for r in rows))
    t += table_end[fmt]
    return t
