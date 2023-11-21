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
        'moda': [],
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

        frac_data = col_data.value_counts(normalize=True, dropna=True)
        
        # min/max examples 
        try:
            mn_element = col_data.min()
            mx_element = col_data.max()
        except:
            mn_element = col_data.astype(str).min()
            mx_element = col_data.astype(str).max()

        info_dict['example_min'].append(((round(frac_data[mn_element], 3)), mn_element))
        info_dict['example_max'].append(((round(frac_data[mx_element], 3)), mx_element))

        # moda
        mff_max_value = frac_data.index[0] if len(frac_data) else '●'
        mff_max_fraction = frac_data.iloc[0] if len(frac_data) else 0
        info_dict['moda'].append((round(mff_max_fraction, 3) if mff_max_fraction != 0 else '●', mff_max_value))
        
        # fraction of null values
        nan_ratio = col_data.isna().mean()
        info_dict['nan_values'].append(round(nan_ratio, 3) if nan_ratio != 0 else '●')
        
        # fraction of zero values
        zeros = (col_data == 0).mean()
        info_dict['zeros'].append(round(zeros, 3) if zeros != 0 else '●')

        # empty strings
        empty_str_ratio = (col_data == '').mean()
        info_dict['empty_str_ratio'].append(round(empty_str_ratio, 3) if empty_str_ratio != 0 else '●')

        #trash score - how many useless values we have
        trash = empty_str_ratio + nan_ratio + zeros
        info_dict['trash_score'].append(round(trash, 3) if trash != 0 else '●') 

    return pd.DataFrame(info_dict, index=df.columns)
