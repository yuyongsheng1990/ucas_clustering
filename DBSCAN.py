from sklearn.cluster import DBSCAN as db

#将二进制simhash向量的每一维转换成float型数值，然后存储到列表中
file_input=open('c:/users/yys/desktop/data_simhash.txt')
file_output=open('c:/users/yys/desktop/data_dbscan.txt','w')
x=[]
for line in file_input:
    #id=line.split('\t')[0]
    simhash_value=line.split('\t')[1].strip()
    simhash_float=[float(i) for i in simhash_value]
    x.append(simhash_float)
x_result=db(eps=5.0,min_samples=2).fit_predict(x)
print(x_result)
for i in x_result:
    file_output.writelines(str(i)+'\n')


