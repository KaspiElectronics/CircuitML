# Introducing CircuitML
**CircuitML** is a **machine learning** library that allows you to convert machine learning models to micro-controllers and other embedded devices.
CircuitML is a fork of [micromlgen](https://github.com/CMLarduino/micromlgen).

## Install
`pip install circuitml`

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
- SEFR
- PCA


```python
from circuitml import port
from sklearn.svm import SVC
from sklearn.datasets import load_iris


if __name__ == '__main__':
    iris = load_iris()
    X = iris.data
    y = iris.target
    clf = SVC(kernel='linear').fit(X, y)
    print(port(clf))
```

You may pass a classmap to get readable class names in the ported code

```python
from circuitml import port
from sklearn.svm import SVC
from sklearn.datasets import load_iris


if __name__ == '__main__':
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

## PCA

It can export a PCA transformer.

```python
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
from circuitml import port

if __name__ == '__main__':
    X = load_iris().data
    pca = PCA(n_components=2, whiten=False).fit(X)
    
    print(port(pca))
```

## SEFR

Read the post about [SEFR](https://CMLarduino.github.io/2020/07/sefr-a-fast-linear-time-classifier-for-ultra-low-power-devices/).

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

## DecisionTreeRegressor and RandomForestRegressor

```bash
pip install circuitml>=1.1.26
```

```python
from sklearn.datasets import load_boston
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from circuitml import port


if __name__ == '__main__':
    X, y = load_boston(return_X_y=True)
    regr = DecisionTreeRegressor(max_depth=10, min_samples_leaf=5).fit(X, y)
    regr = RandomForestRegressor(n_estimators=10, max_depth=10, min_samples_leaf=5).fit(X, y)
    
    with open('RandomForestRegressor.h', 'w') as file:
        file.write(port(regr))
```

```cpp
// Arduino sketch
#include "RandomForestRegressor.h"

CML::ML::Port::RandomForestRegressor regressor;
float X[] = {...};


void setup() {
}

void loop() {
    float y_pred = regressor.predict(X);
}
```
