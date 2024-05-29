# -*- coding: utf-8 -*-
"""Project akhir.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JF8rS1LxI-4Q2OStVZwbFu0i4NFZux1A
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, mean_squared_error,r2_score, confusion_matrix, classification_report

data = pd.read_csv("telco_churn_mod.csv")

data.dtypes

data.describe()

data.head(100)

data['MonthlyCharges'].plot.hist(bins=100, alpha=0.5)

data['gender'] = data['gender'].map({'male': 1, 'female': 0})
data_numeric = data.drop(columns=['customerID'])
sns.heatmap(data_numeric.corr(), annot=True) #heatmap

data.isna().sum()

data['gender'] = data.gender

data['gender'] = data['gender'].map({'male': 1, 'female': 0})

# Hitung korelasi
correlation = data.corrwith(data['gender'])
#tampilkan korelasi

data[['TotalCharges','StreamingTV']].boxplot() #boxplot outlier

"""TotalCharges
Deskripsi

Median (Garis Tengah Kotak): Median biaya total (TotalCharges) berada pada sekitar 3900. Ini berarti bahwa separuh dari nilai TotalCharges berada di bawah 3900 dan separuh lainnya di atas 3900.

Interquartile Range (IQR): Kotak yang mewakili IQR (Q1 ke Q3) menunjukkan distribusi biaya total di sekitar median. Bagian bawah kotak adalah kuartil pertama (Q1), dan bagian atas kotak adalah kuartil ketiga (Q3).

Whiskers (Garis Panjang): Whiskers memperlihatkan rentang nilai TotalCharges yang tidak dianggap outliers. Nilai di luar whiskers ini biasanya dianggap outliers.

Outliers (Titik di Luar Whiskers): Titik-titik di luar whiskers adalah outliers, yaitu nilai TotalCharges yang sangat tinggi atau rendah dibandingkan dengan mayoritas data. Outliers ini bisa menunjukkan pelanggan dengan biaya total yang sangat tinggi.
"""

data.isna().sum() # mengidentifikasi missing value

data.dropna() #drop missing value / fix missing value

selected_features = correlation.abs().nlargest(5).index
print(selected_features) #tampilkan selected fitur

X,y=data.MonthlyCharges,data.TotalCharges
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42) #pembagian data dan test model

from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Assuming 'data' contains your dataset

# Drop rows with NaN values in y (target variable)
data_cleaned = data.dropna(subset=['TotalCharges'])

# Separate features (X) and target variable (y)
X = data_cleaned[['Contract']]
y = data_cleaned['TotalCharges']

# Impute NaN values in X (features)
imputer = SimpleImputer(strategy='mean')
X_imputed = imputer.fit_transform(X)

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_imputed, y, test_size=0.2, random_state=42)

# Initialize and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Calculate metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print results
print("Mean Squared Error:", mse)
print("R^2 Score:", r2)
# testing model data dan evaluasi model data

# evaluasi menggunakan imputer mean agar data yang kosong dapat diisi dengan data bernilai rata rata di suatu kolom tertentu, berhasil fix error

import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split, learning_curve
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Assuming 'data' contains your dataset

# Drop rows with NaN values in y (target variable)
data_cleaned = data.dropna(subset=['TotalCharges'])

# Separate features (X) and target variable (y)
X = data_cleaned[['Contract']]
y = data_cleaned['TotalCharges']

# Impute NaN values in X (features)
imputer = SimpleImputer(strategy='mean')
X_imputed = imputer.fit_transform(X)

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_imputed, y, test_size=0.2, random_state=42)

# Initialize and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Calculate metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print results
print("Mean Squared Error:", mse)
print("R^2 Score:", r2)

# Plot learning curve
train_sizes, train_scores, test_scores = learning_curve(
    model, X_imputed, y, cv=5, scoring='neg_mean_squared_error')

train_scores_mean = -np.mean(train_scores, axis=1)
test_scores_mean = -np.mean(test_scores, axis=1)

plt.figure(figsize=(10, 6))
plt.plot(train_sizes, train_scores_mean, label='Training error')
plt.plot(train_sizes, test_scores_mean, label='Cross-validation error')
plt.xlabel('Training examples')
plt.ylabel('MSE')
plt.title('Learning Curve')
plt.legend()
plt.show()

#Model Learning curve / Modelling no 6.

"""Model fit yang digunakan dalam contoh ini adalah Linear Regression. Linear Regression adalah salah satu teknik regresi yang digunakan untuk memodelkan hubungan antara satu atau lebih variabel independen (fitur) dengan variabel dependen (target) dengan menggunakan garis linear.

Dalam Linear Regression, model mencoba menemukan garis (atau hyperplane dalam dimensi yang lebih tinggi) yang paling cocok untuk menjelaskan hubungan antara variabel independen dan dependen. Proses fitting (penyesuaian) model melibatkan mencari parameter yang sesuai dengan data yang ada, sehingga kesalahan prediksi model terhadap data yang diberikan diminimalkan.

Dalam kode tersebut, model Linear Regression diinisialisasi dengan LinearRegression(), dan kemudian dipasangkan (fitted) dengan data menggunakan metode fit. Proses ini menyesuaikan garis regresi dengan data latih, yaitu data yang telah diimputasi dan dipisahkan menjadi X_train (fitur latih) dan y_train (target latih).

Setelah model dilatih, ia dapat digunakan untuk membuat prediksi terhadap data uji (X_test). Prediksi ini kemudian dievaluasi menggunakan metrik yang sesuai, seperti Mean Squared Error (MSE) dan R^2 Score, untuk mengukur seberapa baik model Linear Regression memodelkan data.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split, learning_curve
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import HuberRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Assuming 'data' contains your dataset

# Drop rows with NaN values in y (target variable)
data_cleaned = data.dropna(subset=['TotalCharges'])

# Separate features (X) and target variable (y)
X = data_cleaned[['Contract']]
y = data_cleaned['TotalCharges']

# Impute NaN values in X (features)
imputer = SimpleImputer(strategy='mean')
X_imputed = imputer.fit_transform(X)

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_imputed)

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Initialize and train the Huber Regression model
model = HuberRegressor()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Calculate metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print results
print("Mean Squared Error:", mse)
print("R^2 Score:", r2)

# Plot learning curve
train_sizes, train_scores, test_scores = learning_curve(
    model, X_scaled, y, cv=5, scoring='neg_mean_squared_error')

train_scores_mean = -np.mean(train_scores, axis=1)
test_scores_mean = -np.mean(test_scores, axis=1)

plt.figure(figsize=(10, 6))
plt.plot(train_sizes, train_scores_mean, label='Training error')
plt.plot(train_sizes, test_scores_mean, label='Cross-validation error')
plt.xlabel('Training examples')
plt.ylabel('MSE')
plt.title('Learning Curve')
plt.legend()
plt.show()

"""- menggunakan StandardScaler untuk menstandarisasi fitur-fitur (variabel independen).

- menggunakan HuberRegressor sebagai model regresi robust yang lebih tahan terhadap outlier.

- setelah melatih model, kami membuat prediksi pada set data uji dan menghitung metrik evaluasi seperti sebelumnya.

- menggunakan learning_curve untuk menggambarkan kurva pembelajaran model dengan menggunakan Mean Squared Error sebagai metrik evaluasi.

- grafik kurva pembelajaran menunjukkan bagaimana kinerja model meningkat seiring dengan jumlah sampel yang digunakan untuk melatih model.

9.PERBEDAAN MODEL SETELAH PERBAIKAN IMBALANCED DATA

Sebelum dan sesudah penanganan data yang tidak seimbang, terdapat beberapa perbedaan yang dapat diamati dalam hasil:

Metrik Evaluasi Model: Setelah penanganan data yang tidak seimbang, metrik evaluasi model seperti Mean Squared Error (MSE) dan R^2 Score mungkin berubah. MSE mengukur seberapa dekat prediksi model dengan nilai sebenarnya, sedangkan R^2 Score mengukur seberapa baik model menjelaskan variasi dalam data. Perubahan dalam metrik evaluasi ini dapat memberikan gambaran tentang peningkatan atau penurunan kinerja model setelah penanganan data yang tidak seimbang.

Kurva Pembelajaran: Kurva pembelajaran menunjukkan bagaimana kinerja model berkembang seiring dengan penambahan data latih. Setelah penanganan data yang tidak seimbang, kurva pembelajaran mungkin menunjukkan pola yang berbeda dalam hal peningkatan kinerja model. Ini dapat mencerminkan efek dari penanganan data yang tidak seimbang terhadap kemampuan model untuk belajar dari data.

Stabilitas Model: Setelah penanganan data yang tidak seimbang, model mungkin menjadi lebih stabil dalam membuat prediksi terhadap data baru. Ini dapat tercermin dalam perubahan dalam variabilitas hasil prediksi antara pengujian yang berbeda.

Secara keseluruhan, perbedaan dalam hasil sebelum dan sesudah penanganan data yang tidak seimbang mencerminkan dampak dari strategi penanganan tersebut terhadap kinerja dan stabilitas model regresi linear.

Kesimpulan dari semua model ini adalah

Linear Regression tanpa Penanganan Data Tidak Seimbang: Model regresi linear tanpa penanganan data yang tidak seimbang menghasilkan hasil evaluasi yang mungkin tidak optimal saat dihadapkan pada data yang tidak seimbang. Hal ini dapat terjadi karena model cenderung lebih sensitif terhadap perbedaan distribusi data.

Linear Regression dengan Penanganan Data Tidak Seimbang: Setelah penanganan data yang tidak seimbang, model regresi linear dapat menunjukkan peningkatan kinerja dan stabilitas dalam memprediksi nilai target. Dengan penanganan yang tepat terhadap masalah ketidakseimbangan, model dapat memberikan prediksi yang lebih akurat dan konsisten.

Pemilihan Model Regresi yang Tepat: Dalam beberapa kasus, seperti ketika terdapat outlier atau ketidakseimbangan yang signifikan dalam data, menggunakan regresi robust seperti Huber Regression dapat menjadi pilihan yang lebih baik daripada regresi linear biasa. Model regresi robust dapat memberikan hasil yang lebih stabil dan dapat diandalkan terhadap variasi dalam data.

Dengan demikian, pemilihan model dan penanganan data yang tepat sangat penting dalam membangun model regresi yang efektif dan dapat diandalkan untuk memprediksi nilai target.
"""