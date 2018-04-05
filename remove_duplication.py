import xlrd
import xlwt
import re
import nltk
from nltk.corpus import stopwords

def filter_puntuation(string):
    text=re.sub('[\.\!\/_,-:;<>≦$%^*()+\"\']+|[+——！，。？、~@#￥%……&*（）]+',' ',string)
    text=re.sub('  ',' ',text,3)
    return text

# 1. 导入excel英文专利数据
file_input=xlrd.open_workbook('c:users/yys/desktop/Data_fivePartyPatents.xls')
file_output=xlwt.Workbook(encoding='utf-8',style_compression=0)
table=file_input.sheets()[0]#选择操作的sheet表
table_output=file_output.add_sheet('sheet1',cell_overwrite_ok=True)
data=[]
line_num = 0
for i in range(table.nrows):
    #if i==0: continue
    table_value=table.row_values(i)
    # print(table_value
    title, abstract=table_value[1],table_value[2]
    patent_text=title.lower().strip()+' '+abstract.lower().strip()
    #print(patent_text)
# 2. 过滤英文停用词
    segmenter_text=nltk.word_tokenize(filter_puntuation(patent_text)) #过滤英文标点
    #print(segmenter_text)
    filter_text=[w for w in segmenter_text if(w not in stopwords.words('english'))]
    #print(filter_text)
# 3. 判断是否重复
    if filter_text in data:
        continue
    else:
# 4. 输出
        data.append(filter_text)
        for j in range(len(table_value)):
            table_output.write(line_num, j, table_value[j])
        line_num+=1
file_output.save(r'c:/users/yys/desktop/Data_fivePartyPatents_remove_dumplication.xls')