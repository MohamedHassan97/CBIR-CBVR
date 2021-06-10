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
    return es.search(index="cbi", size=900)["hits"]["hits"]


# delete_index("cbi")
# input_docs_image("cbi", image_list)
# get_docs("cbi")

data = data_base()

def get_mean_color(query_image, data):
    result_temp = []
    for i in range(len(data)):
        result_temp.append([data[i]["_source"]["mean_color"], data[i]["_id"]])
        data[i] = data[i]["_source"]["mean_color"]

    # pp.pprint(result)
    res = similarity_mean_color(query_image, data)
    for i in range(len(res)):
        res[i] = result_temp[i][1]
    # print(res)
    return res


def get_histogram(query_image):
    result_temp = []
    for i in range(len(data)):
        result_temp.append([data[i]["_source"]["histogram"], data[i]["_id"]])
        data[i] = np.array(data[i]["_source"]["histogram"])

    # pp.pprint(result)
    x = histogram_calc(query_image)
    print(x)
    temp = compare(800,x , data)
    res = retrival(temp,5,200,1000)
    for i in range(len(res)):
        res[i] = "/home/bondok/Downloads/archive/dataset/" + str(res[i]) + ".jpg"
    print(res)
    return res

# images_1 = get_mean_color("/home/bondok/Downloads/archive/dataset/200.jpg", data)
get_histogram("/home/bondok/Downloads/archive/dataset/200.jpg")

def get_layout(query_image, data):
    result_temp = []
    image = []
    for i in range(len(data)):
        result_temp.append([data[i]["_source"]["layout"], data[i]["_id"]])
        data[i] = data[i]["_source"]["layout"]

    # pp.pprint(result)
    res = mean_color_layout_similarity(mean_color_layout(query_image), data)
    for i in range(len(res)):
        res[i] = result_temp[i][1]
    for i in range(5):
        image.append(cv2.imread(res[i]))

    # cv2.imshow("a",image[0])
    # cv2.imshow("b",image[1])
    # cv2.imshow("c",image[2])
    # cv2.imshow("d",image[3])
    # cv2.imshow("e",image[4])
    # cv2.waitKey(0)



# images_2 = get_layout("/home/bondok/Downloads/archive/dataset/200.jpg", data)