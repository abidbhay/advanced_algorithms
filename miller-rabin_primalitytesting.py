'''
##Fast/Modular Exponentiation Package
def expo(a,n,m):
    if n==0:
        return 1%m
    if n==1:
        return a % m
    ret= expo(a,n//2,m)
    ret= (ret *ret) %m
    if n%2==1:
        ret=(ret*a) %m
    return ret
'''
import random
import primalitytest 


def Witness(a,n):
    t=0
    u=n-1
    while u%2==0:
        u=u//2
        t+=1
    x=primalitytest.expo(a,u,n)
    for i in range(t):
 
        y=(x*x)%n
        if y==1 and x==n-1 and x==1 :
                return True
        x=y
    if x!=1:
        return True
    return False

def Miller_Rabin_Test(n,s):
    for j in range(s):
        a=random.randint(1,n-1)
        if Witness(a,n):
            return "Composite with witness: "+str(a)
    return "Prime"
    
n=input("Enter number for Primality Test: ")
a= input( "Enter number of trails: ")
x=Miller_Rabin_Test(int(a),int(n))
print(x)