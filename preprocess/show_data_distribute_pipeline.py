
class Pipeline:
    def __init__(self, func):
        self.func = func

    def __ror__(self, other):
        return self.func(other)

@Pipeline
def pre(number):
    return number+1

@Pipeline
def injectData(number):
    return number+2

@Pipeline
def validateData(number):
    return number+3

number = 1
# unix
# validateData(injectData(pre(number)))
result = number \
         | pre \
         | injectData\
         | validateData

result = (((number) | pre) | injectData) | validateData



print(result)
