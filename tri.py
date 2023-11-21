from numpy import *
from random import*
t1=array([str]*50)
t2=array([int]*50)
t3=array([int]*50)
def saisir():
    global n
    n=int(input('le nombre de partisipon='))
    while not(2<=n<=50):
        n = int(input('le nombre de partisipon='))
def remplir_T(t1,t2,t3,n):
    for i in range (n):
        t1[i]=input('le nom de partisipeur=')
        while not(verif_ch(t1[i])==True and 3<=len(t1[i])):
            t1[i] = input('le nom de partisipeur=')
        t2[i]=int(input('son scor='))
        while not (0<=t2[i]<=100):
            t2[i] = int(input('son scor='))
        t3[i]=identifier(t1[i],t2[i])
def identifier(t1,t2):
    s=t2
    for i in range(len(t1)):
        s=s+ord(t1[i])
    return s
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
def tri(t1,t2,t3,n):
    for j in range(n):
        for i in range(j,n):
            if t2[j]< t2[i]:
                aux=t2[j]
                t2[j]=t2[i]
                t2[i]=aux
                aux1=t1[j]
                t1[j]=t1[i]
                t1[i]=aux1
                aux2=t3[j]
                t3[j]=t3[i]
                t3[i]=aux2
#"""rod belik ta3mel zok omha ib3athni nayek"""
    return t1,t2,t3
#"""____5ater il fonction traja3lik resulta bark_________"""
def afficher(t1,t2,t3,n,file):
    for i in range(n):    
        file.write(str(i+1)+' place pour '+str(t1[i])+" de l'id: "+str(t3[i])+" avec un score: "+str(t2[i])+ '\n')
    file.close() 
saisir()
remplir_T(t1,t2,t3,n)
tri(t1,t2,t3,n)
file=open('test', 'w')   
afficher(t1,t2,t3,n,file)