from DB_video import *
from histogram_v2 import *
from mean_color_multimedia import mean_color, similarity_mean_color
from layout import *
import pprint as pp

image_list = get_files("/home/bondok/Downloads/archive/dataset/")



def input_docs_image(index: str, image_path: list):
    for i in range(len(image_path)):
        es.index(index=index,
                 body={"mean_color": mean_color(image_path[i]), "layout": mean_color_layout(image_path[i]),"histogram": histogram_calc(image_path[i])},
                 id=image_list[i])

def data_base():
    data = []
    for i in range(800):
        querybody={
        "query": {
            "terms": {
                "_id": ["/home/bondok/Downloads/archive/dataset/" + str(200+i) + ".jpg"]
            }
        }
        }
        data.append(es.search(index="cbi",body=querybody, size=900)["hits"]["hits"])

    return data


# delete_index("cbi")
# input_docs_image("cbi", image_list)
# get_docs("cbi")


def get_mean_color(query_image, data):
    result_temp = []
    for i in range(len(data)):
        result_temp.append([data[i][0]["_source"]["mean_color"], data[i][0]["_id"]])
        data[i] = data[i][0]["_source"]["mean_color"]

    # pp.pprint(result)
    res = similarity_mean_color(query_image, data)
    for i in range(len(res)):
        res[i] = result_temp[i][1]
    print(res)
    return res


def get_histogram(query_image, data):
    result_temp = []
    for i in range(len(data)):
        result_temp.append([data[i][0]["_source"]["histogram"], data[i][0]["_id"]])
        data[i] = np.array(data[i][0]["_source"]["histogram"])
    # pp.pprint(result)
    temp = compare(800, histogram_calc(query_image), data)
    res = retrival(temp, 5, 0, 800)
    for i in range(len(res)):
        res[i] = result_temp[res[i]][1]
    print(res)
    return res

images_1 = get_mean_color("/home/bondok/Downloads/archive/dataset/201.jpg", data_base())
images_2 = get_histogram("/home/bondok/Downloads/archive/dataset/201.jpg", data_base())

def get_layout(query_image, data):
    result_temp = []
    image = []
    for i in range(len(data)):
        result_temp.append([data[i][0]["_source"]["layout"], data[i][0]["_id"]])
        data[i] = data[i][0]["_source"]["layout"]
    # pp.pprint(result)
    res = mean_color_layout_similarity(mean_color_layout(query_image), data)
    for i in range(len(res)):
        res[i] = result_temp[i][1]
    print(res)





images_3 = get_layout("/home/bondok/Downloads/archive/dataset/201.jpg", data_base())