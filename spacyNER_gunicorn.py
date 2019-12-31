from flask import Flask
from flask import request
import spacy
#import time

app = Flask(__name__)
app.config['nlp_en'] = spacy.load('en_core_web_sm')
app.config['nlp_de'] = spacy.load('de_core_news_sm')
app.config['nlp_es'] = spacy.load('es_core_news_sm')
app.config['nlp_pt'] = spacy.load('pt_core_news_sm')
app.config['nlp_fr'] = spacy.load('fr_core_news_sm')
app.config['nlp_it'] = spacy.load('it_core_news_sm')
app.config['nlp_nl'] = spacy.load('nl_core_news_sm')

#nlp_en = spacy.load('en_core_web_sm')
#nlp_de = spacy.load('de_core_news_sm')
#nlp_es = spacy.load('es_core_news_sm')
#nlp_pt = spacy.load('pt_core_news_sm')
#nlp_fr = spacy.load('fr_core_news_sm')
#nlp_it = spacy.load('it_core_news_sm')
#nlp_nl = spacy.load('nl_core_news_sm')


@app.route('/spacy_en', methods=['POST'])
def en_processing():
    nlp_en = app.config['nlp_en']
    entities = []
    senId = 0
    content = request.form['content']
    content = nlp_en(str(content))
    for sentence in content.sents:
        senId += 1
        sentence = nlp_en(str(sentence))
        for ent in sentence.ents:
            label = str(ent.label_)
            name = str(ent)
            if len(name) > 1:
                if label == 'PERSON':
                    label = "1-person"
                elif label == 'ORG':
                    label = "2-organization"
                elif label == 'GPE' or label == 'LOC':
                    label = "3-location"
                else:
                    continue
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
    return str(entities)

@app.route('/spacy_de', methods=['POST'])
def de_processing():
    nlp_de = app.config['nlp_de']
    entities = []
    senId = 0
    content = request.form['content']
    content = nlp_de(str(content))
    for sentence in content.sents:
        senId += 1
        sentence = nlp_de(str(sentence))
        for ent in sentence.ents:
            label = str(ent.label_)
            name = str(ent)
            if len(name) > 1:
                if label == 'PER':
                    label = "1-person"
                elif label == 'ORG':
                    label = "2-organization"
                elif label == 'LOC':
                    label = "3-location"
                else:
                    continue
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
    return str(entities)


@app.route('/spacy_es', methods=['POST'])
def es_processing():
    nlp_es = app.config['nlp_es']
    entities = []
    senId = 0
    content = request.form['content']
    content = nlp_es(str(content))
    for sentence in content.sents:
        senId += 1
        sentence = nlp_es(str(sentence))
        for ent in sentence.ents:
            label = str(ent.label_)
            name = str(ent)
            if len(name) > 1:
                if label == 'PER':
                    label = "1-person"
                elif label == 'ORG':
                    label = "2-organization"
                elif label == 'LOC':
                    label = "3-location"
                else:
                    continue
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
    return str(entities)


@app.route('/spacy_pt', methods=['POST'])
def pt_processing():
    nlp_pt = app.config['nlp_pt']
    entities = []
    senId = 0
    content = request.form['content']
    content = nlp_pt(str(content))
    for sentence in content.sents:
        senId += 1
        sentence = nlp_pt(str(sentence))
        for ent in sentence.ents:
            label = str(ent.label_)
            name = str(ent)
            if len(name) > 1:
                if label == 'PER':
                    label = "1-person"
                elif label == 'ORG':
                    label = "2-organization"
                elif label == 'LOC':
                    label = "3-location"
                else:
                    continue
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
    return str(entities)


@app.route('/spacy_fr', methods=['POST'])
def fr_processing():
    nlp_fr = app.config['nlp_fr']
    entities = []
    senId = 0
    content = request.form['content']
    content = nlp_fr(str(content))
    for sentence in content.sents:
        senId += 1
        sentence = nlp_fr(str(sentence))
        for ent in sentence.ents:
            label = str(ent.label_)
            name = str(ent)
            if len(name) > 1:
                if label == 'PER':
                    label = "1-person"
                elif label == 'ORG':
                    label = "2-organization"
                elif label == 'LOC':
                    label = "3-location"
                else:
                    continue
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
    return str(entities)


@app.route('/spacy_it', methods=['POST'])
def it_processing():
    nlp_it = app.config['nlp_it']
    entities = []
    senId = 0
    content = request.form['content']
    content = nlp_it(str(content))
    for sentence in content.sents:
        senId += 1
        sentence = nlp_it(str(sentence))
        for ent in sentence.ents:
            label = str(ent.label_)
            name = str(ent)
            if len(name) > 1:
                if label == 'PER':
                    label = "1-person"
                elif label == 'ORG':
                    label = "2-organization"
                elif label == 'LOC':
                    label = "3-location"
                else:
                    continue
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
    return str(entities)


@app.route('/spacy_nl', methods=['POST'])
def nl_processing():
    nlp_nl = app.config['nlp_nl']
    entities = []
    senId = 0
    content = request.form['content']
    content = nlp_nl(str(content))
    for sentence in content.sents:
        senId += 1
        sentence = nlp_nl(str(sentence))
        for ent in sentence.ents:
            label = str(ent.label_)
            name = str(ent)
            if len(name) > 1:
                if label == 'PER':
                    label = "1-person"
                elif label == 'ORG':
                    label = "2-organization"
                elif label == 'LOC':
                    label = "3-location"
                else:
                    continue
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
    return str(entities)

@app.route('/test')
def test():
    return "It`s work."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001, threaded=False, processes=4)
    #app.run()
