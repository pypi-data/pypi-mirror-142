from decisiontree.node import Node_ID3
import math
from treelib import Tree
import random
tree = Tree()
def build_tree(data,features):

        node = build_tree_rec(data,features)
        print("The decision tree for the dataset using ID3 algorithm is")
        tree.show()
        return node

def build_tree_rec(data,features,attribute=None):
        global tree
        lastcol=[row[-1] for row in data] 
        if(len(set(lastcol)))==1:
            temp = Tree()
            temp.create_node(lastcol[0],random.randint(1,100000))
            tree.paste(attribute,temp)
            node=Node_ID3("")
            node.answer=lastcol[0]
            return node
        
        n=len(data[0])-1 
        gains=[0]*n
        for col in range(n):
            gains[col]=compute_gain(data,col)
        split=gains.index(max(gains))
        new_tree = Tree()
        new_tree.create_node(features[split],features[split])
        node=Node_ID3(features[split])
        fea = features[:split]+features[split+1:]
        attr,dic=subtables(data,split,delete=False)
        for x in range(len(attr)):
            new_tree.create_node(attr[x],attr[x],parent=features[split])
        if tree.root:
            tree.paste(attribute,new_tree)
        else:
            tree = new_tree
        attr,dic=subtables(data,split,delete=True)
        for x in range(len(attr)):        
            child=build_tree_rec(dic[attr[x]],fea,attribute=attr[x])
            node.children.append((attr[x],child))
        return node

def compute_gain(data,col): 
        attr,dic = subtables(data,col,delete=False)
        
        total_size=len(data)
        entropies=[0]*len(attr)
        ratio=[0]*len(attr)
        
        total_entropy=entropy([row[-1] for row in data]) 
        for x in range(len(attr)):
            ratio[x]=len(dic[attr[x]])/(total_size*1.0)
            entropies[x]=entropy([row[-1] for row in dic[attr[x]]])
            total_entropy-=ratio[x]*entropies[x]
        return total_entropy

def subtables(data,col,delete): 
        dic={}
        coldata=[row[col] for row in data]
        attr=list(set(coldata))
        
        counts=[0]*len(attr)
        r=len(data) 
        c=len(data[0]) 
        for x in range(len(attr)):
            for y in range(r):
                if data[y][col]==attr[x]:
                    counts[x]+=1
            
        for x in range(len(attr)): 
            dic[attr[x]]=[[0 for i in range(c)] for j in range(counts[x])]
            pos=0
            for y in range(r):
                if data[y][col]==attr[x]:
                    if delete:
                        del data[y][col]
                    dic[attr[x]][pos]=data[y]
                    pos+=1
        return attr,dic

def entropy(S): 
        attr=list(set(S))
        if len(attr)==1:
            return 0
        
        counts=[0,0] 
        for i in range(2):
            counts[i]=sum([1 for x in S if attr[i]==x])/(len(S)*1.0)
        
        sums=0
        for cnt in counts:
            sums+=-1*cnt*math.log(cnt,2)
        return sums