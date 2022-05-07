from unicodedata import name


def decorator(func):
    def greeting(*args,**kwargs):
        print('please register your details....')
        func(*args,**kwargs)
        print('thank you for share your details')
    return greeting


@decorator
def registration():
    name=input('enter name:')
    age=input('enter age:')
registration()
