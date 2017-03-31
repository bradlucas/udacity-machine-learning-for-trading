import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import math


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


# def compute_daily_returns(df):
#     """Compute and return the daily returns"""
#     daily_returns = df.copy()
#     daily_returns[1:] = (df[1:] / df[:-1].values) - 1
#     daily_returns.ix[0, :] = 0   # set daily returns for row 0 to 0
#     return daily_returns


def compute_daily_returns(df):
    # daily_returns = (price[t] / price[t-1]) - 1
    #               = (price[t] / price[t-1]) / price(t)
    # this returns the percent change for each day
    return (df/df.shift(1)) - 1

# Write a function to calculate the following for a portfolio:
# 1. Cumulative Return
# 2. Average daily return
# 3. Risk (Std deviation)
# 4. Sharpe ratio


def cumulative_returns(df):
    '''The culmative percentage return is the (price[last]/price[0]) - 1'''
    return df/df.values[0]-1


def cumulative_return(df):
    return df.values[-1] / df.values[0] - 1


def avg_daily_return(df):
    return compute_daily_returns(df).mean()


def std_deviation_of_daily_returns(df):
    return compute_daily_returns(df).std()


def sharpe_ratio(df):
    risk_free_return = 0
    return math.sqrt(252) * ((avg_daily_return(df) - risk_free_return) / std_deviation_of_daily_returns(df))


def test_run():
    start_date = "2012-01-01"
    end_date = "2012-12-31"
    # Read data
    symbol_list = ['SPY', 'AAPL', 'GOOG', 'IBM', 'GLD']
    dates = pd.date_range(start_date, end_date)  # date range as index
    df_data = get_data(symbol_list, dates)  # get data for each symbol

    print "Cumulative Returns"
    print cumulative_returns(df_data)

    print "Cumulative Return"
    print cumulative_return(df_data)

    print "Average Daily Return"
    print avg_daily_return(df_data)

    print "Standard Deviation of Daily Returns"
    print std_deviation_of_daily_returns(df_data)

    print "Sharpe Ratio"
    print sharpe_ratio(df_data)


if __name__ == "__main__":
    test_run()
