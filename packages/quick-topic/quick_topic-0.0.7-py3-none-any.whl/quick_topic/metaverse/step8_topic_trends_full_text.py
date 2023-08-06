from quick_topic.topic_trends.trends_by_year_fulltext import *
'''
    Get time trends of numbers of documents containing topic keywords with full text.
'''

# set predefined topic labels
label_names = [
    'Knowledge',
    'Socialization',
    'Digitization',
    'Intelligence'
               ]

# set keywords for each topic

# a list of topics above
list_topics = [
    ['domain knowledge','expert knowledge', 'domain','medical_standard','medical','health','icd','multimodal data','expert','NLP','natural language processing', 'medical_education','train','coding'],
    ['social','social network','virtual reality','virtual','online','internet','platform','community','wearable device','personal','simulation','interaction','communication','face-to-face','VR','interact'],
    ['telemedicine','online','digital','socialization','virtual reality','interaction','multimodal','multimodal data','monitor','remote','avatar','rehabilitation','virtual world','physical world','virtual currency','e-commerce'],
    ['artificial intelligence','artificial','intelligence','web 3.0','clinical','machine_learning','deep learning','expert knowledge','decision-making','decision support','multimodal data','collaborative','immersive']
]

# call function to show trends of number of documents containing topic keywords each year-month
show_year_trends_with_fulltext(
    meta_csv_file="datasets_paper/list_paper.csv",
    list_topics=list_topics,
    label_names=label_names,
    save_result_path="results/topic_trends/trends_fulltext.csv",
    minimum_year=2010,
    raw_text_path=r"datasets_paper/raw_text",
    id_field='file_id',
    time_field='PY',
    prefix_filename=""
)
