
def new_decorator(origin_decorator):
    def wrap_func():
        print("Before decorator call function")
        origin_decorator()
        print("After decorator call function")
    
    return wrap_func

# def funct_needs_decorators():
#     print("This is the function needs decorators")
    
# call_decorator = new_decorator(funct_needs_decorators)

# call_decorator()

@new_decorator
def funct_needs_decorators():
    print("Hung Tran")
    
funct_needs_decorators()

