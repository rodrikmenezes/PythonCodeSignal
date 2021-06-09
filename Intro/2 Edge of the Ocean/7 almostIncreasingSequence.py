"""
Given a sequence of integers as an array, determine whether it is possible to obtain a 
strictly increasing sequence by removing no more than one element from the array.
"""
import time

# Medir tempo
inicio = time.time()

def almostIncreasingSequence(x):
    """ (list) -> bool
    recebe uma lista de n elementos e verifica se é
    estritamente crescente
    """
    n0 = -9999999
    for i in range(len(x)):
        n = x[i]
        if n <= n0:
            s1 = x[:i] + x[i+1:]
            s2 = x[:i-1] + x[i:]
            s3 = x[:i+1] + x[i+2:]
            if crescente(s1) or crescente(s2) or crescente(s3):
                return True
        n0 = n
    return False

    return 

def crescente(x):
    """ (list) -> bool
    recebe uma lista de 3 números e verifica se é crescente
    """
    n0 = -9999999
    for i in range(len(x)):
        n = x[i]
        if n <= n0:
            return False
        n0 = n
    return True


# Testes
print(almostIncreasingSequence([1, 3, 2]))                      # True
print(almostIncreasingSequence([1, 3, 2, 1]))                   # False
print(almostIncreasingSequence([1, 2, 1, 2]))                   # False
print(almostIncreasingSequence([10, 1, 2, 3, 4, 5]))            # True
print(almostIncreasingSequence([1, 1]))                         # True
print(almostIncreasingSequence([1, 2, 5, 3, 5]))                # True
print(almostIncreasingSequence([1, 2, 3, 4, 3, 6]))             # True
print(almostIncreasingSequence([1, 2, 3, 4, 5, 3, 5, 6]))       # False
print(almostIncreasingSequence([1, 2, 3, 4, 5, 3, 5, 6]))       # False
print(almostIncreasingSequence([1, 1, 2, 3, 4, 4]))             # False
print(almostIncreasingSequence([10, 1, 2, 3, 4, 5, 6, 1]))      # False
print(almostIncreasingSequence(list(range(5))))                 # True+
print(almostIncreasingSequence(list(range(10000))+[100,101]))   # False


# Print do tempo de execução
fim = time.time()
print('\nTEMPO = {:.4f}'.format(fim - inicio))
