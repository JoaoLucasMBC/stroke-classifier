import numpy as np
import autograd.numpy as np_   # Thinly-wrapped version of Numpy
from autograd import grad
from sklearn.model_selection import train_test_split
import pandas as pd


class LinearClassifier():
    '''
    Classe que implementa um classificador linear
    treinado com gradiente descendente para realizar predições
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
        '''

        # Função que calcula o gradiente da função de perda
        g = grad(LinearClassifier.loss)

        # Inicializa os parâmetros do classificador
        w = np.random.randn(self.X_train.shape[1],1)
        b = 0.0
        alpha = 10**-2
        
        # Realiza o treinamento com 5k episódios
        for n in range(5000):
            grad_ = g( (w, b, self.X_train.T, self.y_train) )
            w -= alpha*grad_[0]
            b -= alpha*grad_[1]
        
        # Salva os parâmetros do classificador
        self.w = w
        self.b = b


    def score(self):
        '''
        Função que realiza a predição dos dados de teste
        utilizando os parâmetros treinados do classificador
        '''
        self.y_est = self.b + self.w.T @ self.X_test.T

    
    def loss( parametros ):
        '''
        Função que calcula o erro quadrático médio
        entre a saída real e a saída estimada
        '''
        w, b, pontos, val = parametros
        est = w.T @ pontos + b
        mse = np_.mean( (est - val)**2)
        return mse
    

    def accuracy(self):
        '''
        Função que calcula a acurácia do classificador
        de acordo com o sinal da saída estimada

        Positivo -> prediz que houve stroke
        Negativo -> prediz que não houve stroke
        '''
        return np.mean(np.sign(self.y_test)==np.sign(self.y_est))
    




def main():
    '''
    Função principal que realiza teste básico sem poda do classificador
    '''
    df = pd.read_csv('data/healthcare-dataset-stroke-data.csv')
    clf = LinearClassifier(df)

    clf.fit()
    clf.score()
    print(clf.accuracy())

    # Get the 3 most important features
    print(clf.X.columns[np.argsort(clf.w.T)[0][-3:]]) 
    
if __name__ == '__main__':
    main()