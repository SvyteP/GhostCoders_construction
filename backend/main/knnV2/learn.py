import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.neighbors import NearestNeighbors # Модель поиска k-ближайших соседей
import joblib


# Загрузка данных
df = pd.read_csv('data/clean.csv')  
titles = df['Наименование'].tolist()

# Преобразование текстовых данных в TF-IDF векторы 
vectorizer = TfidfVectorizer(min_df=1, max_df=0.6, token_pattern=r"\b\w\w+\b|\d+")
tfidf_matrix = vectorizer.fit_transform(titles)

# Настройка и обучение модели KNN
knn = NearestNeighbors(n_neighbors=5, metric='cosine') # cosine - измеряет угол между двумя векторами в пространстве 
# n_neighbors - количество ближайших соседей
knn.fit(tfidf_matrix)

# Сохранение модели и векторизатора
joblib.dump(vectorizer, 'knnV2/tfidf_vectorizer.pkl')
joblib.dump(knn, 'knnV2/knn_model.pkl')











# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.neighbors import NearestNeighbors
# import joblib

# # Загрузка данных
# df = pd.read_csv('data/clean.csv')
# titles = df['Наименование'].tolist()

# # Предобработка текста для устранения возможных опечаток
# def preprocess_text(text):
#     # Пример: приведение текста к нижнему регистру и удаление лишних пробелов
#     text = text.lower().strip()
#     # Добавьте другие правила предобработки по необходимости
#     return text

# # Преобразование текстовых данных в TF-IDF векторы
# vectorizer = TfidfVectorizer(min_df=1, max_df=0.6, token_pattern=r"\b\w\w+\b|\d+")
# tfidf_matrix = vectorizer.fit_transform([preprocess_text(title) for title in titles])

# # Настройка и обучение модели KNN
# knn = NearestNeighbors(n_neighbors=10, metric='cosine')
# knn.fit(tfidf_matrix)

# # Сохранение модели и векторизатора
# joblib.dump(vectorizer, 'knnV2/tfidf_vectorizer.pkl')
# joblib.dump(knn, 'knnV2/knn_model.pkl')

# print("Модель обучена и сохранена.")





