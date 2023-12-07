#!/usr/bin/python3

# the most straight forward method, works but time limit in big inputs: 
# def is_vowel(c) -> bool:
#     vowels = "aeuioAEUIO"
#     if c in vowels:
#         return True
#     return False


# def create_substring(charList: list, ln: int) -> list:
#     substring = [charList[i: i + ln] for i in range(0, len(charList))]
#     return substring

# def num_of_occurences(substring: str, main_string: str) -> int:
#     count: int = 0
#     start_index: int = 0
#     while (start_index < len(main_string)):
#         index = main_string.find(substring, start_index)

#         if (index == -1):
#             return count
        
#         count += 1
#         start_index = index + 1

#     return count

# def check_substring(totalSubs: list, string: str) -> None:
#     scoreMap = {"Stuart": 0,
#                 "Kevin": 0
#     }

#     for sub in totalSubs:
#         newStr = ''.join(sub)
#         if newStr in string:
#             if is_vowel(sub[0]) == True:
#                 scoreMap["Kevin"] += num_of_occurences(newStr, string)
#             else:
#                 scoreMap["Stuart"] += num_of_occurences(newStr, string)

#     if (is_vowel(string[0]) == True):
#         scoreMap["Kevin"] += 1
#     else:
#         scoreMap["Stuart"] += 1

#     if (scoreMap["Kevin"] > scoreMap["Stuart"]):
#         print("Kevin", scoreMap["Kevin"])
#     elif (scoreMap["Kevin"] < scoreMap["Stuart"]):
#         print("Stuart", scoreMap["Stuart"])
#     elif (scoreMap["Kevin"] == scoreMap["Stuart"]):
#         print("Draw")

# def minion_game(string: str) -> None:
#     totalSubs = []
#     charList = list(string)
    
#     for i in range(1, len(charList)):
#         newSub = tuple(create_substring(charList, i))
#         for ls in newSub:
#             if ls not in totalSubs:
#                 totalSubs.append(ls)
    
#     check_substring(totalSubs, string)


# second method (genius and optimized)
def minion_game(string: str) -> None:
    kCount = 0
    sCount = 0
    vowels = "aeuioAEUIO"

    for i in range(0, len(string)):
        if string[i] in vowels:
            kCount += (len(string) - i)
        else:
            sCount += (len(string) - i)
    
    if (kCount > sCount):
        print("Kevin", kCount)
    elif (kCount < sCount):
        print("Stuart", sCount)
    elif (kCount == sCount):
        print("Draw")

if __name__ == '__main__':
    myStr = input()
    minion_game(myStr)
