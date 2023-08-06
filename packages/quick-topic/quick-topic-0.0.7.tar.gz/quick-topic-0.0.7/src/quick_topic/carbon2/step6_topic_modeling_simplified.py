from quick_topic.topic_modeling.lda import build_lda_models
import os
meta_csv_file="datasets/list_g20_news.csv"
raw_text_folder="datasets/raw_text"

list_term_file = [
        "../datasets/keywords/countries.csv",
        "../datasets/keywords/leaders_unique_names.csv",
        "../datasets/keywords/carbon2.csv"
    ]

for topic_num in range(4,12):
    result_folder=f"results/topic_modelings/topic_num_{topic_num}"
    if not os.path.exists(result_folder):
        os.mkdir(result_folder)
    stop_words_path = "../datasets/stopwords/hit_stopwords.txt"

    list_category = build_lda_models(
        meta_csv_file=meta_csv_file,
        raw_text_folder=raw_text_folder,
        output_folder=result_folder,
        list_term_file=list_term_file,
        stopwords_path=stop_words_path,
        prefix_filename="text_",
        num_topics=topic_num
    )

    print(list_category)