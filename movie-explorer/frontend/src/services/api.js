import axios from "axios";

const API_BASE = "http://localhost:8000/api";

export const fetchMovies = async (filters = {}) => {
  const params = new URLSearchParams(filters).toString();
  const response = await axios.get(`${API_BASE}/movies?${params}`);
  return response.data;
};
