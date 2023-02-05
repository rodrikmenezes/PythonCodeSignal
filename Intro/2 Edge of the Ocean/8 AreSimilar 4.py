"""
Given two arrays a and b, check whether they are similar.
"""
import time

nit = time.perf_counter()

def solution(a, b):
    
    a = sorted(a); b = sorted(b)

    for i in range(len(a)):
        if a[i] == b[i]:
            continue
        else:
            a[i], a[i-1] = a[i-1], a[i]
            if a == b:
                return True
            else:
                return False
    return True
    


# Testes
# print('1- ' + str(solution(a = [1,2,3], b = [1,2,3])))                  # 1- True
# print('2- ' + str(solution(a = [1,2,3], b = [2,1,3])))                  # 2- True
# print('3- ' + str(solution(a = [1,2,2], b = [2,1,1])))                  # 3- False
# print('4- ' + str(solution(a = [3,6,7,1], b = [3,7,6,1])))              # 4- True
# print('5- ' + str(solution(a = [1,1,1,1], b = [1,1,1,2])))              # 5- False
# print('6- ' + str(solution(a = [1,2,1,2], b = [2,2,1,1])))              # 6- True


fim = time.perf_counter()
print('Tempo de execução = ' + str(fim - nit))

