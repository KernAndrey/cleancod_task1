import re


def anagrams_exept_digits():
    strings = str(input())
    string = strings.split()
    anagrams_list = []
    for j in range(len(string)):
        str1 = string[j]
        anagram = []
        for i in range(len(str1)):
            n = len(str1) - 1 - i
            if str1[n].isalpha():
                anagram.append(str1[n])
        for i in range(len(str1)):
            if not str1[i].isalpha():
                anagram.insert(i, str1[i])
        anagram = ''.join(anagram)
        anagrams_list.append(anagram)
    if __name__ == '__main__':
        print(*anagrams_list)
