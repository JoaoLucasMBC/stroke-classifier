import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import matplotlib.pyplot as plt


class TreeClassifier():
    '''
    Classe que implementa um classificador por árvore de decisão
    baseado no conceito de entropia para realizar as melhores
    "perguntas" para realizar predições
    '''

    def __init__(self, df:pd.DataFrame):

        # Seleciona apenas as colunas de atributos do DataFrame
        self.X = df[['gender','age','hypertension','heart_disease','ever_married','work_type','Residence_type','avg_glucose_level','bmi','smoking_status']]
        
        filter = self.X['bmi'].notna() # Filtra para ficar apenas com as linhas que não possuem valor nulo na coluna bmi
        self.X = self.X[filter]

        # Transforma a coluna bmi em uma coluna categórica com 4 categorias: underweight, normal, overweight e obese
        self.X['bmi'] = pd.cut(self.X['bmi'], bins=[0, 18.5, 25, 30, 100], labels=['underweight', 'normal', 'overweight', 'obese'])

        # Transforma a coluna age em uma coluna categórica com 4 categorias: child, young, adult e elder
        self.X['age'] = pd.cut(self.X['age'], bins=[0, 12, 25, 60, 100], labels=['child', 'young', 'adult', 'elder'])

        # Transforma a coluna avg_glucose_level em uma coluna categórica com 4 categorias: low, normal, high e very high
        self.X['avg_glucose_level'] = pd.cut(self.X['avg_glucose_level'], bins=[0, 70, 140, 200, 300], labels=['low', 'normal', 'high', 'very high'])

        # Transforma todas as colunas categoricas em colunas one-hot (ou seja, sempre 0 ou 1)
        self.X = pd.get_dummies(self.X, dtype=int).astype(float)

        # Transforma a coluna stroke em uma coluna com valores -1 e 1 (para ser usada no gradiente descendente e ser predita em relação ao sinal)
        df['stroke'].replace(0, -1, inplace=True)
        
        # Separa a coluna stroke do DataFrame para ser os resultados do treinamento e também a filtra
        self.y = df['stroke']
        self.y = self.y[filter].astype(float)

        # Separa os dados em treinamento e teste
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, train_size=0.5)

        # Transforma os DataFrames em arrays numpy
        self.X_train, self.X_test, self.y_train, self.y_test = self.X_train.to_numpy(), self.X_test.to_numpy(), self.y_train.to_numpy(), self.y_test.to_numpy()


    def fit(self):
        '''
        Função que realiza o treinamento do classificador
        utilizando a classe DecisionTreeClassifier do sklearn
        de acordo com entropia
        '''
        self.tree = DecisionTreeClassifier(criterion='entropy')
        self.tree.fit(self.X_train, self.y_train)
    

    def score(self):
        '''
        Função que realiza a predição dos dados de teste
        utilizando os parâmetros treinados do classificador
        '''
        self.y_est = self.tree.predict(self.X_test)
        self.y_est = np.array(self.y_est)
    

    def accuracy(self):
        '''
        Função que calcula a acurácia do classificador
        de acordo com o sinal da saída estimada

        Positivo -> prediz que houve stroke
        Negativo -> prediz que não houve stroke
        '''
        return self.tree.score(self.X_test, self.y_test)


    def plot(self):
        '''
        Função que plota a árvore de decisão
        '''
        from sklearn.tree import plot_tree
        import matplotlib.pyplot as plt

        plt.figure(figsize=(20, 20))
        plot_tree(self.tree, filled=True, rounded=True, fontsize=14)
        plt.savefig('treeclassifier.png')
        plt.show()




def main():
    '''
    Função principal que realiza teste básico sem poda do classificador
    '''
    df = pd.read_csv('data/healthcare-dataset-stroke-data.csv')
    clf = TreeClassifier(df)

    clf.fit()
    clf.score()
    print(clf.accuracy())


    # Get the 3 most important features
    importances = clf.tree.feature_importances_
    indices = np.argsort(importances)[::-1]
    print("Feature ranking:")
    for f in range(3):
        # Print the name of the feature from the df dataframe
        print("%d. feature %d %s (%f)" % (f + 1, indices[f], clf.X.columns[indices[f]], importances[indices[f]]))

    
if __name__ == '__main__':
    main()