# RNG-Visualised
A simple Script to visualise the spread of random functions to let you mess with RNG spread

Example output
```
0 : *********** : 1111 (11.11%)
1 : ********************* : 2075 (20.75%)
2 : ****************** : 1841 (18.41%)
3 : *************** : 1533 (15.33%)
4 : ************ : 1224 (12.24%)
5 : ********** : 990 (9.9%)
6 : ******* : 698 (6.98%)
7 : **** : 392 (3.92%)
8 : * : 136 (1.36%)
```

## Types:
- Python

## Usage (python)
Modify you random function 
```
# Your random function
def rngfunc():
    value = int(random.triangular(0, 9, 1))
    return value
```
If you want change the number of iterations
```
def visualise():
    # change this to to change the amount of iterations
    x = 10000
```