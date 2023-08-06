from quick_topic.topic_prevalence.main import *
'''
    Estimate yearly topic prevalence trends over topics
'''
# data file: a csv file; a folder with txt files named the same as the ID field in the csv file
meta_csv_file = "datasets/list_g20_news.csv"
text_root = r"datasets/raw_text"

# word segmentation data files
list_keywords_path = [
        "../datasets/keywords/countries.csv",
        "../datasets/keywords/leaders_unique_names.csv",
        "../datasets/keywords/carbon2.csv"
    ]
# remove keywords
stop_words_path = "../datasets/stopwords/hit_stopwords.txt"

# date range for analysis
start_year=2010
end_year=2021

# used topics
label_names = ['经济主题', '能源主题', '公众主题', '政府主题']
topic_economics = ['投资', '融资', '经济', '租金', '政府', '就业', '岗位', '工作', '职业', '技能']
topic_energy = ['绿色', '排放', '氢能', '生物能', '天然气', '风能', '石油', '煤炭', '电力', '能源', '消耗', '矿产', '燃料', '电网', '发电']
topic_people = ['健康', '空气污染', '家庭', '能源支出', '行为', '价格', '空气排放物', '死亡', '烹饪', '支出', '可再生', '液化石油气', '污染物', '回收',
                '收入', '公民', '民众']
topic_government = ['安全', '能源安全', '石油安全', '天然气安全', '电力安全', '基础设施', '零售业', '国际合作', '税收', '电网', '出口', '输电', '电网扩建',
                    '政府', '规模经济']

list_topics = [
    topic_economics,
    topic_energy,
    topic_people,
    topic_government
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
    tag_field="area",
    time_field="date",
    id_field="fileId",
    prefix_filename="text_",
    num_words=10
)