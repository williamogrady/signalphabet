import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# Read data
data_dict = pickle.load(open("./data.pickle", "rb"))
data = np.asarray(data_dict["data"])
labels = np.asarray(data_dict["labels"])

# Make a train- and test-split, shuffle the data and keep proportions between the different lables
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)

# Defining and training the model
model = RandomForestClassifier()
model.fit(x_train, y_train)

# Testing the model
y_predict = model.predict(x_test)
score = accuracy_score(y_predict, y_test)
print("{}% of samples were classified correctly".format(score*100))