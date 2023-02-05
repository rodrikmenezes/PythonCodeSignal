"""
Given two arrays a and b, check whether they are similar.
"""


def solution(a, b):
    
    for x in range(len(a)-1):
            
        if a == b:
            return True
    
        o1 = a[x:x+2]
        o2 = b[x:x+2]
        
        while o1 == o2:
            x += 1
            o1 = a[x:x+2]
            o2 = b[x:x+2]
            
        o2.reverse()
        o3 = a[x+2:len(a)]
        o4 = b[x+2:len(a)]
        
        if  o1 == o2 and o3 == o4:
            return True
        
    return False
                
    






# Testes
# print('1- ' + str(solution(a = [1,2,3], b = [1,2,3])))                  # 1- True
# print('2- ' + str(solution(a = [1,2,3], b = [2,1,3])))                  # 2- True
# print('3- ' + str(solution(a = [1,2,2], b = [2,1,1])))                  # 3- False
# print('4- ' + str(solution(a = [3,4,6,7,1], b = [3,4,7,6,1])))          # 4- True
# print('5- ' + str(solution(a = [1,1,1,1], b = [1,1,1,2])))              # 5- False
# print('6- ' + str(solution(a = [1,2,1,2], b = [2,2,1,1])))              # 6- True






