import graphviz as gf
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

G = gf.Digraph()


placesString=input("Enter the Set of Places: ")

placesList=placesString[1:-1].split(",")

print(placesList)

transitionsString=input("Enter the Set of Transitions: ")

transitionsList=transitionsString[1:-1].split(",")

print(transitionsList)

edgesString=input("enter the Set of Edges: ")

edgesList=edgesString[1:-1].split(")")

print(edgesList)

for i in range (len(edgesList)-1):
    flow = edgesList[i]
    flow=flow.replace(" ","")
    if(i==0):
        flow=flow[1:]
    else:
        flow=flow[2:]
    print(flow)
    ele1,ele2= flow.split(",")
    if(ele1[0]=="P" or ele1[0]=="p" or ele1[0]=="i" or ele1[0]=="o"):
        G.node(ele1,shape="circle")
        G.node(ele2,shape="box")
        G.edge(ele1,ele2)
    else:
        G.node(ele1,shape="box")
        G.node(ele2,shape="circle")
        G.edge(ele1, ele2,)

G.view()