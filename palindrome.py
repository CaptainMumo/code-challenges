import string

def palindrome(word):
    alphabet = string.ascii_lowercase
    numbers = string.digits

    for x in word:
        if x not in alphabet and x not in numbers:
            word = word.lower().replace(x,"")
            
    if len(word) > 0:
        return word == word[::-1]
    else:
        return "Please enter a word or phrase"


if __name__=="__main__":
    user_last_5_entries = []
    
    while True:
        word = input("\nEnter a word or phrase to find out if it is a palindrome\nOr press [Ctrl + C] to quit : ")
        
        print()
        print(palindrome(word))
        print()

        if len(user_last_5_entries) < 5:
            user_last_5_entries.append(word)#+" : "+str(palindrome(word)))
        else:
            user_last_5_entries.pop(0)
            user_last_5_entries.append(word)#+" : "+str(palindrome(word)))
        print(user_last_5_entries)
