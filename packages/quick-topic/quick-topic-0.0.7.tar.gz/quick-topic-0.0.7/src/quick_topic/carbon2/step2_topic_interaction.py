from quick_topic.topic_interaction.main import *
# step 1: data file
meta_csv_file = "datasets/list_g20_news.csv"
text_root = r"datasets/raw_text"

# step2: jieba cut words file
list_keywords_path = [
        "../datasets/keywords/countries.csv",
        "../datasets/keywords/leaders_unique_names.csv",
        "../datasets/keywords/carbon2.csv"
    ]

# remove files
stopwords_path = "../datasets/stopwords/hit_stopwords.txt"

# set predefined topic labels
label_names = ['经济主题', '能源主题', '公众主题', '政府主题']

# set keywords for each topic
topic_economics = ['投资', '融资', '经济', '租金', '政府', '就业', '岗位', '工作', '职业', '技能']
topic_energy = ['绿色', '排放', '氢能', '生物能', '天然气', '风能', '石油', '煤炭', '电力', '能源', '消耗', '矿产', '燃料', '电网', '发电']
topic_people = ['健康', '空气污染', '家庭', '能源支出', '行为', '价格', '空气排放物', '死亡', '烹饪', '支出', '可再生', '液化石油气', '污染物', '回收',
                '收入', '公民', '民众']
topic_government = ['安全', '能源安全', '石油安全', '天然气安全', '电力安全', '基础设施', '零售业', '国际合作', '税收', '电网', '出口', '输电', '电网扩建',
                    '政府', '规模经济']

# a list of topics above
list_topics = [
    topic_economics,
    topic_energy,
    topic_people,
    topic_government
]

# if any keyword is the below one, then the keyword is removed from our consideration
filter_words = ['中国', '国家', '工作', '领域', '社会', '发展', '目标', '全国', '方式', '技术', '产业', '全球', '生活', '行动', '服务', '君联',
                '研究', '利用', '意见']

# dictionaries
'''
list_country=[
    '巴西','印度','俄罗斯','南非'
]
'''

list_country=['中国', '俄罗斯', '南非', '印尼', '沙特', '韩国', '日本', '印度', '土耳其', '墨西哥', '阿根廷', '澳大利亚', '加拿大', '巴西', '意大利', '德国', '欧盟', '法国', '美国', '英国']


# run shell
run_topic_interaction(
    meta_csv_file=meta_csv_file,
    raw_text_folder=text_root,
    output_folder="results/topic_interaction/divided",
    list_category=list_country, # a dictionary where each record contain a group of keywords
    stopwords_path=stopwords_path,
    weights_folder='results/topic_interaction/weights',
    list_keywords_path=list_keywords_path,
    label_names=label_names,
    list_topics=list_topics,
    filter_words=filter_words,
    # set field names
    tag_field="area",
    keyword_field="", # ignore if keyword from csv exists in the text
    time_field="date",
    id_field="fileId",
    prefix_filename="text_",
    num_topics=10,
    num_words=50
)