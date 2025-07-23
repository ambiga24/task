import React, { useEffect, useState } from "react";
import { fetchMovies } from "../services/api";

function MovieList() {
  const [movies, setMovies] = useState([]);

  useEffect(() => {
    fetchMovies().then(setMovies);
  }, []);

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold">Movies</h1>
      {movies.map(movie => (
        <div key={movie.id} className="border p-2 my-2">
          <h2>{movie.title} ({movie.release_year})</h2>
          <p>Director: {movie.director}</p>
          <p>Genres: {movie.genres.join(", ")}</p>
        </div>
      ))}
    </div>
  );
}

export default MovieList;
