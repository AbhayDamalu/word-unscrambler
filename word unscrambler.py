print("         W O R D S   U N S C R A M B L E R")
print()

file=open("english3.txt","r")
words_list=file.readlines()

def permutations(raw_str):
    from itertools import permutations
    word_list=[]
    ch_s=list(inp)
    perm=permutations(ch_s)
    for i in list(perm):
        word=""
        for j in i:
            word+=j
        if word not in word_list:
            word_list+=[word]
    return word_list

while True:
    inp=input("Enter word to unscramble:")
    while inp.isalpha()==False:
        print("Invalid Input...")
        inp=input("Enter word to unscramble:")

    possible_words_list=permutations(inp)
    print()
    print("Words Generated--")
    print("---------------")
    for word in possible_words_list:
        if word+"\n" in words_list:
            print(word)
        else:
            pass
    print()
