def minion_game(string,name1='Stuart',name2='Kevin'):
    string=string.upper()
    n1=name1 #chooses substring starting with consonants
    p1=0        #points of Player 1
    n2=name2  #chooses substring starting with vowels
    p2=0        #points of Player 2
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
    s = input('Enter string:')
    s1=input('Name of Player 1:')
    s2=input('Name of Player 2:')
    minion_game(s,s1,s2)
