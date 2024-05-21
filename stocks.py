import matplotlib.pyplot as plt
import yfinance as yf
from dataclasses import dataclass, field
import pandas as pd
from scipy.stats import t
import numpy as np

from primary_sensitivity import primary_sensitivity as ps
from utils import *


def main():
    tickers = ['SPY', 'XLF']
    start_date = '2008-09-22'
    end_date = '2008-09-30'

    df = yf.download(tickers, start=start_date, end=end_date)
    spy = df["Close"]["SPY"]
    xlf = df["Close"]["XLF"]

    r = compute_correlation(list(zip(spy, xlf)))
    p = p_value_for_pcc(r, len(spy))
    print(r, p)

    bounds = [(0.0, 0.0), (spy.max(), xlf.max())]
    sens_r = ps(list(zip(spy, xlf)), bounds)

    brute = brute_force_search(list(zip(spy, xlf)), (0, spy.max()), (0, xlf.max()), grid_size=100)

    print("C:", sens_r)
    print("Brute-force:", brute)


if __name__ == "__main__":
    main()
