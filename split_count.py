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
    # Create a DataFrame with one column called 'count'
    df = pd.DataFrame(columns=['count'])
    # Go through each row in the Series x bu calling .items() which returns the index and the actual element at that index
    for index,entry in x.items():
        # Split the words in the actual element of the current row by the comma then strip leading and trailing white spaces
        reasons = [word.strip() for word in entry.split(',')]
        for reason in reasons:
            # df.index returns all of the indices in the DataFrame
            if reason not in df.index:
                # Return the entry at the 'count' column for the specific row called reason
                df.loc[reason, 'count'] = 1
            else:
                # Return the entry at the 'count' column for the specific row called reason
                df.loc[reason, 'count'] += 1
    # Sort the DataFrame with respect to the count column entries
    return df.sort_values(by='count')