# CircuitML
**CircuitML** is a **machine learning** library that allows you to convert machine learning models to micro-controllers and other embedded devices.

## Install
```
pip install circuitml
```

## Supported Models
CircuitML can be used to convert the following machine learning models:

- Linear Regression
- Logistic Regression
- Decision Tree
- GaussianNB
- Support Vector Machines (SVC and OneClassSVM)
- Relevant Vector Machines (from `skbayes.rvm_ard_models` package)
- Random Forest
- GaussianNB
- PCA
- [SEFR](https://arxiv.org/abs/2006.04620)


## Usage

### Basic Usage
```python
from circuitml import port
from sklearn.svm import SVC
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data
y = iris.target
clf = SVC(kernel='linear').fit(X, y)
print(port(clf))
```

You can pass classmap to `port` function to map class names to integers :
```python
from circuitml import port
from sklearn.svm import SVC
from sklearn.datasets import load_iris


iris = load_iris()
X = iris.data
y = iris.target
clf = SVC(kernel='linear').fit(X, y)
print(port(clf, classmap={
    0: 'setosa',
    1: 'virginica',
    2: 'versicolor'
}))
```

### PCA
```python
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
from circuitml import port

X = load_iris().data
pca = PCA(n_components=2, whiten=False).fit(X)
    
print(port(pca))
```

### [SEFR](https://arxiv.org/abs/2006.04620)

```shell script
pip install sefr
```

```python
from sefr import SEFR
from circuitml import port

clf = SEFR()
clf.fit(X, y)
print(port(clf))
```

### DecisionTree and RandomForest
```python
from sklearn.datasets import load_boston,load_iris
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from circuitml import port

X, y = load_boston(return_X_y=True)
# regr = DecisionTreeRegressor(max_depth=10, min_samples_leaf=5).fit(X, y)
regr = RandomForestRegressor(n_estimators=10, max_depth=10, min_samples_leaf=5).fit(X, y)
    
with open('RandomForestRegressor.h', 'w') as file:
    file.write(port(regr))
    
X,y = load_iris(return_X_y=True)
# clf = DecisionTreeClassifier(max_depth=10, min_samples_leaf=5).fit(X, y)
clf = RandomForestClassifier(n_estimators=10, max_depth=10, min_samples_leaf=5).fit(X, y)

with open('RandomForestClassifier.h', 'w') as file:
    file.write(port(clf))
```

### Use exported model in C++
```cpp
// Arduino sketch
#include "RandomForestRegressor.h"

ML::Port::RandomForestRegressor regressor;
float X[] = {...};

void setup() {
    ...
}

void loop() {
    float y_pred = regressor.predict(X);
}
```
