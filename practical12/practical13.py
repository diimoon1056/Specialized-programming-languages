from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()

df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
print("Перші 5 рядків датасету:")
print(df.head())

print("\nСтатистичні характеристики датасету:")
df.describe()

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
print("\nДані успішно розділено та масштабовано.")

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
logistic_reg = LogisticRegression(max_iter=1000)
logistic_reg.fit(X_train_scaled, y_train)

svm = SVC(kernel='linear')
svm.fit(X_train_scaled, y_train)

print("\nМоделі успішно навчені.")
from sklearn.metrics import accuracy_score
y_pred_logreg = logistic_reg.predict(X_test_scaled)
accuracy_logreg = accuracy_score(y_test, y_pred_logreg)
print("Accuracy of Logistic Regression:", accuracy_logreg)

y_pred_svm = svm.predict(X_test_scaled)
accuracy_svm = accuracy_score(y_test, y_pred_svm)
print("Accuracy of SVM:", accuracy_svm)
