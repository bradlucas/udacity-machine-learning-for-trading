import pandas as pd


def test_run():
    start_date = '2010-01-02'
    end_date = '2010-01-26'
    dates = pd.date_range(start_date, end_date)
    print dates
    return dates
    df1 = pd.DataFrame(index=dates)
    return df1


if __name__ == '__main__':
    test_run()
