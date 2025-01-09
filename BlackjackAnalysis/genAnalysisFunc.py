import pandas as pd
import numpy as np
import statistics as st

def average(df, astr):
    data = df[astr]
    average = np.average(data.to_numpy())
    return average

def standardDeviation(df, astr):
    data = df[astr]
    sd = st.stdev(data)
    return sd

def lessThan(Ho, Ha):
    return