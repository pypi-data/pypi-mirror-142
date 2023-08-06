# Import Dependencies
 
from sklearn.model_selection import train_test_split

from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB 
from sklearn.naive_bayes import BernoulliNB 
from sklearn.naive_bayes import MultinomialNB 

import pandas as pd

from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score


# Create the classifier function
def classifier_agent(dataset_path, output_column, train_test_ratio):

    results = pd.DataFrame(columns = ["Classifier", "Accuracy", "F1-Score"])
    try:
        df = pd.read_csv(dataset_path)
    except:
        df = pd.read_excel(dataset_path)
    
    y = df[output_column]
    X = df.drop(output_column,axis=1)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=train_test_ratio, random_state=42)

    list_of_models = [KNeighborsClassifier(), LogisticRegression(), DecisionTreeClassifier(), 
                      RandomForestClassifier(), GradientBoostingClassifier(), SVC(), GaussianNB(),
                      BernoulliNB(), MultinomialNB()]

    for model in list_of_models:
        try:
            print("Training on Model: ", str(model).split("()")[0])
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            acc = accuracy_score(y_test, y_pred)
            f1score = f1_score(y_test, y_pred)
            to_append = [str(model).split("()")[0], acc, f1score]
            df_length = len(results)
            results.loc[df_length] = to_append
        except:
           print("Failed to Train on Model: ", str(model).split("()")[0]) 

    print("Training on multiple models complete. Returning results of training as a dataframe....")
    return results