import yfinance as yf
import matplotlib.pyplot as plt
from currency_converter import CurrencyConverter

# Currency converter
c = CurrencyConverter()

# Data
watchlist = {
    'Christian Hansen': yf.Ticker("51C.F"),
    'Novo Nordisk': yf.Ticker("NOVO-B.CO"),
    'Top Danmark': yf.Ticker("TOP.CO"),
    'Tivoli': yf.Ticker("TIV.CO"),
    'Coca Cola': yf.Ticker("KO"),
    'Pepsi': yf.Ticker("PEP"),
}
period = "max"
interval = '1d'
num_days = 365*5

# Plot Paramters
text_title = 'Stock Watchlist'
text_xlabel = 'Time'
text_ylabel = 'Price (DKK)'
text_legend = None
fontsize_title = 24
fontsize_legend = 16
fontsize_label = 16
fontsize_ticks = 16
loc_legend = 'upper left'
width_line = 1

# Chart
fig = plt.figure(figsize=(20,12))
ax = fig.add_subplot() 

for stock in watchlist.keys():

    # extract time and price axes
    axis_time = watchlist[stock].history(period=period, interval=interval).index.tolist()[-num_days:]
    axis_price = watchlist[stock].history(period=period, interval=interval).Close.tolist()[-num_days:]
    
    # if not DKK, convert
    currency = watchlist[stock].info['currency'] 
    if currency != 'DKK':
        axis_price = [c.convert(price, currency, 'DKK') for price in axis_price]
    
    # plot stock price
    ax.plot(
        axis_time,
        axis_price,
        label=stock,
        linewidth=width_line
    )
    
ax.legend(loc=loc_legend, fontsize=fontsize_legend)
ax.set_title(text_title, fontsize=fontsize_title)
ax.set_xlabel(text_xlabel, fontsize=fontsize_label)
ax.set_ylabel(text_ylabel, fontsize=fontsize_label)
[tick.label.set_fontsize(fontsize_ticks) for tick in ax.xaxis.get_major_ticks()]
[tick.label.set_fontsize(fontsize_ticks) for tick in ax.yaxis.get_major_ticks()]
ax.margins(x=0)
ax.grid()

plt.show()