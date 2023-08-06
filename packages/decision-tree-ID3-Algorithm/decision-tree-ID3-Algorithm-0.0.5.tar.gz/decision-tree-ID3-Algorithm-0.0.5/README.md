# Decision Tree algorithms
Implementation of Decision tree algorithms

## Installation 
Run the following command to install:
```python
    pip install decision-tree-ID3-Algorithm
```

## Usage 
```python 
from decisiontree.ID3Algorithm import ID3
id3_2 = ID3(dataset_train,headers_train,dataset_test,headers_test)
# dataset_train contains the training dataset with headers as headers_train
# dataset_test contains unlabled data with headers as headers_test
# all the agruments are of type list
id3_2.build_tree()
id3_2.classify()
```