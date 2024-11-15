import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

data = pd.read_csv("movies.csv")

data['genre'] = data['genre'].astype('category').cat.codes

features = data[['genre', 'year', 'rating', 'duration']]
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

model = NearestNeighbors(n_neighbors=5, algorithm='auto')
model.fit(features_scaled)

historial_recomendaciones = []

def recommend_movie(movie_title):
    if movie_title not in data['title'].values:
        return " La Película no fue encontrada en el conjunto de datos ☹."
    
    
    movie_index = data[data['title'] == movie_title].index[0]
    
    
    distances, indices = model.kneighbors([features_scaled[movie_index]])
    recommended_titles = data.iloc[indices[0][1:]]['title'].tolist()
    
    
    historial_recomendaciones.append(recommended_titles)
    
    return recommended_titles


def ver_historial():
    print("\nHistorial de recomendaciones:")
    if historial_recomendaciones:
        for idx, recomendaciones in enumerate(historial_recomendaciones, 1):
            print(f"{idx}. {recomendaciones}")
    else:
        print("No hay recomendaciones en el historial ☹.")


def deshacer_recomendacion():
    if historial_recomendaciones:
        historial_recomendaciones.pop()
        print("\nÚltima recomendación eliminada del historial.")
    else:
        print("\nNo hay recomendaciones para deshacer.")


while True:
    print("\nOpciones♡:")
    print("1. Obtener recomendaciones")
    print("2. Ver historial de recomendaciones")
    print("3. Deshacer última recomendación")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        movie = input("Ingresa el título de una película que le guste: ")
        recommended_movies = recommend_movie(movie)
        if isinstance(recommended_movies, list):
            print("Películas recomendadas:", recommended_movies)
        else:
            print(recommended_movies)
    
    elif opcion == '2':
        ver_historial()
    
    elif opcion == '3':
        deshacer_recomendacion()
    
    elif opcion == '4':
        print("Saliendo del programa.")
        break
    
    else:
        print("Opción no válida. Intente de nuevo.")
