#les bibliotheque
from numpy import *
"""------------------------------------------------------------------------------"""
t1=array([str]*50)#tableau des noms il contient maximent 50 case
t2=array([int]*50)#tableau des score il contient maximent 50 case
t3=array([int]*50)#tableau des id il contient maximent 50 case
"""------------------------------------------------------------------------------"""
#saisir les nombre de case dans les tableau
def saisir():
    global n
    n=int(input('le nombre de partisipon='))
    while not(2<=n<=50):
        n = int(input('le nombre de partisipon='))
"""------------------------------------------------------------------------------"""
#remplir les tableau par le nom,le score et l'id du participent
def remplir_T(t1,t2,t3,n):
    for i in range (n):
        t1[i]=input('le nom de partisipeur=')
        while not(verif_ch(t1[i])==True and 3<=len(t1[i])):
            t1[i] = input('le nom de partisipeur=')
        t2[i]=int(input('son scor='))
        while not (0<=t2[i]<=100):
            t2[i] = int(input('son scor='))
        t3[i]=identifier(t1[i],t2[i])
"""------------------------------------------------------------------------------"""
#l'id de chaque participent c'est la somme de son score avec les code acqui de chaque letre de sont nom
def identifier(A, B):
    s=B
    for i in range(len(A)):
        s=s+ord(A[i])
    return s
"""------------------------------------------------------------------------------"""
#tester le nom du participent ==> il faux contin uniquement des letre 
def verif_ch(t):
    aux=True
    i=0
    while not(aux==True or i>len(t)):
        ch=t[i]
        if 'A'<=ch[i].upper()<='Z':
            i+=1
        else:
            aux=False
    return aux
"""------------------------------------------------------------------------------"""
#trier les tableau en teste chaque score par tout les score du tableau 
def tri(t1,t2,t3,n):
    for j in range(n):#le score en va le compare (on pose que cet score est le plux grond dans le tableau== max  )
        for i in range(j,n):# les comparesent
            if t2[j]< t2[i]:# si on trouve un score plus grond du max
                aux=t2[j]    #
                t2[j]=t2[i]  #chenger les places dans le tableau du score
                t2[i]=aux    #
                
                aux1=t1[j]   #
                t1[j]=t1[i]  #chenger les places dans le tableau du nom
                t1[i]=aux1   #
                
                aux2=t3[j]   #
                t3[j]=t3[i]  #chenger les places dans le tableau du score
                t3[i]=aux2   #
    return t1,t2,t3
"""------------------------------------------------------------------------------"""
#afficher les resultas dans un file.txt
def afficher(t1,t2,t3,n,file):
    for i in range(n):    
        file.write(str(i+1)+' place pour '+str(t1[i])+" de l'id: "+str(t3[i])+" avec un score: "+str(t2[i])+ '\n')
    file.close()
"""------------------------------------------------------------------------------"""
#en appelle les fonction
saisir()
remplir_T(t1,t2,t3,n)
tri(t1,t2,t3,n)
file=open('test', 'w') #ouvrir le file.txt pour l'ecrir     
afficher(t1,t2,t3,n,file)
