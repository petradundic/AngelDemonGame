# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 13:31:23 2022

@author: Petra Dundic
"""


def ZeroOne():
    
    
    list1=[0,3,1,2,2,3,4,4]
    list2=[3,0,2,1,2,3,4,4]
    adjMatrix=[[" " for x in range(0,len(list1))] for y in range(0,len(list1))]
    prevNum=0
    nextNum=0
   
    i=0
    j=0
    
    if(SimpleCheck(list1, list2) == True):
        prevNum=1
        g=[i for i, e in enumerate(list1) if e == prevNum]
        for item in g:
            adjMatrix[0][item]='Y'
            adjMatrix[item][0]='Y'
            
            
        z=[j for j, el in enumerate(list2) if el == prevNum]
        for item in z:
            adjMatrix[1][item]='Y'
            adjMatrix[item][1]='Y'
        
        while(prevNum<=max(list1) or prevNum<=max(list2)):
            nextNum=prevNum+1
            newG=[i for i, e in enumerate(list1) if e == nextNum]
            
            for elem1 in g:
                for elem2 in newG:
                    
                    if(DifferenceCheck(list1[elem1], list1[elem2], list2[elem1], list2[elem2])):
                        adjMatrix[elem1][elem2]='Y'
                        adjMatrix[elem2][elem1]='Y'
                    else:
                        adjMatrix[elem1][elem2]='N'
                        adjMatrix[elem2][elem1]='N'
                       
               
            for i in range(1,len(newG)):
                if(SecondDifferenceCheck(list1, list2, newG[i], newG[i-1]) == True):
                        adjMatrix[newG[i]][newG[i-1]]='Y'
                        adjMatrix[newG[i-1]][newG[i]]='Y' 
                        
                        
            prevNum=nextNum
            g=newG
            
            
        
            
        
    
    else:
        adjMatrix=[]
    
    for i in range(0,len(list1)):
        for j in range(0,len(list2)):        
            if(adjMatrix[i][j]==" "):
                adjMatrix[i][j]='N'
    
    
    for item in adjMatrix:
        print(item,"\n")
   # print(adjMatrix)
   





def SimpleCheck(list1,list2):
    
    
    if(list1[0]!=0 or list2[1]!=0):
        return False
    if(list1[1]!=list2[0]):
        return False
    if(len(list1)!=len(list2)):
        return False
    
    return True


def DifferenceCheck(num1, num2, num3, num4):
    if((num1-num2==1 or num1-num2==-1) and (num3-num4==1 or num3-num4==-1)):
        return True
    elif((num1-num2==0) or (num3-num4==0)):
        return True
    
    else:
        return False
    
    
def SecondDifferenceCheck(list1,list2,num1,num2):
    temp1=list1[num1]-list1[num2]
    temp2=list2[num1]-list2[num2]
    
    if((num2-num1==1 or num2-num1==-1) and (temp1 != temp2)):
        return True
    else:
        return False
    

def main():
    
    ZeroOne()

   
if __name__ == "__main__":
    main()