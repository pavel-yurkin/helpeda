import pandas as pd


def df_info(df):

    '''
    docstring

    '''

    info_dict = {
        'dtype': [],
        'values': [],
        'unique_values': [],
        'example_min': [],
        'example_max': [],
        'nan_values': [],
        'zeros': [],
        'empty_str_ratio': [],
        'most_freq_frac': [],
        'trash_score': []
    }

    for column in df.columns:
        col_data = df[column]
        
        # type of data
        info_dict['dtype'].append(col_data.dtype.name)

        # count of all elemnts 
        info_dict['values'].append(len(col_data))
        
        # count of unique elements
        info_dict['unique_values'].append(col_data.nunique())
        
        # examples -> get fraction for min and max
        info_dict['example_min'].append(col_data.min())
        info_dict['example_max'].append(col_data.max())
        
        # fraction of null values
        nan_ratio = col_data.isna().mean()
        info_dict['nan_values'].append(round(nan_ratio, 3) if nan_ratio != 0 else '●')
        
        # fraction of zero values
        zeros = (col_data == 0).mean()
        info_dict['zeros'].append(round(zeros, 3) if zeros != 0 else '●')

        # empty strings
        empty_str_ratio = (col_data == '').mean()
        info_dict['empty_str_ratio'].append(round(empty_str_ratio, 3) if empty_str_ratio != 0 else '●')
        
        # the most frequent element
        mff = col_data.value_counts(normalize=True, dropna=True)
        mff_max_value = mff.index[0] if len(mff) else '●'
        mff_max_fraction = mff.iloc[0] if len(mff) else 0
        info_dict['most_freq_frac'].append((round(mff_max_fraction, 3) if mff_max_fraction != 0 else '●', mff_max_value))

        #trash score - how many useless values we have
        info_dict['trash_score'].append(round(empty_str_ratio + nan_ratio + zeros, 3)) 

    return pd.DataFrame(info_dict, index=df.columns)

