# drop
## drop columns by column's name
    df = df.drop(columns = ["5-3级区域","longtitude","magtitude"])
# rename columns
## set column's name
    
    df.columns=list('L','M') 
    !!! df不能为空 空会报错
# set index
    Y.set_index(['index'],inplace = True)