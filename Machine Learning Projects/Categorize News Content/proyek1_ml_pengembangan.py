# -*- coding: utf-8 -*-
"""Proyek1_ML_Pengembangan.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1f3jz3okU_UdJvY3s0O4OyYwmxjzcqTvu

# Proyek 1: Membuat Model NLP dengan TensorFlow
---

Oleh: Mohammad Aditya Rafi Pratama (madityarafip - madityarafip31@gmail.com) - Depok, Indonesia

Pada proyek ini akan dirancang sebuah model NLP dari Machine Learning yang bertujuan untuk mengklasifikasi sebuah teks berita apakah termasuk kedalam kategori berita *business*, *entertainment*, *politics*, *sport*, atau *tech*.
---

---

Proses pertama adalah import library yang digunakan
"""

import pandas as pd

import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt

from google.colab import files

"""Dengan memanfaatkan library yang tersedia pada Google Colab, dataset yang diperlukan akan diupload menggunakan fungsi upload."""

uploaded = files.upload()

"""Setelah data berhasil diload, langkah selanjutnya adalah membaca file .csv dari dataset yang digunakan dengan menggunakan fungsi yang terdapat pada library pandas."""

df = pd.read_csv('bbc-news-data.csv', sep=None)
df.head()

"""Dapat dilihat pada tampilan data terdapat 4 kolom yang terbaca. Pada proyek ini hanya menggunakan 2 kolom yaitu, kolom *content* dan kolom *category*. Sehingga kedua kolom sisanya dapat dihilangkan dengan fungsi drop."""

df = df.drop(columns=['filename'])
df = df.drop(columns=['title'])
df.head()

"""Karena label berupa data kategorikal, maka perlu dilakukan proses one-hot-encoding."""

category = pd.get_dummies(df.category)
new_df = pd.concat([df, category], axis=1)
new_df = new_df.drop(columns='category')
new_df

"""Proses selanjutnya adalah membagi data training dan data testing"""

content = new_df['content'].values
tags = new_df[['business','entertainment','politics','sport','tech']]

content_train, content_test, tags_train, tags_test = train_test_split(content, tags, test_size=0.2)

"""Kemudian ubah setiap kata pada dataset ke dalam bilangan numerik dengan fungsi Tokenizer. Setelah tokenisasi selesai, perlu dilakukan konversi setiap sampel menjadi sequence"""

tokenizer = Tokenizer(num_words=50000, oov_token='-', lower=False)
tokenizer.fit_on_texts(content_train) 
tokenizer.fit_on_texts(content_test)
     
content_train = tokenizer.texts_to_sequences(content_train)
content_test = tokenizer.texts_to_sequences(content_test)
     
padded_train = pad_sequences(content_train) 
padded_test = pad_sequences(content_test)

"""Untuk arsitektur model menggunakan layer Embedding dengan dimensi embedding sebesar 20, serta dimensi dari input sebesar nilai num_words pada objek tokenizer. Pada model ini juga digunakan fungsi dropout sebersar 20% yang berfungsi untuk mengatasi overfitting."""

import tensorflow as tf
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=50000, output_dim=20),
    tf.keras.layers.LSTM(64),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(5, activation='softmax')
])

model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])

"""Sebelum masuk proses melatih/training model dibutuhkan proses callback yang berfungi untuk memberhentikan proses pelatihan ketika mencapai akurasi yang ditentukan, yang dimana pada proyek ini akan berhenti ketika mencapai akurasi >85%."""

class Callback(tf.keras.callbacks.Callback): 
    def on_epoch_end(self, epoch, logs={}): 
        if(logs.get('accuracy') > 0.85 and logs.get('val_accuracy') > 0.85):
            print("\nReached 85% accuracy") 
            self.model.stop_training = True 
     
callbacks = Callback()

"""Proses selanjutnya adalah melatih model dengan menggunakan fungsi fit(). Pada proses ini juga akan dimasukkan nilai Epoch yang diinginkan dengan fungsi input()."""

num_epochs = int(input('Epoch = '))
print(' ')
history = model.fit(padded_train, tags_train, 
                    epochs=num_epochs, 
                    validation_data=(padded_test, tags_test),
                    validation_steps=3, 
                    verbose=2,
                    callbacks=[callbacks]
                    )

"""Setelah proses pelatihan selesai kita dapat melakukan plot akurasi dan loss yang dihasilkan oleh model untuk setiap epoch yang berjalan."""

#Grafik loss dari model
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()

#Grafik accuracy dari model
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()