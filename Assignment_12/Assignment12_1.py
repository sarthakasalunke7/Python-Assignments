# Write a program which accepts one character and checks whether it is vowel or consonant.
# Input: a
# Output: Vowel

def CheckVowel(Value):
    if(Value in ('A' , 'E' , 'I' , 'O' , 'U' , 'a' , 'e' , 'i' , 'o' , 'u')):
        return True
    else:
        return False

def main():
    Ch = input("Enter a character : ")

    Ret = CheckVowel(Ch)

    if (Ret == True):
        print("Vowel")

    else:
        print("Consonant")

if __name__ == "__main__":
    main()