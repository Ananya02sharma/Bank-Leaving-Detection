import pickle
import json
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

sc = StandardScaler()
__locations = None
__data_columns = None
__model = None

def get_estimated_decision(location,credit_score,gender,age,tenure,balance,number_of_products,has_credit_card,is_a_active_member,Estimated_salary):
    term1 = 0 
    term2 = 0
    term3 = 0
    if(location == "France"):
        term1 = 1
        term2 = 0
        term3 = 0
    elif (location == "Spain"):
        term1 = 0
        term2 = 0
        term3 = 1
    else:
        term1 = 0
        term2 = 1
        term3 = 0
    dataset = pd.read_csv('./model/Churn_Modelling.csv')
    X = dataset.iloc[:, 3:-1].values
    y = dataset.iloc[:, -1].values
    le = LabelEncoder()
    X[:, 2] = le.fit_transform(X[:, 2])
    ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [1])], remainder='passthrough')
    X = np.array(ct.fit_transform(X))
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
    sc.fit_transform(X_train)

    print(sc.transform([[term1, term2, term3,credit_score, gender, age, tenure,balance, number_of_products, has_credit_card, is_a_active_member,Estimated_salary]]))

    data = sc.transform([[term1, term2, term3,credit_score, gender, age, tenure,balance,
                                           number_of_products, has_credit_card, is_a_active_member,Estimated_salary]])
    return __model.predict(data) > 0.5


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __locations

    with open("./model/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[:] 
    global __model
    if __model is None:
        with open('./model/model_building.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_decision("Spain",510,1,43,2,125510.82,1,1,1,79084.1))
   