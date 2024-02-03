# FastAPI DDD Implementation Template

## Introduction

This repository contains an implementation of a FastAPI application following Domain-Driven Design (DDD) principles. The goal is to provide a structured and scalable architecture for building web applications with a focus on business domain logic.

## Project Structure

The project is organized into distinct modules following DDD concepts:

- **app/**: The main FastAPI application.
    - **deps/**: Dependencies.
    - **domain/**: Domain logic.
    - **infrastructure/**: Infrastructure-related code (e.g., adapters, repositories).
    - **routes/**: FastAPI routers.
    - **services/**: Application services orchestrating domain logic.
- **tests/**: Unit tests for the application.

## Getting Started

### Prerequisites

- Python 3.10+
- FastAPI 0.104+
- Kafka 1.3+
- [Poetry](https://python-poetry.org/)
