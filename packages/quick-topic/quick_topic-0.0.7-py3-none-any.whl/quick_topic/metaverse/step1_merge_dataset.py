from quickcsv.file import *

list_item1=read_csv("../datasets/google_news_datasets/metaverse/list_news.csv")
list_item2=read_csv("../datasets/google_news_datasets/healthcare_medical/list_news.csv")

for idx,item in enumerate(list_item1):
    list_item1[idx]['category']='Metaverse-related'

for idx,item in enumerate(list_item2):
    list_item2[idx]['category']='Health-Metaverse-related'

list_item=list_item1+list_item2

write_csv('datasets/list_news_all.csv',list_item)
