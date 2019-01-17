'''
Provides common supporting modules to all programs. 

'''
import time


def measureTime(func):
    """
    This function measures the time taken by function to run.
    This function takes function as an argument. Execute that function and calculates its
    executing time
    :param func : function which has to be executed
    :return: function as a variable
    """

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + " took " + str((end - start) * 1000) + " milli seconds")
        return result

    return wrapper
