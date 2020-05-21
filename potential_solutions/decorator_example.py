# Example from: https://www.freecodecamp.org/news/python-example/
def p_decorate(func):
   def func_wrapper(name):
       return "<p>{0}</p>".format(func(name))
   return func_wrapper

def strong_decorate(func):
    def func_wrapper(name):
        return "<strong>{0}</strong>".format(func(name))
    return func_wrapper

def div_decorate(func):
    def func_wrapper(name):
        return "<div>{0}</div>".format(func(name))
    return func_wrapper

@div_decorate
@p_decorate
@strong_decorate
def get_text(name):
   return "lorem ipsum, {0} dolor sit amet".format(name)

print (get_text("John"))


def p_decorate2(func):
   def func_wrapper(*args, **kwargs):
       return "`<p>`{0}`</p>`".format(func(*args, **kwargs))
   return func_wrapper

class Person(object):
    def __init__(self):
        self.name = "John"
        self.family = "Doe"
    @p_decorate2
    def get_fullname(self):
        return self.name+" "+self.family

my_person = Person()
print (my_person.get_fullname())