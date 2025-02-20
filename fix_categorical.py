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

def fix_categorical(x):
    """
    Returns a DataFrame that is sorted by the month-yr

    :param x: The DataFrame with the month-yr column to sort by
    :return: The sorted DataFrame
    """
    assert(isinstance(x, pd.DataFrame)), "The input must be a DataFrame"
    x["month-yr"] = pd.to_datetime(x["month-yr"], format="%b-%Y").dt.strftime("%b-%Y")
    ordered_dates = x["month-yr"].unique()
    cat_dtype = pd.CategoricalDtype(categories=ordered_dates, ordered=True)
    x["month-yr"] = x["month-yr"].astype(cat_dtype)
    return x