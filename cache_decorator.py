from functools import wraps

def cache(limit):
    cache = {}
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(args, kwargs)
            index = args[0]
            # print(index, cache)
            if index in cache:
                return cache[index]

            result = func(*args, **kwargs)
            cache[index] = result
            print(cache)

            for i,arg in enumerate(args):
                print(i, arg)
                max_value = list(limit.keys())[i]  #get the limit for parameter value
                max_result = limit[max_value]      #get the limit for the resulted value
                # print(arg, limit[i])
                if index>max_value and result > max_result:
                    raise ValueError(f"Argument value exceeded for index {index}. Max value: {result}")

            return result
        return wrapper
    return decorator

# Example usage:
@cache(limit={30:10000})
def fibonacci(n):
    if n <= 0:
        return "Invalid input. Please provide a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[-1]
    


if __name__ =="__main__":
    print(fibonacci(6))
    print(fibonacci(10))
    print(fibonacci(30))
    print(fibonacci(31))
