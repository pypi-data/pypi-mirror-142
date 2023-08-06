from quick_topic.topic_trends_correlation.topic_trends_correlation_two import *
'''
    Estimate the correlation among trends
'''
trends_file="results/topic_trends/trends_fulltext.csv"

label_names=['经济','能源','公民','政府']

list_result=[]
list_line=[]
for i in range(0,len(label_names)-1):
    for j in range(i+1,len(label_names)):
        label1=label_names[i]
        label2=label_names[j]
        result=estimate_topic_trends_correlation_single_file(
            trend_file=trends_file,
            selected_field1=label1,
            selected_field2=label2,
            start_year=2010,
            end_year=2021,
            show_figure=False,
            time_field='Time'
        )
        list_result=[]
        line=f"({label1},{label2})\t{result['pearson'][0]}\t{result['pearson'][1]}"
        list_line.append(line)
        print()

print("Correlation analysis resutls:")
print("Pair\tPearson-Stat\tP-value")
for line in list_line:
    print(line)

