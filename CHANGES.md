# CHANGES.md

## 🔧 Overview

This document outlines the changes made to refactor and improve the legacy user management API codebase. The goal was to improve code quality, maintainability, security, and organization — while preserving original functionality.

---

## ✅ Major Issues Identified

- All route logic was crammed into a single file (`app.py`), violating separation of concerns.
- No password hashing or security measures for login.
- No email uniqueness checks or proper data validation.
- Missing testability — code was not structured for unit testing.
- No project structure or modularity (models, routes, utils, config were all mixed).
- No documentation or usage instructions.

---

## ✨ Changes Made

### 📦 Codebase Structure
- Separated logic into modules:
  - `routes.py` → API routes
  - `models.py` → SQLAlchemy models
  - `utils.py` → Password hashing
  - `config.py` → Environment-based DB config
  - `database.py` → Flask app + db init function
- Implemented `init_app()` for reusable app creation.

### 🔒 Security
- Passwords are now hashed using `werkzeug.security.generate_password_hash`.
- Login verifies hashed passwords securely.
- Prevents registration with duplicate emails.

### 💡 Best Practices
- Added error handling and HTTP status codes for every route.
- Ensured all API responses follow a consistent format (`jsonify`).
- Used `Blueprint` for modular route registration.
- Added default `sqlite:///users.db` for local dev, with `DATABASE_URL` env support.

### 🧪 Testing
- Wrote unit tests using `unittest` and Flask test client:
  - User creation
  - Login (success/failure)
  - Search
  - Fetching users

---

## 📝 Trade-offs & Assumptions

- Did not use Marshmallow or Pydantic for validation to keep things minimal.
- In-memory SQLite was used for simplicity; production should use PostgreSQL or similar.
- Login returns basic success/failure without session/token handling (as per task scope).

---

## 🤖 AI Usage Declaration

- Used **ChatGPT (OpenAI)** for:
  - Planning project structure
  - Getting secure password hashing methods
  - Writing test case templates
- All code was reviewed, understood, and modified manually.

---
