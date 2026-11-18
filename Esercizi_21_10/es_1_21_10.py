"""
Scrivi un decorator che esegua la funzione decorata tre volte.
"""
def my_decorator(func): #definisco il decorator
    def wrapper(*args, **kwargs): #definisco il wrapper
        for i in range(3): #definisco cosa deve fare il wrapper sulla funzione
            func(*args, **kwargs)
    return wrapper

@my_decorator #inserisco decorator
def hello_world():
    print("Hello World!")

hello_world() #eseguirà 3 volte la funzione