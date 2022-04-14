# Question 1 Build (m+1)*26 transition table

def DFA_MAKER(P,alph):
    states=len(P)+1
    dfa= [[0 for i in range(len(alph))] for j in range(states)]
    q=0
    for i in range(len(P)+1):
        for j in range(len(alph)):
            if i<len(P) and P[i]==alph[j]:
                q+=1
                dfa[i][j]=q
            else:
                curr=str(P[:i])+alph[j]
                dfa[i][j]=lps(curr)
    return dfa



#Question 2 Feed strings Ti into the Automaton

def Fin_Automaton_Matcher(T,P,alph):
    dfa=DFA_MAKER(P, alph)
    j=1
    for Ti in T:
        n=len(Ti)
        current_state, found_count=0, 0
        
        for i in range(n):
            current_state=dfa[current_state][ord(Ti[i])-ord("a")]
            if current_state==len(P):
                #print("Pattern occurs with shift", i-len(P)+1)
                found_count+=1
        if found_count==0:
             print("Pattern  not  found  in  T"+str(j))
        else:
            print("Pattern found " + str(found_count) + " times in T"+str(j))
        j+=1

                
def lps(P):
    m=len(P)
    pi=[0]*m
    pi[0]=0
    k=0
    for q in range(1,m):
        while k>0 and P[k]!=P[q]:
            k=pi[k-1]
        if P[k]==P[q]:
            k+=1
        pi[q]=k
        
    return pi[-1]  




###### TESTER ########

T=["efgrkhfndln", "gjshlbufhefg", "dhswhefgsdkj","erhbili"]
P= "efg"





alph=["a","b","c","d","e","f",        # ACCEPTABLE ALPHABET LIBRARY FOR TEXTS
      "g","h","i","j",'k',"l","m",
      "n","o","p","q","r","s","t",
      "u","v","w","x","y","z"]      


Fin_Automaton_Matcher(T,P,alph)
















