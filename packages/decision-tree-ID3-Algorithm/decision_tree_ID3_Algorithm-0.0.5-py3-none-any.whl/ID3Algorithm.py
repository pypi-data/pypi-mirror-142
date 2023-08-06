from buildTree import build_tree
from classify_data import classify
class ID3:
    def __init__(self,*args):
        
        self.data_train = args[0]
        self.data_test = args[2]
        self.features_train = args[1]
        self.features_test = args[3]

    def build_tree(self):
        self.node = build_tree(self.data_train,self.features_train)

    def classify(self):
        for xtest in self.data_test:
            print("The test instance:",xtest)
            print("The label for test instance:")   
            classify(self.node,xtest,self.features_test)