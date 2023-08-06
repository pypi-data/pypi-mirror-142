from quick_topic.topic_interaction.main import *
# step 1: data file
meta_csv_file = "datasets_paper/list_paper.csv"
text_root = r"datasets_paper/raw_text"

def get_categories(csv_file):
    list_item=read_csv(csv_file)
    list_ca=[]
    for item in list_item:
        if item['category'] not in list_ca:
            list_ca.append(item['category'])
    return list_ca

# step2: jieba cut words file
list_keywords_path = [

    ]

# remove files
stopwords_path = ""

# set predefined topic labels
label_names = ['Knowledge','Socialization',
               'Digitization','Intelligence'
               ]

# set keywords for each topic

# a list of topics above
list_topics = [
    ['domain_knowledge','expert_knowledge', 'domain','knowledge','medical_standard','medical','health','icd','multimodal_data','information','expert','NLP','natural_language_processing', 'medical_education','train','coding'],
    ['social','social_network','virtual_reality','virtual','online','internet','platform','community','wearable_device','personal','simulation','interaction','communication','face-to-face','VR','interact'],
    ['telemedicine','online','digital','socialization','vr','virtual_reality','interaction','virtual','multimodal','multimodal_data','monitor','remote','platform','avatar','rehabilitation','physical','virtual_word','physical_word','virtual_currency','e-commerce','connection','transmit','real-world'],
    ['artificial_intelligence','artificial','intelligence','ai','vr','ar','web_3.0','clinical','machine_learning','deep_learning','distributed','expert_knowledge','decision-making','decision_support','multimodal_data','collaborative','immersive']
]

# if any keyword is the below one, then the keyword is removed from our consideration
filter_words = []

# dictionaries
list_category=get_categories(csv_file=meta_csv_file)
print(list_category)

# run shell
run_topic_interaction(
    meta_csv_file=meta_csv_file,
    raw_text_folder=text_root,
    output_folder="results/topic_interaction/divided",
    list_category=list_category, # a dictionary where each record contain a group of keywords
    stopwords_path=stopwords_path,
    weights_folder='results/topic_interaction/weights',
    list_keywords_path=list_keywords_path,
    label_names=label_names,
    list_topics=list_topics,
    filter_words=filter_words,
    # set field names
    tag_field="category",
    keyword_field="", # ignore if keyword from csv exists in the text
    time_field="PD",
    id_field="file_id",
    prefix_filename="",
    lang='en'
)