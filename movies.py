from fastapi import FastAPI, HTTPException
from models import Movie
import httpx

app = FastAPI()

TMDB_API_KEY = "ce9f9a5ac2996664f3f3c33003234fc5"


@app.get('/')
async def raiz():
    return {"msg": "Movies API"}


@app.get('/popular-movies')
async def popular_movies():
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

        if response.status_code == 200:
            data = response.json()
            movies = []

            for movie in data.get('results', []):
                popular_movie = Movie(
                    id=movie.get('id'),
                    title=movie.get('title'),
                    overview=movie.get('overview'),
                )
                movies.append(popular_movie)

            return movies
        else:
            raise HTTPException(status_code=response.status_code, detail="Movies not found")


@app.get('/popular-movies/{movie_id}')
async def get_movie(movie_id: int):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

        if response.status_code == 200:
            movies = response.json()
            return {
                "id": movies.get('id'),
                "title": movies.get('title'),
                "overview": movies.get('overview'),
            }
        else:
            raise HTTPException(status_code=response.status_code, detail="Movie not found")


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("movies:app", host='127.0.0.1', port=8000, log_level="info", reload=True)
