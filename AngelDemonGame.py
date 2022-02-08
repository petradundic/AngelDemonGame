# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 18:04:28 2022

@author: Petra Dundic
"""


def AngelDemonGame():
    
    graph= [['N','Y','N','N'],
            ['Y','N','Y','Y'],
            ['N','Y','N','N'],
            ['Y','Y','N','N']]
    
    nodes=0
    
    newGraph=[[" " for x in range(0,4)] for y in range(0,4)]
    i=0
    j=0
    
    A=3
    D=3
    
    Angel=[(0,1),(2,1),(1,3)]
    Demon=[(2,0),(0,3),(2,3)]
    
    
    
    for item in graph:
        nodes+=1


    for i in range(0,nodes):
        for j in range(0,nodes):
            
                if((i,j) in Demon and (((i,j) not in Angel)) and ((j,i) not in Angel)):
                    newGraph[i][j]='N'
                    newGraph[j][i]='N'    
                    print("demon",i,j)
                    
                elif((i,j) in Angel and (((i,j) not in Demon)) and ((j,i) not in Demon)):
                    newGraph[i][j]='Y'
                    newGraph[j][i]='Y'   
                    print("angel",i,j)
             
                
             
    for i in range(0,nodes):
        for j in range(0,nodes):        
            if(newGraph[i][j]==" "):
                newGraph[i][j]=graph[i][j]
                print("nither",i,j)

    print(newGraph)
    if(IsConnected(newGraph)==True):
        print("Winner -> Angel")
    else:
        print("Winner -> Demon")


def IsConnected(adjMat):
    temp=0
    stack=[]
    visited=[False for x in range(0,4)] 
    current=0
    
    
    
    for i in adjMat:
        stack.append(temp)
        temp+=1
   
    
    stack.reverse()
    
    n=len(stack)
    
    while(len(stack)!= 0  ):
        current = stack.pop(-1)
        
        for i in range(0, len(visited)): 
            if (adjMat[current][i] == 'Y'): 
                if(visited[i]== False):
                    visited[i] = True
                if(i==(n-1) and visited[i] == True):
                    return True
                else:
                    continue
        
        

    return False


    

def main():
    
    AngelDemonGame()
   
if __name__ == "__main__":
    main()