import numpy as np
import pandas as pd

'''转换(transform):格式转换'''
def transform(basic_data,target_data_type):
    
    try:
        df = pd.DataFrame(basic_data)   #先转化成dataframe

    except IOError:

        print("This function does not support JSON format or its converted format") #json格式转换成的数组大小是空的

    else:
        
        # 再转化成指定类型
        data = {

            'dataframe': df,                #转换为dataframe类型
            'pandas': df,                   #pandas支持的格式(虽然还是dataframe)

            'list': df.values.tolist(),     #列表

            'array': df.values,             #数组
            'numpy': np.array(df),          #numpy支持的格式(虽然还是数组)

        }.get(target_data_type,"error, unsupported format")
        return data