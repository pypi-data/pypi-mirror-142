from MixedTypeANN.approximate import LSHForest
import pandas as pd
import random
from sklearn.preprocessing import LabelEncoder

from MixedTypeANN.type_enum import Type


def pre_data(df):
    df['default'] = df['default'].map({'yes': 1, 'no': 0})
    df['housing'] = df['housing'].map({'yes': 1, 'no': 0})
    df['loan'] = df['loan'].map({'yes': 1, 'no': 0})

    label_columns = ['job', 'marital', 'education', 'contact']
    for label_column in label_columns:
        label_encoder = LabelEncoder()
        df[label_column] = label_encoder.fit_transform(df[label_column])

    return df


def run_model():
    print("lshf init")
    lshf = LSHForest(random_state=42)
    print("lshf create")
    lshf.fit(X_train, X_type)
    print("lshf.fit finished")
    distances, indices = lshf.kneighbors(X_test, n_neighbors=25)
    print(distances)
    print(indices)

def create_random_list(n=10000):
    randomlist = []
    for i in range(n):
        randomlist.append(random.sample(range(10, 100), 35))
    return randomlist

X_train = create_random_list(1000000)
X_test = create_random_list(600000)
print("created")
X_type = [Type.NUMARICAL, Type.NUMARICAL, Type.NUMARICAL]

# X_train = pd.read_csv("../data/train.csv", sep = ';')
# X_test = pd.read_csv("../data/test.csv", sep = ';')
#
# X_train = pre_data(X_train[['age', 'housing', 'default', 'loan', 'job', 'marital', 'education', 'contact']])
# X_test = pre_data(X_test[['age', 'housing', 'default', 'loan', 'job', 'marital', 'education', 'contact']])
# X_type = [Type.NUMARICAL, Type.NOMINAL, Type.NOMINAL, Type.NOMINAL, Type.NOMINAL, Type.ORDINAL_NOMINAL, Type.NOMINAL]

import time
start_time = time.time()
print(start_time)
run_model()
print("--- %s seconds ---" % (time.time() - start_time))
