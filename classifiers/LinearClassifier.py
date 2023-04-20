import numpy as np
import autograd.numpy as np_   # Thinly-wrapped version of Numpy
from autograd import grad
from sklearn.model_selection import train_test_split
import pandas as pd


class LinearClassifier():

    def __init__(self, df:pd.DataFrame):

        self.X = df[['gender','age','hypertension','heart_disease','ever_married','work_type','Residence_type','avg_glucose_level','bmi','smoking_status']]

        self.X = pd.get_dummies(self.X, dtype=int)
        filter = self.X['bmi'].notna()
        self.X = self.X[filter].astype(float)

        df['stroke'].replace(0, -1, inplace=True)
        self.y = df['stroke']
        self.y = self.y[filter].astype(float)

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, train_size=0.5)
        self.X_train, self.X_test, self.y_train, self.y_test = self.X_train.to_numpy(), self.X_test.to_numpy(), self.y_train.to_numpy(), self.y_test.to_numpy()


    def fit(self):
        g = grad(LinearClassifier.loss)

        w = np.random.randn(self.X_train.shape[1],1)
        b = 0.0
        alpha = 10**-5

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
    
if __name__ == '__main__':
    main()