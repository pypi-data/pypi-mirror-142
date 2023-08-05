import pandas as pd
from dataito.transform import transform

'''输出:数据保存'''
def save(data,savepath = " "):

    data = transform(data,'dataframe')      #统一转换为dataframe

    if isinstance(data,pd.DataFrame):
        if savepath == " ":                             #如果没有填写路径或文件名
            data.to_excel("data.xlsx")                  #默认文件名为data.xlsx
        elif savepath != " ":                           
            data.to_excel(savepath)                     
        else:
            print("save failed") 
    else:
        print("error, unsupported format")