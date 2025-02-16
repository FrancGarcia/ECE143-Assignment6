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