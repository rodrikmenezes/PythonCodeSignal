"""
Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, 
the second - from the year 101 up to and including the year 200, etc.

Examples:

For year = 1905, the output should be
centuryFromYear(year) = 20;

For year = 1700, the output should be
centuryFromYear(year) = 17.
"""

def centuryFromYear(year):
    if year < 100:
        seculo = 1
    elif year % 100 != 0:
        seculo = year // 100 + 1
    else:
        seculo = year // 100 
    return seculo
    
    
# Testes
print(centuryFromYear(100))    # 2
print(centuryFromYear(56))     # 1
print(centuryFromYear(1905))   # 20
print(centuryFromYear(1700))   # 17