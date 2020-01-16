def preprocess(fpath):
    df=pd.read_csv( fpath)
    for col in df.columns:
        if 'ime' in col:
            break
    else:
        return {'failed' : 'configure csv with datetime columns'}
    df.index = col
    df.drop(columns=[col],inplace=True)
    # y = df['Species'][0]
    # if y not in (1,4):
    #     continue
    # if df.shape[0] < 100:
    #     continue
    # if y == 4:
    #     y = 0
    # df.drop(columns=['Species'],inplace=True)
    for param in ['Lat', 'Long', 'Alt']:
        df['v_' + param ] = 0
        df['v_' + param][1:] = df[param][1:].values - df[param][:-1].values
        df = df.iloc[1:,:]
    df['v_Alt'] /= 60
    for param in ['Alt']:
        df['a_'  + param ] = 0
        df['a_'  + param][1:] = df['v_' + param][1:].values - df['v_' + param][:-1].values
        df = df.iloc[1:,:]
    df['a_Alt'] /= 60
    row = []
    
    for cols in df.columns:   
        row.extend(df[cols].values[:100])
    row = pd.Series(row)
    return row
