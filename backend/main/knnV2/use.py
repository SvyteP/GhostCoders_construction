# import pandas as pd
# import joblib

# # Загрузка данных
# df = pd.read_csv('data/clean.csv')  
# titles = df['Наименование'].tolist()

# # Загрузка сохраненной модели и векторизатора
# vectorizer = joblib.load('knnV2/tfidf_vectorizer.pkl')
# knn = joblib.load('knnV2/knn_model.pkl')

# # Функция для предсказания наиболее похожих названий и их расстояний
# def predict_similar_titles_with_distances(input_title, titles, vectorizer, knn):
#     input_vec = vectorizer.transform([input_title])
#     distances, indices = knn.kneighbors(input_vec)
#     similar_titles = [(titles[idx], distances[0][i]) for i, idx in enumerate(indices[0])]
#     return similar_titles

# # Пример использования с выводом наиболее вероятных заголовков, их кодов и расстояний
# input_title = "Шнек двз Бур.1700 мм,450 мм"
# similar_titles_with_distances = predict_similar_titles_with_distances(input_title, titles, vectorizer, knn)
# print(f"\nV1_Входное: '{input_title}' \nНаиболее вероятные заголовки, их коды и расстояния:\n")
# for title, distance in similar_titles_with_distances:
#     print(f"Код: {df[df['Наименование'] == title]['Код ресурса'].values[0]}, Заголовок: {title}, Уверенность: {1-distance}")



# import pandas as pd
# import joblib
# import difflib

# # Загрузка данных
# df = pd.read_csv('data/clean.csv')  
# titles = df['Наименование'].tolist()

# # Загрузка сохраненной модели и векторизатора
# vectorizer = joblib.load('knnV2/tfidf_vectorizer.pkl')
# knn = joblib.load('knnV2/knn_model.pkl')

# # Функция для предсказания наиболее похожих названий и их расстояний
# def predict_similar_titles_with_distances(input_title, titles, vectorizer, knn):
#     # Используем difflib для поиска наиболее похожих строк
#     closest_matches = difflib.get_close_matches(input_title, titles, cutoff=0.4)
#     print(closest_matches)
    
#     # Если есть близкие совпадения, выбираем первое
#     if closest_matches:
#         input_title = closest_matches[0]
#     else:
#         print("Похожих заголовков не найдено, используем входной заголовок как есть.")
    
#     input_vec = vectorizer.transform([input_title])
#     distances, indices = knn.kneighbors(input_vec)
#     similar_titles = [(titles[idx], distances[0][i]) for i, idx in enumerate(indices[0])]
#     return similar_titles

# # Пример использования с выводом наиболее вероятных заголовков, их кодов и расстояний
# input_title = "Выключатель с зад стен 2кл 16А"
# similar_titles_with_distances = predict_similar_titles_with_distances(input_title, titles, vectorizer, knn)
# print(f"\nV2_Входное: '{input_title}' \nНаиболее вероятные заголовки, их коды и расстояния:\n")
# for title, distance in similar_titles_with_distances:
#     print(f"{df[df['Наименование'] == title]['Код ресурса'].values[0]},  {title}, Уверенность: {1-distance}")







# import pandas as pd
# import joblib
# import difflib

# # Загрузка данных
# df = pd.read_csv('data/clean.csv')  
# titles = df['Наименование'].tolist()

# # Загрузка сохраненной модели и векторизатора
# vectorizer = joblib.load('knnV2/tfidf_vectorizer.pkl')
# knn = joblib.load('knnV2/knn_model.pkl')

# # Функция для предсказания наиболее похожих названий и их расстояний
# def predict_similar_titles_with_distances(input_title, titles, vectorizer, knn):
#     # Используем difflib для поиска наиболее похожих строк
#     closest_matches = difflib.get_close_matches(input_title, titles, cutoff=0.1)
#     print(closest_matches)
    
#     # Если есть близкие совпадения, выбираем первое
#     if closest_matches:
#         input_title = closest_matches[0]
#     else:
#         print("Похожих заголовков не найдено, используем входной заголовок как есть.")
    
#     input_vec = vectorizer.transform([input_title])
#     distances, indices = knn.kneighbors(input_vec)
#     similar_titles = [(titles[idx], distances[0][i]) for i, idx in enumerate(indices[0])]
#     return similar_titles

# # Пример использования с выводом наиболее вероятных заголовков, их кодов и расстояний
# input_title = "Заслdqwонка для прямоугdольных,300 150"
# similar_titles_with_distances = predict_similar_titles_with_distances(input_title, titles, vectorizer, knn)
# print(f"\nV2_Входное: '{input_title}' \nНаиболее вероятные заголовки, их коды и расстояния:\n")
# for title, distance in similar_titles_with_distances:
#     print(f"{df[df['Наименование'] == title]['Код ресурса'].values[0]},  {title}") 





# import pandas as pd
# import joblib
# import difflib


# # Загрузка данных
# df = pd.read_csv('data/clean.csv')  
# titles = df['Наименование'].tolist()

# # Загрузка сохраненной модели и векторизатора
# vectorizer = joblib.load('knnV2/tfidf_vectorizer.pkl')
# knn = joblib.load('knnV2/knn_model.pkl')

# # Функция для предсказания наиболее похожих названий и их расстояний
# def predict_similar_titles_with_distances(input_title, titles, vectorizer, knn):
#     # Используем difflib для поиска наиболее похожих строк
#     closest_matches = difflib.get_close_matches(input_title, titles, cutoff=0.7) # cutoff - минимальная доля схожести 
#     print(closest_matches)

#     closest_matches2 = difflib.get_close_matches(input_title, titles, cutoff=0.4) # cutoff - минимальная доля схожести 
#     print(closest_matches2)


#     # Если есть близкие совпадения, выбираем первое
#     if closest_matches:
#         input_title = closest_matches[0]
    
#     input_vec = vectorizer.transform([input_title])
#     distances, indices = knn.kneighbors(input_vec)
    
#     similar_titles = [(titles[idx], distances[0][i]) for i, idx in enumerate(indices[0])]
#     return similar_titles


# # Использование модели
# input_title = "Заслdqwонка для прямоугdольных,300 150"
# similar_titles_with_distances = predict_similar_titles_with_distances(input_title, titles, vectorizer, knn)

# # Вычисляем сумму расстояний
# total_distance = sum(distance for title, distance in similar_titles_with_distances)

# if total_distance > 0:
#     print(f"\nV2_Входное: '{input_title}' \nНаиболее вероятные заголовки, их коды и расстояния:\n")
#     for title, distance in similar_titles_with_distances:
#         код_ресурса = df[df['Наименование'] == title]['Код ресурса'].values
#         if len(код_ресурса) > 0:
#             код_ресурса = код_ресурса[0]
#             # Нормализуем расстояние
#             score = (1 - distance / total_distance) * 100
#             # print(distance)
#             print(f"{код_ресурса},\t{title}, \t\tУверенность: {score:.2f} из 100")
#         else:
#             print(f"Не найден код ресурса для заголовка: {title}")
# else:
#     print("Такого ресурса")











# Результат dflib в knn
import pandas as pd
import joblib
import difflib


# Загрузка данных
df = pd.read_csv('backend/main/data/clean.csv')  
titles = df['Наименование'].tolist()

# Загрузка сохраненной модели и векторизатора
vectorizer = joblib.load('backend/main/knnV2/tfidf_vectorizer.pkl')
knn = joblib.load('backend/main/knnV2/knn_model.pkl')

# Функция для предсказания наиболее похожих названий и их расстояний
def predict_similar_titles_with_distances(input_title, titles, vectorizer, knn):
    # Используем difflib для поиска наиболее похожих строк
    closest_matches = difflib.get_close_matches(input_title, titles, cutoff=0.65) # cutoff - минимальная доля схожести 
    print(closest_matches)

    # Если есть близкие совпадения, выбираем первое и отправляем векторизованное представление в KNN модель
    if closest_matches:
        input_title = closest_matches[0]
        input_vec = vectorizer.transform([input_title])
        distances, indices = knn.kneighbors(input_vec)
        print(distances)
        similar_titles = [(titles[idx], distances[0][i]) for i, idx in enumerate(indices[0])]
        return similar_titles
    
    # Если нет близких совпадений, сразу возвращаем результаты KNN модели
    input_vec = vectorizer.transform([input_title])
    distances, indices = knn.kneighbors(input_vec)
    similar_titles = [(titles[idx], distances[0][i]) for i, idx in enumerate(indices[0])]
    print(distances)
    return similar_titles


# Использование модели
input_title = "Заслdqwонка для прямоугdольных,300 150"
similar_titles_with_distances = predict_similar_titles_with_distances(input_title, titles, vectorizer, knn)

# Вычисляем сумму расстояний
total_distance = sum(distance for title, distance in similar_titles_with_distances)

if total_distance > 0 and total_distance < knn.n_neighbors:
    print(f"\nV2_Входное: '{input_title}' \nНаиболее вероятные заголовки, их коды и расстояния:\n")
    for title, distance in similar_titles_with_distances:
        код_ресурса = df[df['Наименование'] == title]['Код ресурса'].values
        if len(код_ресурса) > 0:
            код_ресурса = код_ресурса[0]
            # Нормализуем расстояние
            score = (1 - distance / total_distance) * 100
            # print(distance)
            print(f"{код_ресурса},\t{title}, \t\tУверенность: {score:.2f} из 100")
        else:
            print(f"Не найден код ресурса для заголовка: {title}")
else:
    print("Такого ресурса нет")





# KNN в Dflib
# import pandas as pd
# import joblib
# import difflib


# # Загрузка данных
# df = pd.read_csv('data/clean.csv')  
# titles = df['Наименование'].tolist()

# # Загрузка сохраненной модели и векторизатора
# vectorizer = joblib.load('knnV2/tfidf_vectorizer.pkl')
# knn = joblib.load('knnV2/knn_model.pkl')

# # Функция для предсказания наиболее похожих названий и их расстояний
# def predict_closest_title(input_title, titles, vectorizer, knn):
#     # Используем KNN для поиска наиболее похожего заголовка
#     input_vec = vectorizer.transform([input_title])
#     distances, indices = knn.kneighbors(input_vec)
#     closest_title = titles[indices[0][0]]
#     return closest_title

# def find_best_match(input_title, titles, filtered_titles):
#     # Используем difflib для поиска наиболее похожих заголовков в отфильтрованном списке
#     closest_matches = difflib.get_close_matches(input_title, filtered_titles, cutoff=0.7)
 
#     # Если есть близкие совпадения, выбираем наиболее подходящий
#     if closest_matches:
#         return closest_matches[0]
#     else:
#         return None

# def predict_similar_titles_with_distances(input_title, titles, vectorizer, knn):
#     closest_title = predict_closest_title(input_title, titles, vectorizer, knn)
    
#     filtered_titles = [title for title in titles if difflib.SequenceMatcher(None, closest_title, title).ratio() >= 0.7]

#     best_match = find_best_match(closest_title, titles, filtered_titles)

#     if best_match:
#         best_match_distance = difflib.SequenceMatcher(None, closest_title, best_match).ratio()
#         return [(best_match, best_match_distance)]
#     else:
#         input_vec = vectorizer.transform([closest_title])
#         distances, indices = knn.kneighbors(input_vec)
#         closest_distance = distances[0][0]
#         return [(closest_title, closest_distance)]

# # Пример использования
# input_title = "Заслонка регулирующая для прямоугольных каналов, ширина 300, высота 150 "
# similar_titles_with_distances = predict_similar_titles_with_distances(input_title, titles, vectorizer, knn)
