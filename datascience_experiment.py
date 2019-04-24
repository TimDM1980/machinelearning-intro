import pandas as pd
import sklearn

titanic_tickets = pd.read_csv('titanic_tickets.csv')

replacements = {
    'Sex': {
        'male': 0,
        'female': 1
    },
    'Embarked': {
        'S': 1,
        'C': 2,
        'Q': 3,
    }
}

cleaned = titanic_tickets\
    .drop(columns=['PassengerId', 'Name', 'Ticket', 'Cabin'])\
    .dropna()\
    .replace(replacements)

# print(cleaned)

from sklearn.model_selection import train_test_split

# labels = het resultaat dat we zoeken, nl survived of niet
# dit zit in de 0e kolom
labels = cleaned.iloc[:, 0]
# print(labels)

# features = de data die we kunnen gebruiken om het resultaat te zoeken
# dit zit in de andere kolommen
features = cleaned.iloc[:, 1:8]
# print(features)

features_train, features_test, labels_train, labels_test = train_test_split(features, labels)

from sklearn.neighbors import KNeighborsClassifier

kn_clf = KNeighborsClassifier()
kn_clf = kn_clf.fit(features_train, labels_train)

print(kn_clf.score(features_train, labels_train))
print(kn_clf.score(features_test, labels_test))

from sklearn.tree import DecisionTreeClassifier

dt_clf = DecisionTreeClassifier()
dt_clf = dt_clf.fit(features_train, labels_train)

print(dt_clf.score(features_train, labels_train))
print(dt_clf.score(features_test, labels_test))
