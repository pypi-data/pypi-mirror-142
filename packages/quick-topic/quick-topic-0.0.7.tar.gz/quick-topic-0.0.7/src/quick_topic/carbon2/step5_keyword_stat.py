from quick_topic.topic_stat.stat_by_keyword import *
'''
    Stat sentence numbers by keywords
'''
meta_csv_file='datasets/list_g20_news.csv'

raw_text_folder="datasets/raw_text"

keywords_energy = ['煤炭', '天然气', '石油', '生物', '太阳能', '风能', '氢能', '水力', '核能']

stat_sentence_by_keywords(
    meta_csv_file=meta_csv_file,
    keywords=keywords_energy,
    id_field="fileId",
    raw_text_folder=raw_text_folder,
    contains_keyword_in_sentence='',
    prefix_file_name='text_'
)

