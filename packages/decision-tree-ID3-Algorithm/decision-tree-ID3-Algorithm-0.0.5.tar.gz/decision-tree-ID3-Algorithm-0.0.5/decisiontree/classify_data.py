from treelib import Tree
tree = Tree()
def classify(node,x_test,features,attribute=None):
    global tree 
    if node.answer!="":
        print(node.answer)
        temp = Tree()
        temp.create_node(node.answer,node.answer)
        tree.paste(attribute,temp)
        print("The tree traversal for the test instance is: ")
        tree.show()
        tree = Tree()
        return node.answer
    pos=features.index(node.attribute)
    new_tree = Tree()
    new_tree.create_node(node.attribute,node.attribute)
    if tree.root:
        tree.paste(attribute,new_tree)
    else:
        tree = new_tree
    for value, n in node.children:
        if x_test[pos]==value:
            temp = Tree()
            temp.create_node(value,value)
            tree.paste(node.attribute,temp)
            classify(n,x_test,features,value)