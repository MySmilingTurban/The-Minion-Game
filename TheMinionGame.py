def minion_game(string):
    n1='Stuart' #chooses substring starting with consonants
    p1=0        #points of Stuart
    n2='Kevin'  #chooses substring starting with vowels
    p2=0        #points of Kevin
    v=['A','E','I','O','U']
#Combinations of each substring's occurence = len(string) - (index of substring)
    for z in range(len(string)):
        if string[z] in v:      #substring starting with a vowel
            p2+=len(string)-z
        else:                   #substring starting with a consonant
            p1+=len(string)-z 
#Comparison of Scores for Result
    if p1>p2:
        print(n1,p1,sep=' ')    #Stuart Wins
    elif p1<p2:
        print(n2,p2,sep=' ')    #Kevin Wins
    else:
        print('Draw')
    
if __name__ == '__main__':
    s = input()
    minion_game(s)
