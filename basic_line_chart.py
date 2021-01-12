import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

## Data
axis_x = np.linspace(0,100, num=100)
axis_y = np.random.rand(100,)

## Plot Paramters
text_title = 'Basic Line Chart'
text_xlabel = 'x-axis'
text_ylabel = 'y-axis'
text_legend = 'legend'
fontsize_title = 24
fontsize_legend = 16
fontsize_label = 16
fontsize_ticks = 16
width_line = 2
width_xmargins = 0
width_ymargins = 0.5
color_line  = None
fig_size = (12,8)
loc_legend = 'upper right'

# Chart
fig = plt.figure(figsize=fig_size)
ax = fig.add_subplot() 
ax.plot(
    axis_x,
    axis_y,
    label=text_legend,
    linewidth=width_line,
    color=color_line
)
ax.legend(loc=loc_legend, fontsize=fontsize_legend)
ax.set_title(text_title, fontsize=fontsize_title)
ax.set_xlabel(text_xlabel, fontsize=fontsize_label)
ax.set_ylabel(text_ylabel, fontsize=fontsize_label)
[tick.label.set_fontsize(fontsize_ticks) for tick in ax.xaxis.get_major_ticks()]
[tick.label.set_fontsize(fontsize_ticks) for tick in ax.yaxis.get_major_ticks()]
ax.margins(x=width_xmargins, y=width_ymargins)
ax.grid()

plt.show()