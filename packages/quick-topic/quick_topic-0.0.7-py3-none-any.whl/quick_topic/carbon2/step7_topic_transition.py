from quick_topic.topic_transition.transition_by_year_month_term import *
from quick_topic.topic_transition.divide_by_year_month import *
'''
    Estimate the topic transition over time
'''
meta_csv_file="datasets/list_g20_news.csv"
raw_text_folder=r"datasets/raw_text"
output_divided_folder="results/topic_transition/divided_year_month"
output_figure_folder="results/topic_transition/figures"
select_keywords = ['燃煤', '储能', '电动汽车', '氢能', '脱碳', '风电', '水电', '天然气', '光伏', '可再生', '清洁能源', '核电']
start_year=2010
end_year=2021

# Step 1: divide the dataset by year-month
divide_by_year_month(
    meta_csv_file=meta_csv_file,
    raw_text_folder=raw_text_folder,
    output_folder=output_divided_folder,
    start_year=start_year,
    end_year=end_year,
    id_field='fileId',
    tag_field='area',
    time_field='date',
    prefix_filename='text_'
)

# Step 2: analyze the divided datasets
'''
list_all_range = [
    [[2010, 2015], [2016, 2021]],
    [[2011, 2017], [2018, 2021]],
    [[2009, 2017], [2018, 2021]],
    [[2011, 2016], [2017, 2021]],
    [[2017, 2018], [2019, 2021]],
    [[2009, 2014], [2015, 2021]],
    [[2009, 2014], [2015, 2021]],
    [[2009, 2015], [2016, 2021]],
    [[2008, 2011], [2012, 2015], [2016, 2021]],
    [[2011, 2016], [2017, 2021]],
    [[2009, 2012], [2013, 2016], [2017, 2021]],
    [[2009, 2015], [2016, 2021]]
]
'''
list_all_range=None

show_transition_by_year_month_term(
    root_path=output_divided_folder,
    select_keywords=select_keywords,
    list_all_range=list_all_range,
    output_figure_folder=output_figure_folder,
    start_year=start_year,
    end_year=end_year,
min_total_num=20,maximum_rate_if_meet_min_num=0.7,font_size=16,
    x_label='年份',
    y_label='文档比例'
)