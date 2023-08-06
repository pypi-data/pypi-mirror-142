from quick_topic.topic_stat.stat_by_keyword import *
'''
    Stat sentence numbers by keywords
'''
meta_csv_file='datasets_paper/list_paper.csv'

raw_text_folder="datasets_paper/raw_text"

keywords_metaverse = ['virtual reality', 'augmented reality', 'mixed reality', 'virtual world', 'avatar', '3d world', 'hyper reality', 'digital economy','social network','gaming','immersive']

keywords_health_metaverse=['telemedicine','virtual reality','augmented reality','medical information','online health communities','digital health','mobile health']

keywords_metaverse_perspective=['digital transformation','digital economy','blockchain','artificial intelligence','digital twin','wearable device','multimodal data']

labels=["Metaverse-related","Health Metaverse-related",'Metaverse perspective']

keywords=[
    keywords_metaverse,
    keywords_health_metaverse,
    keywords_metaverse_perspective
]

list_dict=[]

for the_keyword in keywords:
    r=stat_sentence_by_keywords(
        meta_csv_file=meta_csv_file,
        keywords=the_keyword,
        id_field="file_id",
        raw_text_folder=raw_text_folder,
        contains_keyword_in_sentence='',
        prefix_file_name=''
    )
    list_dict.append(r)

print()
list_all_words=[]
for dict in list_dict:
    for k in dict:
        if k not in list_all_words:
            list_all_words.append(k)

print("keyword\t"+"\t".join(labels))
for w in list_all_words:
    list_v=[]
    for dict in list_dict:
        count=0
        if w in dict.keys():
            count=dict[w]
        list_v.append(str(count))
    print(w+"\t"+ "\t".join(list_v))

