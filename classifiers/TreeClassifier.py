import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import matplotlib.pyplot as plt


class TreeClassifier():

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
        
        self.tree = DecisionTreeClassifier(criterion='entropy')
        self.tree.fit(self.X_train, self.y_train)
    

    def score(self):

        self.y_est = self.tree.predict(self.X_test)
        self.y_est = np.array(self.y_est)
    

    def accuracy(self):

        return self.tree.score(self.X_test, self.y_test)


    def plot(self):

        from sklearn.tree import plot_tree
        import matplotlib.pyplot as plt

        plt.figure(figsize=(20, 20))
        plot_tree(self.tree, filled=True, rounded=True, fontsize=14)
        plt.savefig('treeclassifier.png')
        plt.show()




def main():
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