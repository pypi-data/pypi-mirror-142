from quick_topic.topic_transition.transition_by_year_topic import *


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

for idx,keywords in enumerate(list_topics):
    label=label_names[idx]
    show_transition_by_year_topic(
        root_path="results/topic_transition/divided_year",
        label=label,
        keywords=keywords,
        start_year=2010,
        end_year=2021,
        save_figure=True,
        figure_path=f'results/topic_transition/by_topic/figure_{label}.jpg'
    )

