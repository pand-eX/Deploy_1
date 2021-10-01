# Criação do Modelo de Machine Learning

# Imports
import joblib
from sklearn import datasets
from sklearn import svm

# Carrega o dataset
iris = datasets.load_iris()

# Divide os dados em entrada e saída para aprendizagem supervisionada
X, y = iris.data, iris.target

# Cria e treina o modelo
modelo = svm.LinearSVC(max_iter=10000)
modelo.fit(X, y)

# Grava o modelo
joblib.dump(modelo, 'modeloml1.pickle')