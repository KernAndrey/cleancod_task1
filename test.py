str = '+*-1qwer5tyuiop7'


anagram = []
for i in range (len(str)):
    n = len(str) - 1 - i
    if  str[n].isalpha():
        anagram.append(str[n])
for i in range (len(str)):
    if not str[i].isalpha():
        anagram.insert(i, str[i])
anagram = ''.join(anagram)
print(anagram)