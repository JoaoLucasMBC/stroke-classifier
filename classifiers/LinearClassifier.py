import numpy as np
import autograd.numpy as np_   # Thinly-wrapped version of Numpy
from autograd import grad
from sklearn.model_selection import train_test_split
import pandas as pd


class LinearClassifier():

    def __init__(self, df:pd.DataFrame):

        self.X = df[['gender','age','hypertension','heart_disease','ever_married','work_type','Residence_type','avg_glucose_level','bmi','smoking_status']]
        filter = self.X['bmi'].notna()
        self.X = self.X[filter]

        # Transforms the bmi column in a categorical column with 4 categories: underweight, normal, overweight and obese
        self.X['bmi'] = pd.cut(self.X['bmi'], bins=[0, 18.5, 25, 30, 100], labels=['underweight', 'normal', 'overweight', 'obese'])

        # Transforms the age column in a categorical column with 4 categories: child, young, adult and elder
        self.X['age'] = pd.cut(self.X['age'], bins=[0, 12, 25, 60, 100], labels=['child', 'young', 'adult', 'elder'])

        # Transforms the avg_glucose_level column in a categorical column with 4 categories: low, normal, high and very high
        self.X['avg_glucose_level'] = pd.cut(self.X['avg_glucose_level'], bins=[0, 70, 140, 200, 300], labels=['low', 'normal', 'high', 'very high'])

        self.X = pd.get_dummies(self.X, dtype=int).astype(float)

        df['stroke'].replace(0, -1, inplace=True)
        self.y = df['stroke']
        self.y = self.y[filter].astype(float)

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, train_size=0.5)
        self.X_train, self.X_test, self.y_train, self.y_test = self.X_train.to_numpy(), self.X_test.to_numpy(), self.y_train.to_numpy(), self.y_test.to_numpy()


    def fit(self):
        g = grad(LinearClassifier.loss)

        w = np.random.randn(self.X_train.shape[1],1)
        b = 0.0
        alpha = 10**-2

        for n in range(5000):
            grad_ = g( (w, b, self.X_train.T, self.y_train) )
            w -= alpha*grad_[0]
            b -= alpha*grad_[1]
        
        self.w = w
        self.b = b


    def score(self):
        self.y_est = self.b + self.w.T @ self.X_test.T

    
    def loss( parametros ):
        w, b, pontos, val = parametros
        est = w.T @ pontos + b
        mse = np_.mean( (est - val)**2)
        return mse
    

    def accuracy(self):
        return np.mean(np.sign(self.y_test)==np.sign(self.y_est))
    




def main():
    df = pd.read_csv('data/healthcare-dataset-stroke-data.csv')
    clf = LinearClassifier(df)

    clf.fit()
    clf.score()
    print(clf.accuracy())

    # Get the 3 most important features
    print(clf.X.columns[np.argsort(clf.w.T)[0][-3:]])

    # ideias:
    # * faixas categóricas para os floats
    # * fazer uma versão sem idade e bmi
    # * rodar 100 vezes com muitos steps e ver a coluna de maior peso que ocorre mais vezes
    # * ver o que o de árvore dá de features mais importantes e cruzar (intersecção) com o que o linear deu
    
if __name__ == '__main__':
    main()