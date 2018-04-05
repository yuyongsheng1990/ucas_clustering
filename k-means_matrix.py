# 利用英文专利分类中的upc分类号生成共现矩阵(稀疏矩阵),将共现矩阵转换为能用于聚类的特征向量
import re
import xlrd
import numpy as np
from scipy.sparse import coo_matrix
from sklearn.cluster import KMeans

file_input=xlrd.open_workbook('c:/users/yys/desktop/test_data.xlsx')
file_output=open('c:/users/yys/desktop/test_matrix.txt','w')
#定义一个共现函数，用于记录单个专利中upc类号的共现关系
def co_exist(upc_list):
    i=0
    upc_list_copy = upc_list.copy()
    while i < len(upc_list):
        upc1=upc_list[i].strip() #分类号'H04L12/24'
        upc1_num=upc_list_all.index(upc1) #分类号离散化，用数字0表示
        upc_list_copy.remove(upc_list[i])
        j=0
        while j < len(upc_list_copy):
            upc2=upc_list_copy[j].strip()
            upc2_num=upc_list_all.index(upc2)
            if upc1_num in row and upc2_num in col: #coo_matrix的行和列-列表中是否包含upc分类号
                temp_num=0
                foo_value=True
                while temp_num < len(row): #判断行分类号在row中的index与列分类号在col中的index是否对齐，若对齐则为同一共现，否则不为同一共现
                    #如共现(2,3)，而现有的row=[2,4];col=[1,2]
                    if row[temp_num]==upc1_num and col[temp_num]==upc2_num:
                        data[temp_num]+=1
                        foo_value=False
                        break
                    temp_num += 1
                if foo_value:
                    row.append(upc1_num);
                    col.append(upc2_num);
                    data.append(1)  # 分类号表示数字在列表中的索引index=row.index(upc1_num)
            else:
                row.append(upc1_num);col.append(upc2_num);data.append(1)

            if upc2_num in row and upc1_num in col: # 因为要实现共现关系，如(2,3)=1;(3,2)=1
                temp_num=0
                foo_value=True
                while temp_num < len(row):
                    if row[temp_num]==upc2_num and col[temp_num]==upc1_num:
                        data[temp_num]+=1
                        foo_value=False
                        break
                    temp_num += 1
                if foo_value:
                    row.append(upc2_num)
                    col.append(upc1_num)
                    data.append(1)

            else:
                row.append(upc2_num);col.append(upc1_num);data.append(1)
            j+=1
        i+=1

# 1.读入excel英文专利数据
table=file_input.sheets()[0] #sheet1存储着原始数据2015-2017年的数据
    #1.1将所有不同的技术类号添加到列表中
upc_list_all=[]
row=[]
col=[]
data=[]
for i in range(table.nrows):
    if i==0: continue
    upc_list=str(table.row_values(i)[10]).split(';')
    for j in upc_list:
        if j.strip() in upc_list_all:
            continue
        else:
            upc_list_all.append(j.strip()) #注意清除upc类号前后的空格
#print(upc_list_all)
print(len(upc_list_all))
'''for i in upc_list_all:
    file_output2.writelines(i+'\n') 
#file_output2.close()'''
    #1.2 利用sparse.coo_matrix生成英文专利upc类号的共现矩阵
for i in range(table.nrows):
    if i==0: continue
    upc_list = str(table.row_values(i)[10]).split(';')
    co_exist(upc_list)
co_exist_matrix=coo_matrix((data,(row,col)),shape=(max(row)+1,max(col)+1)).todense()
#co_exist_matrix.getA
#np.set_printoptions(threshold=np.inf)
#print (str(co_exist_matrix))
'''# 2.将共现矩阵输出为能用于聚类的特征向量
i=0
while i < len(co_exist_matrix):
    upc_title=upc_list_all[i]
    file_output.writelines(upc_title+'\t')
    #print(co_exist_matrix[i])
    file_output.writelines(str(co_exist_matrix[i]))
    file_output.writelines('\n')
    i+=1
file_output.close()'''
#3. 直接在python内部聚类
x_result=KMeans(n_clusters=100,init='k-means++',n_init=300,max_iter=200).fit_predict(co_exist_matrix,y=None)
print(x_result)
for i in x_result:
    file_output.writelines(str(i)+'\n')
