from CBVR import *
from elasticsearch import Elasticsearch
import pprint as pp
from os import listdir
from os.path import isfile, join
from layout import *

es = Elasticsearch()


def delete_index(index):
    # used to delete an index
    es.indices.delete(index=index, ignore=[400, 404])


def get_indices():
    # used to retrieve all indices in elasticsearch cluster
    indices = es.indices.get_alias().keys()
    index_0 = list(indices)
    index_1 = []
    for i in range(len(index_0)):
        if index_0[i][0] != '.':
            index_1.append(index_0[i])
    print(index_1)


def get_docs(index, field: str = None):
    # used to retrieve docs, if field is set will be retrieve and saved in images and pca_features
    # field values (features,tags, not set) base is not supported yet
    # _source_includes="name"
    if field:
        results = es.search(index=index, _source_includes=field, size=9999)['hits']['hits']
        return results
    else:
        results = es.search(index=index, size=9999)['hits']['hits']
        return results
    # print(results)


def delete_all_docs(index):
    # delete all docs in a certain index
    es.delete_by_query(index=index, body={"query": {"match_all": {}}})

# Video Part
def get_files(folder_path):
    only_files = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
    for i in range(len(only_files)):
        only_files[i] = "/home/bondok/cbv/" + only_files[i]
    return only_files


# video_list contain video pathes


video_list = get_files("/home/bondok/cbv")
# print(video_list)

def input_docs_video(index: str, video_path):
    for i in range(len(video_path)):
        key_frames = keyframe(video_list[i], 0.3)
        es.index(index=index, body={"keyframes": key_frames}, id=video_list[i])


def get_output(key_frame_ls,query_video_path):
    ls=[]
    for i in key_frame_ls:
        ls.append((i["_id"] , video_distance(np.array(i["_source"]["keyframes"]),np.array(keyframe(query_video_path, 0.3)) , threshold=0.5)))
    for i in ls:
        if i[1] >= 0.7:
            return i[0]


# input_docs_video("cbv",video_list)
results = get_docs("cbv")
print(get_output(results, "/home/bondok/part.mp4"))

# Image part

image_list =
