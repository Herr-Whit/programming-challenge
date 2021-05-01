#!/usr/bin/env python
# coding: utf-8

"""
Weather Data Challenge
In specific.csv you’ll find the daily specific data of a single month. Read the file, then output the day number
(column one Day) of the day with the smallest temperature spread (difference between maximum & minimum temperature of
the day.) The maximum temperature is the second column MxT, the minimum temperature the third column MnT.
"""
import pandas as pd


def find_highest_tdiff():
    """
    Solution to the specific data challenge. Finds the highest temparature difference in specific data and identifies the
    day
    :return: day - integer specifying the day in the month with the highest temparature difference.
    """
    # Transform the file in the "Pandas" DataFrame format

    source_file = r'../../src/main/resources/de/exxcellent/challenge/weather.csv'
    df = pd.read_csv(source_file)

    # Calculate the difference in Temparature for each day.

    df['TDiff'] = df['MxT'] - df['MnT']

    # Check for each day, whether it is one of the days with the highest temparature difference.

    maximum_temparature = max(df['TDiff'])

    ismax = df['TDiff'] == maximum_temparature

    # Select datapoints, which reflect the highest temparature differences using boolean indexing.
    # Isolate the "Day" entry.

    df_with_highest_diff = df[ismax]

    day = df_with_highest_diff["Day"].iloc[0]
    return day

