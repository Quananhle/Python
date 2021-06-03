import pandas as pd
import numpy as np

def estimate_volatility(prices, l):
    """Create an exponential moving average model of the volatility of a stock
    price, and return the most recent (last) volatility estimate.
    
    Parameters
    ----------
    prices : pandas.Series
        A series of adjusted closing prices for a stock.
        
    l : float
        The 'lambda' parameter of the exponential moving average model. Making
        this value smaller will cause the model to weight older terms less 
        relative to more recent terms.
        
    Returns
    -------
    last_vol : float
        The last element of your exponential moving averge volatility model series.
    
    """
    # TODO: Implement the exponential moving average volatility model and return the last value.
    # alpha = 1 - lambda\
    curr_prices = prices          # prices.shift(0)
    prev_prices = prices.shift(1) # shift prices to 1 day before
    log_returns = np.log(curr_prices) - np.log(prev_prices)
    # last_vol = np.sqrt((log_returns**2).ewm(alpha=1-l).mean().iloc[-1])
    volatility = (log_returns**2).ewm(alpha=1-l).mean()
    most_recent_volatility = np.sqrt(volatility.iloc[-1])
    return most_recent_volatility
def test_run(filename='data.csv'):
    """Test run get_most_volatile() with stock prices from a file."""
    prices = pd.read_csv(filename, parse_dates=['date'], index_col='date', squeeze=True)
    print("Most recent volatility estimate: {:.6f}".format(estimate_volatility(prices, 0.7)))


if __name__ == '__main__':
    test_run()