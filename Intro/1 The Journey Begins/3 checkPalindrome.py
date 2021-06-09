"""
Palindrome: A string that doesn't changed when reversed (it reads the same backward and forward).
"""


def checkPalindrome(inputString):
    
    """ (str) -> boolean
    Verifica se o inverso do parametro inputString e a mesma palavra
    """
    x = len(inputString) // 2
    
    s1 = inputString[:x]
    s2 = inputString[-x:][::-1]
    
    if s1 == s2 or x == 0:
        resultado = True
    else:
        resultado = False
    
    return resultado



# Testes
print(checkPalindrome('cooc'))          # True
print(checkPalindrome('coioioc'))       # True
print(checkPalindrome('o'))             # True
print(checkPalindrome('coo'))           # False