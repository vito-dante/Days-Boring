__author__ = 'dante'

def fibonacci(numero):
    if(numero <=1):
        return 1
    else:
        return fibonacci(numero-1)+fibonacci(numero-2)

print(fibonacci(3))
#
# 01123581321
# 012345
# n-1 * n-2
#
# 5-1 + 5-2
# 4 + 3

