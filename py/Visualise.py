import random

# Your random function
def rngfunc():
    value = int(random.triangular(0, 9, 1))
    return value


def iterate(x=10000):
    response = {}
    array = []
    for i in range(0, x):
        array.append(rngfunc())
    response["raw"] = array

    counts = {}
    percent = {}
    for item in array:
        counts[item] = array.count(item)
        percent[item] = str(counts[item]/(x/100)) + "%"
    response["counts"] = counts
    response["percents"] = percent

    return response


def visualise():
    # change this to to change the amount of iterations
    x = 10000
    response = iterate(x)
    for index, item in response["percents"].items():
        temp = int(round(float(item.strip('%'))))
        stars = ""
        for i in range(0, temp):
            stars = stars + "*"
        print(str(index) + " : " + stars + " : " + str(response["counts"][index]) + " (" + item + ")")


if __name__ == "__main__":
    visualise()

