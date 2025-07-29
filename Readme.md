# 🎬 Movie Explorer App

A full-stack movie database web application to explore, filter, and view details about movies, actors, and directors. Built with **Golang (Gin)** for the backend and optionally React or any frontend of your choice. This app allows users to browse movies by genre, view actor profiles, and explore movie data interactively.

---

## 🚀 Features

### 🔍 Advanced Movie Filtering
- Search and filter movies based on:
  - **Genre**
  - **Actor**
  - **Director**
  - **Release Year**
- Backend-powered filtering using efficient database queries (no client-side filtering).

### 👤 Actor & Director Profiles
- View individual actor and director pages.
- Explore all movies associated with a specific actor or director.

### 🧪 Testing & Code Quality
- Unit tests included to ensure backend functionality.
- Code is linted to follow clean and consistent style.

### 📦 Dockerized Setup
- Easily set up the app using Docker and Docker Compose:
  ```bash
  docker-compose up --build

### Tech Stack
- Backend: Golang (Gin framework), GORM

- Database: PostgreSQL or MySQL

- Documentation: Swagger (OpenAPI)

- Containerization: Docker & Docker Compose

- Frontend (optional): HTML/CSS/JS, React, or your preferred framework

### Running Tests

- go test ./...
- golangci-lint run

### API Examples
Example endpoints:

- GET /movies?genre=Action&year=2020

- GET /actors/:id

- GET /directors/:id

- Swagger UI can be accessed at: (http://localhost:8080/swagger/index.html)