




from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from datetime import datetime

app = Flask(__name__)
api = Api(app)

# Data awal film
movies = {
    "1": {
        "title": "Inception",
        "genre": "Science Fiction",
        "year": 2010,
        "director": "Christopher Nolan",
        "cast": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Ellen Page"],
        "synopsis": "A thief who steals corporate secrets through dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.",
        "rating": 8.8,
        "createdAt": "2024-01-01T00:00:00.000Z",
        "updatedAt": "2024-01-01T00:00:00.000Z"
    },
    "2": {
        "title": "The Dark Knight",
        "genre": "Action",
        "year": 2008,
        "director": "Christopher Nolan",
        "cast": ["Christian Bale", "Heath Ledger", "Aaron Eckhart"],
        "synopsis": "Batman faces the Joker, a criminal mastermind who wants to plunge Gotham City into anarchy.",
        "rating": 9.0,
        "createdAt": "2024-01-02T00:00:00.000Z",
        "updatedAt": "2024-01-02T00:00:00.000Z"
    },
  "3":{
    "_id": "507f191e810c19729de860ec",
    "title": "Interstellar",
    "genre": "Adventure",
    "year": 2014,
    "director": "Christopher Nolan",
    "cast": ["Matthew McConaughey", "Anne Hathaway", "Jessica Chastain"],
    "synopsis": "A team of explorers travel through a wormhole in space to ensure humanity's survival.",
    "rating": 8.6,
    "createdAt": "2024-01-03T00:00:00.000Z",
    "updatedAt": "2024-01-03T00:00:00.000Z"
  },
  "4": {
    "_id": "507f191e810c19729de860ed",
    "title": "Parasite",
    "genre": "Thriller",
    "year": 2019,
    "director": "Bong Joon-ho",
    "cast": ["Song Kang-ho", "Lee Sun-kyun", "Cho Yeo-jeong"],
    "synopsis": "A poor family schemes to become employed by a wealthy family and infiltrate their household.",
    "rating": 8.6,
    "createdAt": "2024-01-04T00:00:00.000Z",
    "updatedAt": "2024-01-04T00:00:00.000Z"
  },
  "5":{
    "_id": "507f191e810c19729de860ee",
    "title": "The Shawshank Redemption",
    "genre": "Drama",
    "year": 1994,
    "director": "Frank Darabont",
    "cast": ["Tim Robbins", "Morgan Freeman"],
    "synopsis": "Two imprisoned men bond over years, finding solace and eventual redemption through acts of common decency.",
    "rating": 9.3,
    "createdAt": "2024-01-05T00:00:00.000Z",
    "updatedAt": "2024-01-05T00:00:00.000Z"
  },
  "6":{
    "_id": "507f191e810c19729de860ef",
    "title": "Pulp Fiction",
    "genre": "Crime",
    "year": 1994,
    "director": "Quentin Tarantino",
    "cast": ["John Travolta", "Uma Thurman", "Samuel L. Jackson"],
    "synopsis": "The lives of two mob hitmen, a boxer, a gangster and his wife intertwine in four tales of violence and redemption.",
    "rating": 8.9,
    "createdAt": "2024-01-06T00:00:00.000Z",
    "updatedAt": "2024-01-06T00:00:00.000Z"
  },
  "7":{
    "_id": "507f191e810c19729de860f0",
    "title": "Fight Club",
    "genre": "Drama",
    "year": 1999,
    "director": "David Fincher",
    "cast": ["Brad Pitt", "Edward Norton", "Helena Bonham Carter"],
    "synopsis": "An insomniac office worker and a soap salesman form an underground fight club.",
    "rating": 8.8,
    "createdAt": "2024-01-07T00:00:00.000Z",
    "updatedAt": "2024-01-07T00:00:00.000Z"
  },
  "8": {
    "_id": "507f191e810c19729de860f1",
    "title": "Forrest Gump",
    "genre": "Drama",
    "year": 1994,
    "director": "Robert Zemeckis",
    "cast": ["Tom Hanks", "Robin Wright"],
    "synopsis": "The story of a slow-witted but kind-hearted man from Alabama who witnesses and influences several historical events.",
    "rating": 8.8,
    "createdAt": "2024-01-08T00:00:00.000Z",
    "updatedAt": "2024-01-08T00:00:00.000Z"
  },
  "9":{
    "_id": "507f191e810c19729de860f2",
    "title": "The Dark Knight",
    "genre": "Action",
    "year": 2008,
    "director": "Christopher Nolan",
    "cast": ["Christian Bale", "Heath Ledger", "Aaron Eckhart"],
    "synopsis": "When the menace known as the Joker emerges from his mysterious past, he wreaks havoc on Gotham.",
    "rating": 9.0,
    "createdAt": "2024-01-09T00:00:00.000Z",
    "updatedAt": "2024-01-09T00:00:00.000Z"
  },
  "10":{
    "_id": "507f191e810c19729de860f3",
    "title": "The Godfather",
    "genre": "Crime",
    "year": 1972,
    "director": "Francis Ford Coppola",
    "cast": ["Marlon Brando", "Al Pacino", "James Caan"],
    "synopsis": "The aging patriarch of an organized crime dynasty transfers control of his empire to his reluctant son.",
    "rating": 9.2,
    "createdAt": "2024-01-10T00:00:00.000Z",
    "updatedAt": "2024-01-10T00:00:00.000Z"
  },
  "11":{
    "_id": "507f191e810c19729de860f4",
    "title": "Schindler's List",
    "genre": "Biography",
    "year": 1993,
    "director": "Steven Spielberg",
    "cast": ["Liam Neeson", "Ben Kingsley", "Ralph Fiennes"],
    "synopsis": "In German-occupied Poland, Oskar Schindler becomes concerned for his Jewish workforce after witnessing their persecution.",
    "rating": 9.0,
    "createdAt": "2024-01-11T00:00:00.000Z",
    "updatedAt": "2024-01-11T00:00:00.000Z"
  },
  "12":{
    "_id": "507f191e810c19729de860f5",
    "title": "The Lord of the Rings: The Return of the King",
    "genre": "Fantasy",
    "year": 2003,
    "director": "Peter Jackson",
    "cast": ["Elijah Wood", "Viggo Mortensen", "Ian McKellen"],
    "synopsis": "Gandalf and Aragorn lead the World of Men against Sauron's army to draw his gaze from Frodo and Sam as they approach Mount Doom with the One Ring.",
    "rating": 8.9,
    "createdAt": "2024-01-12T00:00:00.000Z",
    "updatedAt": "2024-01-12T00:00:00.000Z"
  }
]
}

class MovieList(Resource):
    def get(self):
        return jsonify(movies)

class Movie(Resource):
    def get(self, movie_id):
        movie = movies.get(movie_id)
        if movie:
            return jsonify(movie)
        else:
            return jsonify({"message": "Movie not found"}), 404

    def post(self, movie_id):
        if movie_id in movies:
            return jsonify({"message": "Movie with this ID already exists"}), 400

        data = request.get_json()
        new_movie = {
            "title": data["title"],
            "genre": data["genre"],
            "year": data["year"],
            "director": data["director"],
            "cast": data["cast"],
            "synopsis": data["synopsis"],
            "rating": data["rating"],
            "createdAt": datetime.utcnow().isoformat() + "Z",
            "updatedAt": datetime.utcnow().isoformat() + "Z"
        }
        movies[movie_id] = new_movie
        return jsonify({"message": "Movie added", "movie": new_movie}), 201

    def put(self, movie_id):
        data = request.get_json()
        movie = movies.get(movie_id)
        if movie:
            movie.update({
                "title": data.get("title", movie["title"]),
                "genre": data.get("genre", movie["genre"]),
                "year": data.get("year", movie["year"]),
                "director": data.get("director", movie["director"]),
                "cast": data.get("cast", movie["cast"]),
                "synopsis": data.get("synopsis", movie["synopsis"]),
                "rating": data.get("rating", movie["rating"]),
                "updatedAt": datetime.utcnow().isoformat() + "Z"
            })
            return jsonify({"message": "Movie updated", "movie": movie})
        else:
            return jsonify({"message": "Movie not found"}), 404

    def delete(self, movie_id):
        if movie_id in movies:
            deleted_movie = movies.pop(movie_id)
            return jsonify({"message": "Movie deleted", "movie": deleted_movie})
        else:
            return jsonify({"message": "Movie not found"}), 404

# Registering endpoints
api.add_resource(MovieList, '/api/movies')
api.add_resource(Movie, '/api/movies/<movie_id>')

if __name__ == '__main__':
    app.run(debug=True)
