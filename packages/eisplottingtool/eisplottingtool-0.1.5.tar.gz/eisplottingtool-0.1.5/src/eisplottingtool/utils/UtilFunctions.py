import os
from typing import Union

import pandas as pd
import eclabfiles as ecf
from matplotlib import figure, axes, pyplot as plt, rcParams, cycler, legend


def load_df_from_path(path, sep="\t"):
    ext = os.path.splitext(path)[1][1:]

    if ext in {"csv", "txt"}:
        data = pd.read_csv(path, sep=sep, encoding="unicode_escape")
    elif ext in {"mpr", "mpt"}:
        data = ecf.to_df(path)
    else:
        raise ValueError(f"Datatype {ext} not supported")

    if data.empty:
        raise ValueError(f"File {path} has no data")
    return data


def set_plot_params() -> None:
    """
    Sets the default plotting params for matplotlib
    """
    rcParams["font.family"] = "sans-serif"
    rcParams["font.sans-serif"] = ["Arial"]
    rcParams["font.size"] = 22
    rcParams["axes.linewidth"] = 1.1
    rcParams["axes.labelpad"] = 4.0
    plot_color_cycle = cycler(
        "color",
        [
            "000000",
            "0000FE",
            "FE0000",
            "008001",
            "FD8000",
            "8c564b",
            "e377c2",
            "7f7f7f",
            "bcbd22",
            "17becf",
        ],
    )
    rcParams["axes.prop_cycle"] = plot_color_cycle
    rcParams["axes.xmargin"] = 0.1
    rcParams["axes.ymargin"] = 0.1
    rcParams.update(
        {
            "figure.subplot.hspace": 0,
            "figure.subplot.left": 0.11,
            "figure.subplot.right": 0.946,
            "figure.subplot.bottom": 0.156,
            "figure.subplot.top": 0.965,
            "xtick.major.size": 4,
            "xtick.minor.size": 2.5,
            "xtick.major.width": 1.1,
            "xtick.minor.width": 1.1,
            "xtick.major.pad": 5,
            "xtick.minor.visible": True,
            "xtick.direction": "in",
            "xtick.top": True,
            "ytick.major.size": 4,
            "ytick.minor.size": 2.5,
            "ytick.major.width": 1.1,
            "ytick.minor.width": 1.1,
            "ytick.major.pad": 5,
            "ytick.minor.visible": True,
            "ytick.direction": "in",
            "ytick.right": True,
            "lines.markersize": 10,
            "lines.markeredgewidth": 0.8,
        }
    )


def create_fig(
    nrows: int = 1,
    ncols: int = 1,
    sharex="all",
    sharey="all",
    figsize=None,
    subplot_kw=None,
    gridspec_kw=None,
    top_ticks=False,
    no_params=False,
    **fig_kw,
) -> tuple[figure.Figure, Union[axes.Axes, list[axes.Axes]]]:
    """Creates the figure, axes for the plots and set the style of the plot

    Parameters
    ----------
    nrows : int
        number of rows
    ncols :
        number of columns
    sharex
    sharey
    figsize
    subplot_kw
    gridspec_kw
    top_ticks
    fig_kw


    Returns
    -------
    the figure and list of created axes
    """
    if not no_params:
        set_plot_params()

    if figsize is None:
        figsize = (6.4 * ncols, 4.8 * nrows)
    if gridspec_kw is None:
        gridspec_kw = {"hspace": 0}
    elif gridspec_kw.get("hspace") is None:
        gridspec_kw["hspace"] = 0

    fig, axs = plt.subplots(
        nrows,
        ncols,
        figsize=figsize,
        sharex=sharex,
        sharey=sharey,
        gridspec_kw=gridspec_kw,
        subplot_kw=subplot_kw,
        **fig_kw,
    )

    if top_ticks:
        axs[0].xaxis.set_tick_params(which="both", labeltop=True)

    return fig, axs


def save_fig(
    path: str,
    fig: figure.Figure = None,
    show: bool = False,
    close: bool = True,
    **kwargs,
) -> None:
    """Saves the current figure at path

    Parameters
    ----------
    path : str
        path to save the figure
    fig : matplotlib.figure.Figure
        the figure to save
    show : bool
        show figure, no saving, False: save and show figure
    **kwargs
        any Keywords for Figure.savefig
    """
    if fig is None:
        fig = plt.gcf()
    fig.savefig(path, bbox_inches="tight", **kwargs)
    fig.canvas.draw_idle()
    if show:
        plt.show()
    if close:
        plt.close(fig)


def plot_legend(
    ax: axes.Axes = None,
    loc="upper left",
    fontsize="xx-small",
    frameon=True,
    markersize=10,
    handletextpad=0.1,
    mode=None,
    edgecolor="white",
    borderpad=0.0,
    framealpha=1.0,
    **kwargs,
) -> legend.Legend:
    """Adds legend to an axes

    Parameters
    ----------
    ax
    loc
    fontsize
    frameon
    markerscale
    handletextpad
    mode
    kwargs
    edgecolor
    borderpad
    framealpha

    Returns
    -------

    """
    if ax is None:
        ax = plt.gca()

    leg = ax.legend(
        loc=loc,
        fontsize=fontsize,
        frameon=frameon,
        framealpha=framealpha,
        edgecolor=edgecolor,
        handletextpad=handletextpad,
        mode=mode,
        borderpad=borderpad,
        **kwargs,
    )

    for handle in leg.legendHandles:
        handle.set_markersize(markersize)
    return leg


def show_plot(*args, **kwargs):
    plt.show(*args, **kwargs)
