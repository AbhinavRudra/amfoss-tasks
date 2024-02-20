'''William, an ardent fan of FOSS, possesses a string s with a fixed length of 10. This string comprises only lowercase Latin letters. In his quest for knowledge, William desires to determine the number of indices at which his string s differs from the reference string "amfoss."
For instance, consider the string s = "amfood." In this case, there are 2 indices where the characters in the string s differ from the corresponding characters in "amfoss." These differing characters are depicted in bold.
Your mission is to aid William by calculating the count of indices where his strings deviates from the string "amfoss." However, please keep in mind that reordering the characters within the string s is not allowed.
'''

def countDifferences(s):
    reference = "amfoss"
    diff_count = 0
    for i in range(min(len(s), len(reference))):
        if s[i] != reference[i]:
            diff_count += 1
    return diff_count

diff_count = 0
n = int(input())
for i in range(n):
    s = input()
    print(countDifferences(s))