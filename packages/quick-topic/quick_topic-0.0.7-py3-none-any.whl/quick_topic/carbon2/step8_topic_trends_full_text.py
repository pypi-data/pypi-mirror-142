from quick_topic.topic_trends.trends_by_year_month_fulltext import *
'''
    Get time trends of numbers of documents containing topic keywords with full text.
'''

# define a group of topics with keywords, each topic has a label
label_names=['经济','能源','公民','政府']

keywords_economics = ['投资', '融资', '经济', '租金', '政府', '就业', '岗位', '工作', '职业', '技能']
keywords_energy = ['绿色', '排放', '氢能', '生物能', '天然气', '风能', '石油', '煤炭', '电力', '能源', '消耗', '矿产', '燃料', '电网', '发电']
keywords_people = ['健康', '空气污染', '家庭', '能源支出', '行为', '价格', '空气排放物', '死亡', '烹饪', '支出', '可再生', '液化石油气', '污染物', '回收',
                   '收入', '公民', '民众']
keywords_government = ['安全', '能源安全', '石油安全', '天然气安全', '电力安全', '基础设施', '零售业', '国际合作', '税收', '电网', '出口', '输电', '电网扩建',
                       '政府', '规模经济']

list_topics = [
    keywords_economics,
    keywords_energy,
    keywords_people,
    keywords_government
]

# call function to show trends of number of documents containing topic keywords each year-month
show_year_month_trends_with_fulltext(
    meta_csv_file="datasets/list_g20_news.csv",
    list_topics=list_topics,
    label_names=label_names,
    save_result_path="results/topic_trends/trends_fulltext.csv",
    minimum_year=2010,
    raw_text_path=r"datasets/raw_text",
    id_field='fileId',
    time_field='date',
    prefix_filename="text_"
)
