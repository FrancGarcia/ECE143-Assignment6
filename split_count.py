import pandas as pd
def split_count(x):
    """
    Returns a cleaned DataFrame that contains the count 
    of what people want to use Python for.

    :param x: pd.Series object of the data to clean
    :return: a pd.DataFrame of the cleaned data that consists of two columns
    such as the reason for using Python and the frequency count.
    """
    assert(isinstance(x, pd.Series)), "x argument must be a Pandas Series object"
    df = pd.DataFrame(columns=['count'])
    for index,entry in x.items():
        reasons = [word.strip() for word in entry.split(',')]
        for reason in reasons:
            if reason not in df.index:
                df.loc[reason, 'count'] = 1
            else:
                df.loc[reason, 'count'] += 1
    return df.sort_values(by='count')