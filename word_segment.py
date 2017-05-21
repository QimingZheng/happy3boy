import jieba
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


def document_abtain(file_name):
    file=open(file_name)
    text=file.read()
    return text
    
def document_segmentation(text):
    seg_list=jieba.cut(text)
    file=open("segmentation_result_dev.txt","w")
    for word in seg_list:
        file.write(word)
        file.write(' ')

def main():
    #text=document_abtain("./BoP2017-DBQA.train.txt")
    text=document_abtain("./BoP2017-DBQA.dev.txt")
    document_segmentation(text)



main()
    

