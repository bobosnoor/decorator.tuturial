#decorating sum numbers test :-
def Decorating(func):
    def nested(*n):
        for number in n:
            if number < 0:
                print("be aware one number is less than zero")
        func(*n)
    return nested
@Decorating
def sum_all(*n):
    print(sum(n))
sum_all(6,9,7,4,9,0,7,-3,-4)

# SPEED TEST :-

from time import time
def speedTime(func):
    def warpper():
        start = time()
        func()
        end = time()
        print(f"function time is: {end - start}")
    return warpper
@speedTime
def bigLog():
    for number in range(1, 100):
        if number % 2 == 0 :
            print(number)
bigLog()
