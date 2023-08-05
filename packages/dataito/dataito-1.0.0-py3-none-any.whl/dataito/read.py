import pandas as pd
import numpy as np
import json

'''输入(input):数据读取'''
def read(path,header=0):
    print(header)
    DataFormat = path.split(".")[1] #获取文件后缀

    # 前两种格式特殊处理(否则会报错)
    
    # xlsx
    if DataFormat == 'xlsx':
        if str(header) == '0' or str(header) == 'True':     #直接用header不行
            data = pd.read_excel(path,engine='openpyxl',header=0)
        elif str(header) == 'None' or str(header) == 'False':
            data = pd.read_excel(path,engine='openpyxl',header=None)
        else:
            print("header参数错误,建议使用None或0")
        return np.array(data)
    
    # csv 
    elif DataFormat == 'csv':
        if str(header) == '0' or str(header) == 'True':
            data = pd.read_csv(path,"r")
        elif str(header) == 'None' or str(header) == 'False':
            data = pd.read_csv(path,header=None)
        else:
            print("header参数错误,建议使用None或0")
        return data

    # json
    elif DataFormat == 'json':
        data = json.loads(open(path).read())
        return data

    # txt
    elif DataFormat == 'txt':
        data = open(path, "r").read().splitlines(), #不保留换行符
        return data

    # other
    else:
        print("不支持的文件格式")


    ## 弃用
    # else:
        
    #     # 字典格式保留速度较快
    #     data = {
    #         # 'txt': open(path,"r").readlines(),    #保留换行符
    #         'txt': open(path, "r").read().splitlines(), #不保留换行符
    #         'csv': pd.read_csv(path,"r"),

    #          #这几个比较离谱，放在这里就会报错
    #         # 'json': pd.read_json(path,"r")
    #         # 'json': json.loads(open(path).read())
    #         # 'xlsx': pd.read_excel(path,engine='openpyxl')
    #     }.get(DataFormat,"error, unsupported format")

        return np.array(data)
