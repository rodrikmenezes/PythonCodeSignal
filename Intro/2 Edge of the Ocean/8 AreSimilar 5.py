"""
Given two arrays a and b, check whether they are similar.
"""
import time

inicio = time.perf_counter()

def solution(a, b):
    cont = 0
    if sorted(a) == sorted(b):
        for i in range(len(a)):
            if a[i] != b[i]:
                cont += 1
        return cont < 3
    else:
        return False


# Testes
# print('1- ' + str(solution(a = [1,2,3], b = [1,2,3])))                  # 1- True
# print('2- ' + str(solution(a = [1,2,3], b = [2,1,3])))                  # 2- True
# print('3- ' + str(solution(a = [1,2,2], b = [2,1,1])))                  # 3- False
# print('4- ' + str(solution(a = [3,6,7,1], b = [3,7,6,1])))              # 4- True
# print('5- ' + str(solution(a = [1,1,1,1], b = [1,1,1,2])))              # 5- False
# print('6- ' + str(solution(a = [1,2,1,2], b = [2,2,1,1])))              # 6- True
# print('7- ' + str(solution(a = [832, 998, 148, 570, 533, 561, 894, 147, 455, 279], b = [832, 570, 148, 998, 533, 561, 455, 147, 894, 279])))    # 6- False


fim = time.perf_counter()
print('Tempo de execução = ' + str(fim - inicio))

