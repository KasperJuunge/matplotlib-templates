import numpy as np
import matplotlib.pyplot as plt

# Data
line_1 = np.random.rand(50,)
line_2 = np.random.rand(50,)

# Plot Parameters
text_suptitle = 'Basic Line Subplot'
fontsize_suptitle = 24
fontsize_title = 20
fontsize_legend = 12
fontsize_label = 16
fontsize_ticks = 16
loc_legend = 'upper right'
figsize=(12,8)

# Subplot 1 Paramters
text_title_1 = 'Title 1'
text_xlabel_1 = 'xlabel 1'
text_ylabel_1 = 'ylabel 1'
text_legend_1 = 'legend 1'
xlim_1 = [0,10]
ylim_1 = [0,1]
width_line_1 = 1

# Subplot 2 Paramters
text_title_2 = 'Title 2'
text_xlabel_2 = 'xlabel 2'
text_ylabel_2 = 'ylabel 2'
text_legend_2 = 'legend 2'
xlim_2 = [0,10]
ylim_2 = [0,1]
width_line_2 = 1


# Figure
fig = plt.figure(figsize=figsize)

# Line + Stem

ax1 = fig.add_subplot(211)
ax1.plot(line_1, label=text_legend_1)
ax1.legend(loc=loc_legend, fontsize=fontsize_legend)
ax1.set_title(text_title_1, fontsize=fontsize_title)
ax1.set_xlabel(text_xlabel_1)
ax1.set_ylabel(text_ylabel_1)
ax1.set_xlim(xlim_1)
ax1.set_ylim(ylim_1)


# Bar plot
ax2 = fig.add_subplot(212)
ax2.plot(line_2, label=text_legend_2)
ax2.legend(loc=loc_legend, fontsize=fontsize_legend)
ax2.set_title(text_title_2, fontsize=fontsize_title)
ax2.set_xlabel(text_xlabel_2)
ax2.set_ylabel(text_ylabel_2)
ax2.set_xlim(xlim_2)
ax2.set_ylim(ylim_2)


# Super title
plt.suptitle(
    text_suptitle,
    fontsize=fontsize_suptitle,
    fontweight='bold',
)

# tune subplot layout
plt.subplots_adjust(
    left=None,   # the left side of the subplots of the figure
    right=None,  # the right side of the subplots of the figure
    bottom=None, # the bottom of the subplots of the figure
    top=None,    # the top of the subplots of the figure
    wspace=None, # the amount of width reserved for space between subplots, expressed as a fraction of the average axis width
    hspace=0.4  # the amount of height reserved for space between subplots, expressed as a fraction of the average axis height
)

plt.show()