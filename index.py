from flask import Flask, jsonify
# from flask_restful import Api, Resource
# from datetime import datetime

app = Flask(__name__)
# api = Api(app)

# Define a simple GET endpoint
@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, World!"})

# For Vercel to recognize the app
from api.index import app as application
# Data awal film
# movies = {
#     "1": {
#         "title": "Inception",
#         "genre": "Science Fiction",
#         "year": 2010,
#         "director": "Christopher Nolan",
#         "cast": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Ellen Page"],
#         "synopsis": "A thief who steals corporate secrets through dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.",
#         "rating": 8.8,
#         "createdAt": "2024-01-01T00:00:00.000Z",
#         "updatedAt": "2024-01-01T00:00:00.000Z"
#     },
#     "2": {
#         "title": "The Dark Knight",
#         "genre": "Action",
#         "year": 2008,
#         "director": "Christopher Nolan",
#         "cast": ["Christian Bale", "Heath Ledger", "Aaron Eckhart"],
#         "synopsis": "Batman faces the Joker, a criminal mastermind who wants to plunge Gotham City into anarchy.",
#         "rating": 9.0,
#         "createdAt": "2024-01-02T00:00:00.000Z",
#         "updatedAt": "2024-01-02T00:00:00.000Z"
#     }
#     # Tambahkan data film lainnya sesuai kebutuhan
# }

# class MovieList(Resource):
#     def get(self):
#         return jsonify(movies)

# class Movie(Resource):
#     def get(self, movie_id):
#         movie = movies.get(movie_id)
#         if movie:
#             return jsonify(movie)
#         else:
#             return jsonify({"message": "Movie not found"}), 404

#     def post(self, movie_id):
#         if movie_id in movies:
#             return jsonify({"message": "Movie with this ID already exists"}), 400
        
#         data = request.get_json()
#         # Validasi input
#         if not data or not all(k in data for k in ("title", "genre", "year", "director", "cast", "synopsis", "rating")):
#             return jsonify({"message": "Invalid input, all fields are required"}), 400

#         new_movie = {
#             "title": data["title"],
#             "genre": data["genre"],
#             "year": data["year"],
#             "director": data["director"],
#             "cast": data["cast"],
#             "synopsis": data["synopsis"],
#             "rating": data["rating"],
#             "createdAt": datetime.utcnow().isoformat() + "Z",
#             "updatedAt": datetime.utcnow().isoformat() + "Z"
#         }
#         movies[movie_id] = new_movie
#         return jsonify({"message": "Movie added", "movie": new_movie}), 201

#     def put(self, movie_id):
#         data = request.get_json()
#         movie = movies.get(movie_id)
#         if movie:
#             movie.update({
#                 "title": data.get("title", movie["title"]),
#                 "genre": data.get("genre", movie["genre"]),
#                 "year": data.get("year", movie["year"]),
#                 "director": data.get("director", movie["director"]),
#                 "cast": data.get("cast", movie["cast"]),
#                 "synopsis": data.get("synopsis", movie["synopsis"]),
#                 "rating": data.get("rating", movie["rating"]),
#                 "updatedAt": datetime.utcnow().isoformat() + "Z"
#             })
#             return jsonify({"message": "Movie updated", "movie": movie})
#         else:
#             return jsonify({"message": "Movie not found"}), 404

#     def delete(self, movie_id):
#         if movie_id in movies:
#             deleted_movie = movies.pop(movie_id)
#             return jsonify({"message": "Movie deleted", "movie": deleted_movie})
#         else:
#             return jsonify({"message": "Movie not found"}), 404

# # Registering endpoints
# api.add_resource(MovieList, '/api/movies')
# api.add_resource(Movie, '/api/movies/<movie_id>')

# if __name__ == '__main__':
#     app.run(debug=True)
