

# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from .forms import TitleForm
# from io import BytesIO
# import pandas as pd
# import joblib
# import difflib
# import json
# import os
# from django.views.decorators.csrf import csrf_exempt

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# file_path = os.path.join(BASE_DIR, 'main', 'data', 'clean.csv')

# if os.path.exists(file_path):
#     df = pd.read_csv(file_path)
#     titles = df['Наименование'].tolist()
# else:
#     raise FileNotFoundError(f"File not found: {file_path}")

# vectorizer = joblib.load(os.path.join(BASE_DIR, 'main', 'knnV2', 'tfidf_vectorizer.pkl'))
# knn = joblib.load(os.path.join(BASE_DIR, 'main', 'knnV2', 'knn_model.pkl'))


# def predict_similar_titles_with_distances(input_title, titles, vectorizer, knn):
#     closest_matches = difflib.get_close_matches(input_title, titles, cutoff=0.65)
#     if closest_matches:
#         input_title = closest_matches[0]
#     input_vec = vectorizer.transform([input_title])
#     distances, indices = knn.kneighbors(input_vec)
#     most_probable_title = titles[indices[0][0]]
#     distance = distances[0][0]
#     return most_probable_title, distance



# def index(request):
#     return render(request, 'index.html')


# def classify_title(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             input_title = data.get('input', '')

#             if not input_title:
#                 return JsonResponse({'error': 'No input title provided'}, status=400)
            
#             most_probable_title, distance = predict_similar_titles_with_distances(input_title, titles, vectorizer, knn)

#             код_ресурса = df[df['Наименование'] == most_probable_title]['Код ресурса'].values
#             if len(код_ресурса) > 0:
#                 код_ресурса = код_ресурса[0]
#                 score = (1 - distance) * 100
#                 result = {
#                     'код_ресурса': код_ресурса,
#                     'title': most_probable_title,
#                     'score': f"{score:.2f}"
#                 }
#             else:
#                 result = {
#                     'код_ресурса': None,
#                     'title': most_probable_title,
#                     'score': 'Не найден код ресурса для заголовка'
#                 }

#             return JsonResponse({'result': result})
#         except json.JSONDecodeError:
#             return JsonResponse({'error': 'Invalid JSON'}, status=400)
#     else:
#         return JsonResponse({'error': 'Invalid HTTP method'}, status=405)


# def upload_file(request):
#     if request.method == 'POST':
#         output_files = []

#         try:
#             for uploaded_file in request.FILES.getlist('file'):
#                 df_to_update = pd.read_csv(uploaded_file)

#                 for index, row in df_to_update.iterrows():
#                     input_title = row['name']
#                     most_probable_title, distance = predict_similar_titles_with_distances(input_title, titles, vectorizer, knn)

#                     print(distance)
#                     print(knn.n_neighbors)
                    
#                     if distance < knn.n_neighbors:
#                         code = df[df['Наименование'] == most_probable_title]['Код ресурса'].values
#                         if len(code) > 0:
#                             code = code[0]
#                             df_to_update.at[index, 'КСР наименование'] = most_probable_title
#                             df_to_update.at[index, 'КСР код'] = code
#                         else:
#                             print(f"Не найден код ресурса для заголовка: {most_probable_title}")
#                     else:
#                         print("Такого ресурса нет")

#                 output_filename = f"output_{len(output_files) + 1}.csv"
#                 output_path = os.path.join(BASE_DIR, 'main', 'output', output_filename)
#                 df_to_update.to_csv(output_path, index=False)
#                 output_files.append(output_filename)

#             # Создаем ссылки для скачивания файлов
#             file_urls = []
#             for output_file in output_files:
#                 file_url = request.build_absolute_uri(f'/download/?file_name={output_file}')
#                 file_urls.append({
#                     "file_name": output_file,
#                     "file_url": file_url
#                 })

#             return JsonResponse({"files": file_urls}, status=200)

#         except Exception as e:
#             # Добавляем отладочное сообщение об ошибке
#             print(f"Ошибка: {str(e)}")
#             return JsonResponse({'error': str(e)}, status=500)
#     else:
#         return JsonResponse({'error': 'Неверный HTTP-метод'}, status=405)


# def download_output(request):
#     file_name = request.GET.get('file_name', '')
#     file_path = os.path.join(BASE_DIR, 'main', 'output', file_name)
#     if os.path.exists(file_path):
#         with open(file_path, 'rb') as f:
#             response = HttpResponse(f.read(), content_type='text/csv')
#             response['Content-Disposition'] = f'attachment; filename={file_name}'
#             return response
#     else:
#         return JsonResponse({'error': 'File not found'}, status=404)







from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import TitleForm
from io import BytesIO
import pandas as pd
import joblib
import difflib
import json
import os
import zipfile
from django.views.decorators.csrf import csrf_exempt

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(BASE_DIR, 'main', 'data', 'clean.csv')

if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    titles = df['Наименование'].tolist()
else:
    raise FileNotFoundError(f"File not found: {file_path}")

vectorizer = joblib.load(os.path.join(BASE_DIR, 'main', 'knnV2', 'tfidf_vectorizer.pkl'))
knn = joblib.load(os.path.join(BASE_DIR, 'main', 'knnV2', 'knn_model.pkl'))

def predict_similar_titles_with_distances(input_title, titles, vectorizer, knn):
    closest_matches = difflib.get_close_matches(input_title, titles, cutoff=0.65)
    if closest_matches:
        input_title = closest_matches[0]
    input_vec = vectorizer.transform([input_title])
    distances, indices = knn.kneighbors(input_vec)
    most_probable_title = titles[indices[0][0]]
    distance = distances[0][0]
    return most_probable_title, distance

def index(request):
    return render(request, 'index.html')

def classify_title(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            input_title = data.get('input', '')

            if not input_title:
                return JsonResponse({'error': 'No input title provided'}, status=400)
            
            most_probable_title, distance = predict_similar_titles_with_distances(input_title, titles, vectorizer, knn)

            код_ресурса = df[df['Наименование'] == most_probable_title]['Код ресурса'].values
            if len(код_ресурса) > 0:
                код_ресурса = код_ресурса[0]
                score = (1 - distance) * 100
                result = {
                    'код_ресурса': код_ресурса,
                    'title': most_probable_title,
                    'score': f"{score:.2f}"
                }
            else:
                result = {
                    'код_ресурса': None,
                    'title': most_probable_title,
                    'score': 'Не найден код ресурса для заголовка'
                }

            return JsonResponse({'result': result})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        output_files = []

        try:
            for uploaded_file in request.FILES.getlist('file'):
                df_to_update = pd.read_csv(uploaded_file)

                for index, row in df_to_update.iterrows():
                    input_title = row['name']
                    most_probable_title, distance = predict_similar_titles_with_distances(input_title, titles, vectorizer, knn)

                    print(distance)
                    print(knn.n_neighbors)
                    
                    if distance < knn.n_neighbors:
                        code = df[df['Наименование'] == most_probable_title]['Код ресурса'].values
                        if len(code) > 0:
                            code = code[0]
                            df_to_update.at[index, 'КСР наименование'] = most_probable_title
                            df_to_update.at[index, 'КСР код'] = code
                        else:
                            print(f"Не найден код ресурса для заголовка: {most_probable_title}")
                    else:
                        print("Такого ресурса нет")

                output_filename = f"output_{len(output_files) + 1}.csv"
                output_path = os.path.join(BASE_DIR, 'main', 'output', output_filename)
                df_to_update.to_csv(output_path, index=False)
                output_files.append(output_filename)

            # Создаем ссылки для скачивания файлов
            file_urls = []
            for output_file in output_files:
                file_url = request.build_absolute_uri(f'/download/?file_name={output_file}')
                file_urls.append({
                    "file_name": output_file,
                    "file_url": file_url
                })

            # Создаем ZIP-файл со всеми выходными файлами
            zip_filename = "ALL.zip"
            zip_path = os.path.join(BASE_DIR, 'main', 'output', zip_filename)
            with zipfile.ZipFile(zip_path, 'w') as zipf:
                for file in output_files:
                    zipf.write(os.path.join(BASE_DIR, 'main', 'output', file), arcname=file)
            
            zip_url = request.build_absolute_uri(f'/download/?file_name={zip_filename}')
            file_urls.append({
                "file_name": "all",
                "file_url": zip_url
            })
            print(zip_url)

            return JsonResponse({"files": file_urls}, status=200)

        except Exception as e:
            # Добавляем отладочное сообщение об ошибке
            print(f"Ошибка: {str(e)}")
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Неверный HTTP-метод'}, status=405)

def download_output(request):
    file_name = request.GET.get('file_name', '')
    file_path = os.path.join(BASE_DIR, 'main', 'output', file_name)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/zip' if file_name.endswith('.zip') else 'text/csv')
            response['Content-Disposition'] = f'attachment; filename={file_name}'
            return response
    else:
        return JsonResponse({'error': 'File not found'}, status=404)
