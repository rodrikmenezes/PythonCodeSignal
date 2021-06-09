"""
Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. 
Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. 
He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.
"""

def makeArrayConsecutive2(statues):
    
    """ (list) -> bool
    """
    
    statues.sort()
    statues_complete = list(range(statues[0], statues[-1] + 1))
    
    i = 0
    while i < len(statues_complete):
        for j in statues:
            if statues_complete[i] == j:
                statues_complete.remove(j)
        i += 1
    
    return len(statues_complete)

# Testes
print(makeArrayConsecutive2([6, 2, 3, 8]))          # 3
print(makeArrayConsecutive2([4, 13, 8, 6, 11]))     # 5