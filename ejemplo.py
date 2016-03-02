__author__ = 'dante'

def add_context(key,value):
    context = {}
    context[key] = value
    return "la llave es %s y el valor es %s , resultado final %s"%(key,value,context)

print (add_context("nombre", "vito"))

