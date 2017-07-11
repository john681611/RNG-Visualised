import random

def rngfunc():
    value = int(random.triangular(0, 9, 1))
    return value


def iterate(x=0, y=10000):
    response = {}
    array = []
    for i in range(x, y):
        array.append(rngfunc())
    response["raw"] = array

    counts = {}
    percent = {}
    for item in array:
        counts[item] = array.count(item)
        percent[item] = str(counts[item]/((y-x)/100)) + "%"
    response["counts"] = counts
    response["percents"] = percent

    return response


def visualise():
    x = 0
    y = 10000
    response = iterate(x,y)
    print("Percentages : " + str(response["percents"]))
    print("Counts : " + str(response["counts"]))
    print("Raw : " + str(response["raw"]))
    for index, item in response["percents"].items():
        temp = int(round(float(item.strip('%'))))
        stars = ""
        for i in range(0, temp):
            stars = stars + "*"
        print(str(index) + " : " + stars + " : " + item)


if __name__ == "__main__":
    visualise()

