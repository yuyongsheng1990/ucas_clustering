from sklearn.cluster import KMeans

#将二进制simhash向量的每一维转换成float型数值，然后存储到列表中
file_input=open('c:/users/yys/desktop/data_simhash.txt')
file_output=open('c:/users/yys/desktop/data_k-means.txt','w')
x=[]
for line in file_input:
    #id=line.split('\t')[0]
    simhash_value=line.split('\t')[1].strip()
    simhash_float=[float(i) for i in simhash_value]
    x.append(simhash_float)
x_result=KMeans(n_clusters=100,init='k-means++',n_init=300,max_iter=200).fit_predict(x,y=None)
print(x_result)
for i in x_result:
    file_output.writelines(str(i)+'\n')
