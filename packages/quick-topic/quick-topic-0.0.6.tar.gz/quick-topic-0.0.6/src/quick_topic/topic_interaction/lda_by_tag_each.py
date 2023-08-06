import os
import os
from gensim import corpora, models
import gensim
import re
from quickcsv.file import *
import jieba
import jieba.posseg as pseg
from nltk.tokenize import word_tokenize
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from gensim.utils import lemmatize, simple_preprocess
import spacy

def get_text_english(list_doc):
    return singularize(list_doc)

def singularize(text,min_count=5,threshold=100):
    from nltk.corpus import stopwords
    stop_words = stopwords.words('english')
    def sent_to_words(sentences):
        for sent in sentences:
            sent = re.sub('\S*@\S*\s?', '', sent)  # remove emails
            sent = re.sub('\s+', ' ', sent)  # remove newline chars
            sent = re.sub("\'", "", sent)  # remove single quotes
            sent = gensim.utils.simple_preprocess(str(sent), deacc=True)
            # print(sent)
            yield (sent)

            # Convert to list
    data_words = list(sent_to_words(text))

    # Build the bigram and trigram models
    bigram = gensim.models.Phrases(data_words, min_count=min_count,
                                   threshold=threshold)  # higher threshold fewer phrases.
    trigram = gensim.models.Phrases(bigram[data_words], threshold=threshold)
    bigram_mod = gensim.models.phrases.Phraser(bigram)
    trigram_mod = gensim.models.phrases.Phraser(trigram)

    # allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']
    allowed_postags = ['NOUN']

    # !python3 -m spacy download en  # run in terminal once
    def process_words(texts, stop_words=stop_words, allowed_postags=None):
        """Remove Stopwords, Form Bigrams, Trigrams and Lemmatization"""
        texts = [[word for word in simple_preprocess(str(doc)) if word not in stop_words] for doc in texts]
        texts = [bigram_mod[doc] for doc in texts]
        texts = [trigram_mod[bigram_mod[doc]] for doc in texts]
        texts_out = []
        nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])
        for sent in texts:
            doc = nlp(" ".join(sent))
            texts_out.append([token.lemma_ for token in doc if token.pos_ in allowed_postags])
        # remove stopwords once more after lemmatization
        texts_out = [[word for word in simple_preprocess(str(doc)) if word not in stop_words] for doc in texts_out]
        return texts_out

    data_ready = process_words(data_words,stop_words=stop_words,allowed_postags=allowed_postags)  # processed Text Data!
    return data_ready


def get_text_chinese(list_doc,stopwords_path):
    stopwords=[]
    if os.path.exists(stopwords_path):
        stopwords = [w.strip() for w in open(stopwords_path, 'r', encoding='utf-8').readlines()
                 if w.strip() != ""]

    # load data
    # dict_dataset=pickle.load(open("datasets/weibo_vae_dataset_prepared_with_domain.pickle", "rb"))

    # compile sample documents into a list
    # doc_set = [doc_a, doc_b, doc_c, doc_d, doc_e]

    doc_set = []
    for doc in list_doc:
        # list_words=jieba.cut(doc,cut_all=False)
        list_words = pseg.cut(doc)
        list_w = []
        for w, f in list_words:
            if f in ['n', 'nr', 'ns', 'nt', 'nz', 'vn', 'nd', 'nh', 'nl', 'i']:
                if w not in stopwords and len(w) != 1:
                    list_w.append(w)
        # print(list_w)
        doc_set.append(list_w)

    # list for tokenized documents in loop
    texts = []

    # loop through document list
    for tokens in doc_set:
        # clean and tokenize document string

        # stem tokens
        # stemmed_tokens = [p_stemmer.stem(i) for i in tokens]

        # add tokens to list
        texts.append(tokens)
    return texts

def LDA(field,list_doc,weights_path,list_keywods_path,stopwords_path,num_topics=6,num_words=50,num_pass=5,lang='zh'):

    # ============ begin configure ====================
    NUM_TOPICS = num_topics
    NUM_WORDS = num_words
    FIG_V_NUM = 2
    FIG_H_NUM = 3
    WC_MAX_WORDS = 20
    NUM_PASS = num_pass
    # ============ end configure ======================


    # qc_write("results/result_expert.csv",list_result)
    texts=None
    if lang=='zh':

        for pp in list_keywods_path:
            print(pp)
            words=[w.strip() for w in open(pp,'r',encoding='utf-8').read().split("\n")]
            for w in words:
                jieba.add_word(w,1)
        texts=get_text_chinese(list_doc,stopwords_path=stopwords_path)
    else:
        texts=get_text_english(list_doc)

    # turn our tokenized documents into a id <-> term dictionary
    dictionary = corpora.Dictionary(texts)

    # convert tokenized documents into a document-term matrix
    corpus = [dictionary.doc2bow(text) for text in texts]

    # generate LDA model
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=NUM_TOPICS, id2word=dictionary, passes=NUM_PASS)

    # print keywords
    topics = ldamodel.print_topics(num_words=NUM_WORDS, num_topics=NUM_TOPICS)

    save_topic_weights(field,topics,weights_path)

def save_topic_weights(field,topics,weights_path):
    f_out_k=open(f"{weights_path}/{field}_k.csv",'w',encoding='utf-8')
    f_out_v = open(f"{weights_path}/{field}_v.csv", 'w', encoding='utf-8')
    for topic in topics:
        print(topic)
        topic_id=topic[0]
        list_keywords=[]
        list_weight=[]
        s=str(topic[1])
        for k in s.split("+"):
            fs=k.split("*")
            w=fs[0].strip()
            keyword=fs[1].replace("\"","").strip()
            # print(keyword,w)
            list_keywords.append(keyword)
            list_weight.append(str(w))
        # print(','.join(list_keywords))
        # print("total weight:",round(np.sum(list_weight,4)))
        f_out_k.write(','.join(list_keywords)+"\n")
        f_out_v.write(','.join(list_weight)+"\n")
    f_out_v.close()
    f_out_k.close()

def lda_by_tag_each(list_category,root_path,weights_path,list_keywords_path,stopwords_path,minimum_num_doc=15,num_topics=6,num_pass=5,num_words=50,lang='zh'):
    if not os.path.exists(weights_path):
        os.mkdir(weights_path)
    print("Building topic models...")
    for country in list_category:
        list_doc = []

        if not os.path.exists(os.path.join(root_path, country)):
            continue
        for file in os.listdir(os.path.join(root_path, country)):
            folder = f"{root_path}/{country}/{file}"
            if not os.path.exists(folder):
                continue
            text = open(folder, "r", encoding='utf-8').read()
            list_doc.append(text)
        if len(list_doc) >= minimum_num_doc:
            print(country,len(list_doc))
            LDA(country, list_doc,weights_path,list_keywords_path,stopwords_path,num_topics,num_words,num_pass,lang=lang)
        print()
