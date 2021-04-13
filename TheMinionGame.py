def minion_game(string,name1='Stuart',name2='Kevin'):
    n1=name1 #chooses substring starting with consonants
    p1=0        #points of Stuart
    n2=name2  #chooses substring starting with vowels
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
        print(n1,'Wins, scoring',p1,sep=' ')   
    elif p1<p2:
        print(n2,'Wins, scoring',p2,sep=' ')    
    else:
        print('Draw')
    
if __name__ == '__main__':
    s = input()
    s1=input()
    s2=input()
    minion_game(s,s1,s2)
