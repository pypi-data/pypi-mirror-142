import pandas as pd

'''
文本充填
'''
def textfill(file_path,name_idx,group_idx,text_head,cloumn_name_idx,write_path):
    df = pd.read_csv(file_path)

    text  = list(cloumn_name_idx)
    idx = list(cloumn_name_idx.values())


    name_header = df.columns.values.tolist()[name_idx-1]
    df.sort_values(name_header,inplace=True)    #按姓名排序
    name = df.iloc[:,name_idx-1].unique()

    # 按姓名和组名一起去重
    namegroup_distinct = df.drop_duplicates(subset=[df.columns.values.tolist()[name_idx-1],df.columns.values.tolist()[group_idx-1]]).iloc[:,[name_idx-1,group_idx-1]]

    f = open(write_path,'a')    # 'a':追加模式

    info_num = 0    #记录写入文本数
    # 循环写入
    for i in range(len(name)):      # 第i个人

        f.writelines([str(name[i]),'\n'])  #邮箱前缀(姓名)
        f.writelines([str(namegroup_distinct.iloc[i,1]),'\n'])      #组名
        f.writelines(['<----->','\n','\n'])
        f.writelines([text_head,'\n'])
        
        for j in range(len(df)):  # 第i个人的第j行信息

            if df.iloc[j,name_idx-1] == name[i]:
                
                for k in range(len(idx)):   #第j行的多条信息写入
                    f.writelines([text[k],':  ', str(df.iloc[j,idx[k]-1]) ,'\n'])
                info_num += 1
                f.writelines(['\n'])

        f.writelines(['--------------------------------------------------------------------------------------'])    #分割线
        f.writelines(['\n','\n'])

    f.close()

    print("总人数:",len(name))
    print("写入文本数:",info_num)