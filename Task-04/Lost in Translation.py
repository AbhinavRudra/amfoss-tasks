'''
In the vast virtual world of an online game, our enthusiastic player, Alex, has just discovered the joy of chatting with fellow gamers in a virtual chat room. Eager to make new friends, Alex decides to greet everyone with a friendly "hello." However, Alex's typing skills are still a work in progress, and sometimes he makes mistakes while typing the word "hello."
Alex types a string of characters represented by s. The ultimate question is whether Alex successfully managed to say "hello" if some letters can be deleted from the typed word, resulting in the actual word "hi." For instance, if Alex types "ahhellllloou," it will be considered that he said "hello." On the other hand, if Alex types "hlelo” it will be considered that he didn't manage to say "hello" correctly.
Your task is to determine whether Alex succeeded in saying "hello" with the given string s. You need to check if some letters can be deleted from the typed word to yield the exact word "hello." If such a transformation is possible, then Alex managed to say "hello"; otherwise, he might have been misunderstood, and he didn't successfully convey his friendly greeting.
'''
def HelloCheck(s):
    word = "hello"
    i = 0
    
    for char in s:
        char = char.lower()
        if char == word[i]:
            i += 1
        if i == len(word):
            return True
    else:    
        return False

s = input("")
if HelloCheck(s):
    print("YES")
else:
    print("NO")