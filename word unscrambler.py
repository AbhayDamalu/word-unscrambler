print("         W O R D S   U N S C R A M B L E R")
print()

file=open("english3.txt","r")
words_list=file.readlines()

def permutations(raw_str):
    from itertools import permutations
    word_list=[]
    ch_s=list(raw_str)
    perm=permutations(ch_s)
    for i in list(perm):
        word=""
        for j in i:
            word+=j
        if word not in word_list:
            word_list+=[word]
    return word_list

while True:
    count=0
    inp=input("Enter word to unscramble:")
    while inp.isalpha()==False:
        print("Invalid Input...")
        inp=input("Enter word to unscramble:")

    possible_words_list=permutations(inp.lower())
    print()
    print("Words Generated--")
    print("---------------")
    for word in words_list:
        if word[:-1] in possible_words_list:
            count+=1
            print(word[:-1])
    if count==0:
        print("No word possible...")
    print()
