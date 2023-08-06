from quick_topic.topic_modeling.lda import *
from quickcsv.file import *
import os
meta_csv_file="datasets/list_country.csv"
raw_text_folder="datasets/raw_text"

dict_country={}
list_item=read_csv(meta_csv_file)

for item in list_item:
    area=item['area']
    id=item['fileId']
    text_path=f'{raw_text_folder}/text_{id}.txt'
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
        "../datasets/keywords/countries.csv",
        "../datasets/keywords/leaders_unique_names.csv",
        "../datasets/keywords/carbon2.csv"
    ]

stop_words_path = "../datasets/stopwords/hit_stopwords.txt"

for country in dict_country:
    build_lda_model(
        list_doc=dict_country[country],
        output_folder='results/topic_modeling',
        stopwords_path=stop_words_path,
        save_name=country,
        list_term_file=list_term_file,
    )

