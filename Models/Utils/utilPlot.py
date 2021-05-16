#util function for plot handling
import matplotlib.pyplot as plt

import utilFunc

# Create chart with particular properties
# ax - chart
# x, y - list of arg and function's value
# keywords - named parameters
def preparePlot(ax, x, y, **keywords):
    line = None
    #
    label = utilFunc.extractValue('label', **keywords)
    if label is not None:
        line, = ax.plot(x, y, label = keywords.get("label"))
    else:
        line, = ax.plot(x, y)

    color = utilFunc.extractValue('color', **keywords)
    if color is not None:
        line.set_color(color)

    title = utilFunc.extractValue('title', **keywords)
    if title is not None:
        ax.set_title(title)

    grid = utilFunc.extractValue('grid', **keywords)
    # special logic supporting a grid onto multiline chart
    if grid is not None:
        if grid:
            ax.grid()
            ax.legend(loc='best')
    else:
        ax.grid()
        ax.legend(loc='best')

    xlabel = utilFunc.extractValue('xlabel', **keywords)
    if xlabel is not None:
        ax.set_xlabel(xlabel)

    ylabel = utilFunc.extractValue('ylabel', **keywords)
    if ylabel is not None:
        ax.set_ylabel(ylabel)

    return

# Hide particular chart
# ax - chart
def hidePlot(ax):
    ax.axis('off')
    return

# Create chart with phase diagram (multiline)
# ax - chart
# vec_xy - list of xy, where xy - (correspond to each line) pair of list x and y
# title, label, xlabel, ylabel, color - parameters of chart
# firstColor - special color for the first line
def preparePhaseDiagram(ax, vec_xy, title, label, xlabel, ylabel, color = 'red', firstColor = 'blue'):
    length = len(vec_xy)
    for i in range(length):
        clr = firstColor if i==0 else color
        grid = None if i==0 else False
        preparePlot(ax, vec_xy[i][0], vec_xy[i][1], title = title, xlabel = xlabel, ylabel = ylabel, color = clr,
                    grid = grid)

# Function to draw charts
# fig - matplotlib.figure
def showScene(fig):
    fig.tight_layout()
    plt.grid()
    plt.show()   