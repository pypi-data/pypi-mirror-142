from quick_topic.topic_modeling.lda import *
from quickcsv.file import *
import os
meta_csv_file="datasets_paper/list_paper.csv"
raw_text_folder="datasets_paper/raw_text"

dict_country={}
list_item=read_csv(meta_csv_file)

for item in list_item:
    area=item['category']
    id=item['file_id']
    text_path=f'{raw_text_folder}/{id}.txt'
    if not os.path.exists(text_path):
        continue
    text=read_text(text_path)
    if text.strip()=="":
        continue
    if area in dict_country:
        dict_country[area].append(text)
    else:
        dict_country[area]=[text]

list_term_file = [

    ]

stop_words_path = ""

for country in dict_country:
    list_topic_weight=build_lda_model(
        list_doc=dict_country[country],
        output_folder='results/topic_modeling',
        stopwords_path=stop_words_path,
        save_name=country,
        list_term_file=list_term_file,
        lang='en'
    )
    # print(list_topic_weight)
    for topic in list_topic_weight:
        for k in topic:
            print(f"{topic['topic_num']}\t{topic['topic_percent']}\t{topic['topic_keywords']}")
    print()

