from distutils.core import setup


setup(
  name = 'circuitml',
  packages = ['circuitml'],
  version = '1.1.27',
  license='MIT',
  description = 'Generate C code for microcontrollers from Python\'s sklearn classifiers',
  author = 'Simone Salerno',
  author_email = 'kaspielectronics@pm.me',
  url = 'https://github.com/KaspiElectronics/CircuitML/',
  download_url = 'https://github.com/KaspiElectronics/CircuitML//blob/master/dist/micromlgen-1.1.27.tar.gz?raw=true',
  keywords = [
    'ML',
    'microcontrollers',
    'sklearn',
    'machine learning'
  ],
  install_requires=[
    'jinja2',
  ],
  package_data={
    'circuitml': ['templates/pca', 'templates/linearregression', 'templates/wifiindoorpositioning', 'templates/vote.jinja', 'templates/dot.jinja', 'templates/gaussiannb', 'templates/rvm', 'templates/xgboost', 'templates/decisiontree', 'templates/randomforest', 'templates/__init__.py', 'templates/__pycache__', 'templates/_skeleton.jinja', 'templates/sefr', 'templates/svm', 'templates/logisticregression', 'templates/principalfft', 'templates/classmap.jinja', 'templates/trainset.jinja', 'templates/testset.jinja', 'templates/pca/__init__.py', 'templates/pca/pca.jinja', 'templates/linearregression/__init__.py', 'templates/linearregression/linearregression.jinja', 'templates/wifiindoorpositioning/__init__.py', 'templates/wifiindoorpositioning/wifiindoorpositioning.jinja', 'templates/gaussiannb/vote.jinja', 'templates/gaussiannb/gaussiannb.jinja', 'templates/gaussiannb/__init__.py', 'templates/rvm/__init__.py', 'templates/rvm/rvm.jinja', 'templates/xgboost/tree.jinja', 'templates/xgboost/__init__.py', 'templates/xgboost/xgboost.jinja', 'templates/decisiontree/tree_regressor.jinja', 'templates/decisiontree/tree.jinja', 'templates/decisiontree/decisiontree.jinja', 'templates/decisiontree/__init__.py', 'templates/decisiontree/decisiontree_regressor.jinja', 'templates/randomforest/randomforest_regressor.jinja', 'templates/randomforest/randomforest.jinja', 'templates/randomforest/tree_regressor.jinja', 'templates/randomforest/tree.jinja', 'templates/randomforest/__init__.py', 'templates/__pycache__/__init__.cpython-37.pyc', 'templates/sefr/sefr.jinja', 'templates/sefr/dot.jinja', 'templates/sefr/__init__.py', 'templates/svm/__init__.py', 'templates/svm/computations', 'templates/svm/svm.jinja', 'templates/svm/kernel', 'templates/svm/computations/class.jinja', 'templates/svm/computations/decisions.jinja', 'templates/svm/computations/votes.jinja', 'templates/svm/computations/kernel', 'templates/svm/computations/kernel/attiny.jinja', 'templates/svm/computations/kernel/arduino.jinja', 'templates/svm/kernel/attiny.jinja', 'templates/svm/kernel/arduino.jinja', 'templates/svm/kernel/kernel.jinja', 'templates/logisticregression/__init__.py', 'templates/logisticregression/vote.arduino.jinja', 'templates/logisticregression/logisticregression.jinja', 'templates/logisticregression/vote.attiny.jinja', 'templates/principalfft/lut.jinja', 'templates/principalfft/__init__.py', 'templates/principalfft/principalfft.jinja', 'templates/principalfft/lut_bool.jinja']
  },
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Code Generators',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
