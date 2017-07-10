from random import randint


def rngfunc():
    value = randint(0, 9)
    return value


def iterate(x=0, y=10000):
    response = {}
    arry = []
    for i in range(x, y):
        arry.append(rngfunc())
    response["raw"] = arry

    counts = {}
    percent = {}
    for item in arry:
        counts[item] = arry.count(item)
        percent[item] = counts[item]/((y-x)/100)
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


if __name__ == "__main__":
    visualise()

