import random


def rng_function():
    # Your random function
    value = int(random.triangular(0, 9, 1))
    return value


def iterate(x=10000):
    response = {"raw": [], "counts": {}, "percents": {}}
    for i in range(0, x):
        rng = rng_function()
        response["raw"].append(rng)
        response["counts"][rng] = response["raw"].count(rng)
        response["percents"][rng] = str(response["counts"][rng] / (x / 100)) + "%"
    return response


def visualise():
    # change this to to change the amount of iterations
    x = 10000
    response = iterate(x)
    for index, item in response["percents"].items():
        stars = "*" * round(float(item.strip('%')))
        print(str(index) + " : " + stars + " : " + str(response["counts"][index]) + " (" + item + ")")


if __name__ == "__main__":
    visualise()

