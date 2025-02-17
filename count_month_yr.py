import pandas as pd
import datetime

def add_month_yr(x):
    """
    Modifies the current DataFrame x by
    adding a new column called 'month-yr'
    and returns it

    :param x: the DataFrame to modify
    :return: the modified DataFrame
    """
    assert(isinstance(x,pd.DataFrame)), "Argument x must be a DataFrame object"
    x["month-yr"] = None
    for index,entry in x["Timestamp"].items():
        # Convert string to datetime object
        dt_object = datetime.datetime.strptime(entry, '%m/%d/%Y %H:%M')
        # Format the datetime object to 'month-year'
        month_year = dt_object.strftime('%b-%Y')
        x.loc[index, "month-yr"] = month_year
    return x

def count_month_yr(x):
    """
    Returns a new DataFrame with the month-yr and count column.

    :param x: The input DataFrame retrieved from add_month_yr(x)
    :return: A new DataFrame with the month-yr column and count of each 
    """
    assert(isinstance(x, pd.DataFrame)), "Argument must be a DataFrame"
    # Creates a Series as the unique month-yr as the index and the column
    # as the frequency. Then resets the indices.
    df = x["month-yr"].value_counts().reset_index()
    # sets the indices to be month-yr instead of 0 indexed
    df.set_index("month-yr", inplace=True)
    # Renames count column to timestamp
    df.rename(columns={"count": "Timestamp"}, inplace=True)
    return df