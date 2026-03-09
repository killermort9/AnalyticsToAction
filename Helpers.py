def get_dataframe_by_val_in_key(df,key_name,value):
    '''
    Input: 
    df: Dataframe to sort
    key_name: string of key name, that is to be sorted by
    value: the value of the key that we wish to extract

    Output: dataframe consisting of only entries with that value for the specific key
    '''
    return df[df[key_name] == value]


