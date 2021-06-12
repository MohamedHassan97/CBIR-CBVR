from elasticsearch import Elasticsearch
es = Elasticsearch()

def create_doc(index, doc: dict):
    doc={

    }
    es.index(index=index, body=doc)
