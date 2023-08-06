from quick_topic.topic_modeling.lda import build_lda_models
from quick_topic.topic_similarity.topic_similarity_by_category import *
'''
    Estimate topic similarity between two groups of LDA topics
'''
# Step 1: build topic models
meta_csv_file="datasets_paper/list_paper.csv"
raw_text_folder="datasets_paper/raw_text"

list_term_file = [
    ]

stop_words_path = ""

list_category = build_lda_models(
    meta_csv_file=meta_csv_file,
    raw_text_folder=raw_text_folder,
    output_folder="results/topic_similarity_two/topics",
    list_term_file=list_term_file,
    stopwords_path=stop_words_path,
    prefix_filename="",
    num_topics=6,
    num_words=50,
    tag_field='category',
    id_field='file_id',
    lang='en'
)

# Step 2: estimate similarity

output_folder = "results/topic_similarity_two/topics"

keywords_file="../datasets/keywords/carbon2.csv"

estimate_topic_similarity(
    list_topic=list_category,
    topic_folder=output_folder,
  #  list_keywords_file=keywords_file,
    lang='en'

)


