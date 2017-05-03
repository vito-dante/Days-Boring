def makebold(my_function):
    def wrapped(*args, **kwargs):
        return "<b>"+ my_function(*args,**kwargs)+"</b>"
    return wrapped

@makebold
def hello(*args,**kwargs):
    return f"hello args:{args} kwargs:{kwargs}"

message = hello("vito","marca",name="vito")
print(message)
