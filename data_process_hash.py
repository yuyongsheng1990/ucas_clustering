# 文本二进制向量

import xlrd
import re
import nltk
from nltk.corpus import stopwords
from simhash import Simhash


#nltk.download('punkt')
#nltk.download('stopwords') 在第一次导入停用词表后就屏蔽掉，然后补充英文停用词表english

def filter_puntuation(string):
    text=re.sub('[\.\!\/_,-:;<>≦$%^*()+\"\']+|[+——！，。？、~@#￥%……&*（）]+',' ',string)
    text=re.sub('  ',' ',text,3)
    return text

# 1. 导入excel英文专利数据
file_input=xlrd.open_workbook('c:users/yys/desktop/Data_fivePartyPatents.xls')
file_output=open(r'c:/users/yys/desktop/data_simhash2015-2017.txt','w')
table=file_input.sheets()[1]
for i in range(table.nrows):
    if i==0: continue
    table_value=table.row_values(i)
    # print(table_value
    id=int(table_value[0]) #专利的id
    title, abstract=table_value[1],table_value[2]#,table_value[8]
    patent_text=title.lower().strip()+' '+abstract.lower().strip()#+' '+claims.lower().strip()
    #print(patent_text)
# 2. 过滤英文停用词
    segmenter_text=nltk.word_tokenize(filter_puntuation(patent_text)) #过滤英文标点
    #print(segmenter_text)
    filter_text=[w for w in segmenter_text if(w not in stopwords.words('english'))]
    #print(filter_text)
#3. 生成simhash二进制指纹
    simhash_=Simhash(filter_text).value
    file_output.writelines(str(id)+'\t'+str(simhash_)+'\n')
file_output.close()




