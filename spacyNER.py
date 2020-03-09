from flask import Flask
from flask import request
import spacy
import re
import pandas as pd
#import time
cop = re.compile("[^a-z^A-Z^0-9.&' ]")

app = Flask(__name__)
app.config['nlp_en'] = spacy.load('en_core_web_sm')
app.config['nlp_de'] = spacy.load('de_core_news_sm')
app.config['nlp_es'] = spacy.load('es_core_news_sm')
app.config['nlp_pt'] = spacy.load('pt_core_news_sm')
app.config['nlp_fr'] = spacy.load('fr_core_news_sm')
app.config['nlp_it'] = spacy.load('it_core_news_sm')
app.config['nlp_nl'] = spacy.load('nl_core_news_sm')

with open('config/sx') as f:
    sc = list(map(lambda x: x.replace("\n",''),set(f.readlines())))

data_df = pd.read_csv("config/地点-black.csv")
loc_black = data_df["entity"].tolist()
data_df = pd.read_csv("config/组织-black.csv")
org_black = data_df["entity"].tolist()
data_df = pd.read_csv("config/人物-black.csv")
per_black = data_df["entity"].tolist()

def type_adjustment(name):
    def normallize(name):
        if len(name)<=5 and name.isupper() or (name in sc):
            return name
        else:
            return name.capitalize()

    name = name.strip()
    name_list = name.split(' ')
    name_lists = list(map(normallize, name_list))
    name = " ".join(name_lists)
    if name == "White House":
        name = "The "+name
    return  cop.sub("", name).rstrip("'").strip()

def analysis(content,nlp_name):
    nlp = app.config[nlp_name]
    entities = []
    senId = 0
    content = nlp(str(content))
    for sentence in content.sents:
        senId += 1
        sentence = nlp(str(sentence))
        for ent in sentence.ents:
            label = str(ent.label_)
            name = str(ent)
            if len(name) > 1 and len(name)<20 and name !="'s" and name != "’s" and name.isdigit()==False:
                if label == 'PERSON' and (name not in per_black):
                    label = "1-person"
                elif label == 'ORG' and (name not in org_black):
                    label = "2-organization"
                elif label == 'GPE' or label == 'LOC':
                    if (name not in loc_black):
                        label = "3-location"
                else:
                    continue
                name = type_adjustment(str(ent))
                if name == "US":
                    name = "U.S."
                if name == "White House":
                    name = "The White House"
                if len(str(entities)) < 800:
                    entities.append({
                        "entity": name,
                        "typeName": label,
                        "paraId": 1,
                        "senId": senId,
                        "startPos": int(ent.start_char),
                        "endPos": int(ent.end_char)
                    })
                else:
                    return str(entities)
    return entities

@app.route('/spacy_en', methods=['POST'])
def en_processing():
    nlp_name = 'nlp_en'
    content = request.form['content']
    entities = analysis(content,nlp_name)
    # print(entities)
    return str(entities)

@app.route('/spacy_de', methods=['POST'])
def de_processing():
    nlp_name = 'nlp_de'
    content = request.form['content']
    entities = analysis(content, nlp_name)
    return str(entities)


@app.route('/spacy_es', methods=['POST'])
def es_processing():
    nlp_name = 'nlp_es'
    content = request.form['content']
    entities = analysis(content, nlp_name)
    return str(entities)


@app.route('/spacy_pt', methods=['POST'])
def pt_processing():
    nlp_name = 'nlp_pt'
    content = request.form['content']
    entities = analysis(content, nlp_name)
    return str(entities)

@app.route('/spacy_fr', methods=['POST'])
def fr_processing():
    nlp_name = app.config['nlp_fr']
    content = request.form['content']
    entities = analysis(content, nlp_name)
    return str(entities)

@app.route('/spacy_it', methods=['POST'])
def it_processing():
    nlp_name ='nlp_it'
    content = request.form['content']
    entities = analysis(content, nlp_name)
    return str(entities)


@app.route('/spacy_nl', methods=['POST'])
def nl_processing():
    nlp_name = 'nlp_nl'
    content = request.form['content']
    entities = analysis(content, nlp_name)
    return str(entities)

@app.route('/test')
def test():
    return "It`s work."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001, threaded=False, processes=4)
    #app.run()
