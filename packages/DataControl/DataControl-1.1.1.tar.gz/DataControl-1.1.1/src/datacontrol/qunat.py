# 获取没有填写备注的人的名字并去重
import pandas as pd

def qunat(flie_path,write_path,name_idx,qianzhui='',info_idx=''):
    
    df = pd.read_csv(flie_path, header=0)
    if info_idx == '':
        info_idx = df.shape[1]    #备注所在列数（默认最后一列）

    name = []

    for i in range(df.shape[0]):
        print(i,':',df.iloc[i,name_idx-1])
        if pd.isnull(df.iloc[i,info_idx-1]) and (str(qianzhui)+str(df.iloc[i,name_idx-1]) ) not in name:
            name.append(str(qianzhui) + str(df.iloc[i,name_idx-1]))

    name = pd.DataFrame(name)
    name = pd.DataFrame(name.iloc[:,0].unique())    #去重

    name.to_csv(write_path,index=None,header=None)