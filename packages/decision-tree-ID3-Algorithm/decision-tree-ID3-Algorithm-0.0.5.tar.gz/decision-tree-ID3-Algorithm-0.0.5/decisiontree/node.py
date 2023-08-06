class Node_ID3:
    def __init__(self,attribute):
        self.attribute=attribute
        self.children=[]
        self.answer=""
    def __str__(self):
        return "Attribute " + self.attribute + " Children " + str(self.children) + "Answer" + self.answer