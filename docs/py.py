from __future__ import print_function
from functools import reduce

def starred_expression():
    n = int(input())
    
    arr=[]
    arr=[int(x) for x in range(1,n+1,1)]
    
    print(*arr, sep='', end='\n')

def teste():
    n = int(input())
    arr = map(int, input().split())
    print(arr)
    first = max(arr)
    while max(arr) == first:
        arr.remove(max(arr))
    
    print(max(arr))

def new_lambda():
    lista = [6, 6, 6, 6, 6]
    produto = reduce(lambda x,y: x * y, lista) #retorna o produto de todos os elemento de lista
    print("lista = ", lista,"\n\nproduto = ", produto)