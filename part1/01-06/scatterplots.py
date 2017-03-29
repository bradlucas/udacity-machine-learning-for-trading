import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os


def symbol_to_path(symbol, base_dir='/Users/brad/work/QSTK//env/lib/python2.7/site-packages/QSTK/QSData/Yahoo/'):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df_final = pd.DataFrame(index=dates)
    if "SPY" not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, "SPY")

    for symbol in symbols:
        file_path = symbol_to_path(symbol)
        df_temp = pd.read_csv(file_path, parse_dates=True, index_col="Date",
            usecols=["Date", "Adj Close"], na_values=["nan"])
        df_temp = df_temp.rename(columns={"Adj Close": symbol})
        df_final = df_final.join(df_temp)
        if symbol == "SPY":  # drop dates SPY did not trade
            df_final = df_final.dropna(subset=["SPY"])

    return df_final


def plot_data(df_data, title="Stock Data", ylabel="Price"):
    """Plot stock data with appropriate axis labels."""
    ax = df_data.plot(title=title, fontsize=2)
    ax.set_xlabel("Date")
    ax.set_ylabel(ylabel)
    plt.show()


def compute_daily_returns(df):
    """Compute and return the daily returns"""
    daily_returns = df.copy() 
    daily_returns[1:] = (df[1:] / df[:-1].values) - 1
    daily_returns.ix[0, :] = 0   # set daily returns for row 0 to 0
    return daily_returns

def test_run():
    start_date = "2009-01-01"
    end_date = "2012-12-31"
    # Read data
    symbol_list = ['SPY', 'XOM', 'GLD']
    dates = pd.date_range(start_date, end_date)  # date range as index
    df_data = get_data(symbol_list, dates)  # get data for each symbol

    # Plot
    # plot_data(df_data, title="Daily Returns", ylabel="Daily returns")

    daily_returns = compute_daily_returns(df_data)
    # #plot_data(daily_returns, title="Daily Returns", ylabel="Daily Returns")

    # daily_returns.plot(kind='scatter', x='SPY', y='XOM')
    # daily_returns.plot(kind='scatter', x='SPY', y='GLD')


    # Fit a line to the scatterplot
    # polyfit with a degree of 1
    # polynomial coeefient and the intercept
    daily_returns.plot(kind='scatter', x='SPY', y='XOM')

    # return slope/beta and intercept/alha
    beta_XOM, alpha_XOM = np.polyfit(daily_returns['SPY'], daily_returns['XOM'], 1)

    # Plot with equation -> y = mx + b
    plt.plot(daily_returns['SPY'], beta_XOM*daily_returns['SPY'] + alpha_XOM, '-', color='r')


    daily_returns.plot(kind='scatter', x='SPY', y='GLD')
    beta_GLD, alpha_GLD = np.polyfit(daily_returns['SPY'], daily_returns['GLD'], 1)
    plt.plot(daily_returns['SPY'], beta_GLD*daily_returns['SPY'] + alpha_GLD, '-', color='r')

    print "beta_XOM=", beta_XOM
    print "alpha_XOM=", alpha_XOM

    print "beta_GLD=", beta_GLD
    print "alpha_GLD=", alpha_GLD

    print daily_returns.corr(method='pearson')

    plt.show()

    # alpha_XOM= -0.00024686727668
    # beta_GLD= 0.0597611348322
    # alpha_GLD= 0.00074788111616
    #         SPY       XOM       GLD
    # SPY  1.000000  0.820241  0.067324
    # XOM  0.820241  1.000000  0.069687
    # GLD  0.067324  0.069687  1.000000

    # Notice XOM is more closely correlated to SPY than GLD


if __name__ == "__main__":
    test_run()
