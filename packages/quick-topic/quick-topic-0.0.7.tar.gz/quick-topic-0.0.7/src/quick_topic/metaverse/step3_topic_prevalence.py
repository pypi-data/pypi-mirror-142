from quick_topic.topic_prevalence.main import *
'''
    Estimate yearly topic prevalence trends over topics
'''
# data file: a csv file; a folder with txt files named the same as the ID field in the csv file
meta_csv_file = "datasets_paper/list_paper.csv"
text_root = r"datasets_paper/raw_text"

# word segmentation data files
list_keywords_path = [

    ]
# remove keywords
stop_words_path = ""

# date range for analysis
start_year=2010
end_year=2021

# used topics
# set predefined topic labels
label_names = ['Knowledge','Socialization',
               'Digitization','Intelligence'
               ]

# a list of topics above
list_topics = [
    ['domain_knowledge','expert_knowledge', 'domain','knowledge','medical_standard','medical','health','icd','multimodal_data','information','expert','NLP','natural_language_processing', 'medical_education','train','coding'],
    ['social','social_network','virtual_reality','virtual','online','internet','platform','community','wearable_device','personal','simulation','interaction','communication','face-to-face','VR','interact'],
    ['telemedicine','online','digital','socialization','vr','virtual_reality','interaction','virtual','multimodal','multimodal_data','monitor','remote','platform','avatar','rehabilitation','physical','virtual_word','physical_word','virtual_currency','e-commerce','connection','transmit','real-world'],
    ['artificial_intelligence','artificial','intelligence','ai','vr','ar','web_3.0','clinical','machine_learning','deep_learning','distributed','expert_knowledge','decision-making','decision_support','multimodal_data','collaborative','immersive']
]

# run-all

run_topic_prevalence(
    meta_csv_file=meta_csv_file,
    raw_text_folder=text_root,
    save_root_folder="results/topic_prevalence",
    list_keywords_path=list_keywords_path,
    stop_words_path=stop_words_path,
    start_year=start_year,
    end_year=end_year,
    label_names=label_names,
    list_topics=list_topics,
    tag_field="category",
    time_field="PD",
    id_field="file_id",
    prefix_filename="",
    lang='en'
)