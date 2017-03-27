import pandas as pd

data_dir = '/Users/brad/work/QSTK//env/lib/python2.7/site-packages/QSTK/QSData/Yahoo/'


def get_data_file(symbol):
    rtn = data_dir + "{}.csv"
    return rtn.format(symbol)

def test_run():
    start_date = '2010-01-02'
    end_date = '2010-01-26'
    dates = pd.date_range(start_date, end_date)

    # Create empty dataframe
    df1 = pd.DataFrame(index=dates)

    # Read SPY data into a temporary dataframe
    dfSPY = pd.read_csv(get_data_file('SPY'),
                            # Use Date column as the index rather than the default integer index
                            index_col="Date", parse_dates=True,
                            # Include only Date and Adj Close columns
                            usecols=['Date', 'Adj Close'],
                            #
                            na_values=['nan'])

    # left join
    df1 = df1.join(dfSPY)

    # Drop NaN values
    df1 = df1.dropna()
    return df1



if __name__ == '__main__':
    # test_run()
    pass
