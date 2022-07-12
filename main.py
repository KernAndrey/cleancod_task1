import re


def anagrams_exept_digits():
    string = str(input())
    string = string.split()
    anagrams_list = []
    for j in range(len(string)):
        str = string[j]
        anagram = []
        for i in range(len(str)):
            n = len(str) - 1 - i
            if str[n].isalpha():
                anagram.append(str[n])
        for i in range(len(str)):
            if not str[i].isalpha():
                anagram.insert(i, str[i])
        anagram = ''.join(anagram)
        anagrams_list.append(anagram)
    print(*anagrams_list)
