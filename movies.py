from fastapi import FastAPI
from fastapi import HTTPException, status
from fastapi import Response
from models import Movie

app = FastAPI()


@app.get('/')
async def root():
    return {"msg": "Popular Movies"}


movies = {
    1: {
        "name": "Barbie",
        "assessment": 73,
        "genre": "Comedy, Adventure, Fantasy",
        "runtime": "1h 52m",
        "phrase": "She's everything. He's just Ken."
    },
    2: {
        "name": "Meg 2: The Trench",
        "assessment": 70,
        "genre": "Action, Science Fiction, Horror",
        "runtime": "1h 56m",
        "phrase": "Back for seconds."
    },
    3: {
        "name": "Fast X",
        "assessment": 73,
        "genre": "Action, Crime, Thriller",
        "runtime": "2h 22m",
        "phrase": "The end of the road begins."
        },
    4: {
        "name": "The Nun II",
        "assessment": 67,
        "genre": "Horror, Mystery, Thriller",
        "runtime": "1h 50m",
        "phrase": "The greatest evil in the Conjuring universe."
        },
    5: {
        "name": "Talk to Me",
        "assessment": 73,
        "genre": "Horror, Thriller",
        "runtime": "1h 35m",
        "phrase": "You call. They'll answer."
    },

}


@app.get('/movies')
async def get_movies():
    return movies


@app.get('/movies/{movie_id}')
async def get_movie(movie_id: int):
    try:
        movie = movies[movie_id]
        movie.update({"id": movie_id})
        return movie
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Movie not found')


@app.post('/movies')
async def post_movie(movie: Movie):
    movie.id = sorted(movies.keys())[-1] + 1  # trazendo o ultumo item da lista
    movies[movie.id] = movie
    return movie
    # else:
    #     raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Já existe um curso com o ID {curso.id}")


@app.put('/movies/{movie_id}')
async def put_movie(movie_id: int, movie: Movie):
    if movie_id in movies:
        movie_id = movie_id
        movies[movie_id] = movie
        return movie
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='This film does not exist.')


@app.delete('/movies/{movie_id}')
async def delete_curso(movie_id: int):
    if movie_id in movies:
        del movies[movie_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='This film does not exist.')


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("movies:app", host='127.0.0.1', port=8001, log_level="info", reload=True)
