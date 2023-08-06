from quick_topic.topic_modeling.lda import build_lda_models
from quick_topic.topic_similarity.topic_similarity_by_category import *
'''
    Estimate topic similarity between two groups of LDA topics
'''
# Step 1: build topic models
meta_csv_file="datasets/list_g20_news.csv"
raw_text_folder="datasets/raw_text"

list_term_file = [
        "../datasets/keywords/countries.csv",
        "../datasets/keywords/leaders_unique_names.csv",
        "../datasets/keywords/carbon2.csv"
    ]

stop_words_path = "../datasets/stopwords/hit_stopwords.txt"

list_category = build_lda_models(
    meta_csv_file=meta_csv_file,
    raw_text_folder=raw_text_folder,
    output_folder="results/topic_similarity_two/topics",
    list_term_file=list_term_file,
    stopwords_path=stop_words_path,
    prefix_filename="text_",
    num_topics=10,
    num_words=50
)

# Step 2: estimate similarity

output_folder = "results/topic_similarity_two/topics"

keywords_file="../datasets/keywords/carbon2.csv"

estimate_topic_similarity(
    list_topic=list_category,
    topic_folder=output_folder,
    list_keywords_file=keywords_file,

)


