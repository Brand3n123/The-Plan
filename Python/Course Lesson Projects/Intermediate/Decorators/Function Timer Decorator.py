from functools import reduce
import time

def func_decorator(function): 
    def wrapper(*args, **kwargs):
        start_time = time.time()
        function(*args, **kwargs)
        end_time = time.time()
        print(f"{function.__name__} took {end_time - start_time:.6f} seconds")
        #return function(*args, **kwargs)
    return wrapper

num_list = [1, 14, 9, 7, 2, 88]

@func_decorator
def square_num_func():
    return list(map(lambda num: num * num, num_list))

@func_decorator
def even_num_func():
    return(list(filter(lambda num: num % 2 == 0, num_list)))

@func_decorator
def product_num_func():
    return(reduce(lambda num1, num2: num1 * num2, num_list))

square_num_func()
even_num_func()
product_num_func()