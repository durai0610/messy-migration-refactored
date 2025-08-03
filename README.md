# 🧩 User Management API — Refactored

A refactored version of a legacy user management API, using Flask, SQLAlchemy, and modular best practices.

---

## ⚙️ Setup Instructions

### 📦 Prerequisites
- Python 3.8+
- pip (Python package manager)

### 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/your-username/your-repo.git
cd messy-migration-refactored

# Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Initialize the database with test users
python init_db.py

# Run the app
python app.py
```

🔌 API Endpoints

| Method | Endpoint           | Description              |
|--------|--------------------|--------------------------|
| GET    | `/`                | Health check             |
| GET    | `/users`           | Get all users            |
| GET    | `/user/<id>`       | Get user by ID           |
| POST   | `/users`           | Create a new user        |
| PUT    | `/user/<id>`       | Update existing user     |
| DELETE | `/user/<id>`       | Delete user              |
| GET    | `/search?name=...` | Search users by name     |
| POST   | `/login`           | Authenticate user        |

---

📁 Project Structure

```
messy-migration-refactored/
├── app.py                  # App entrypoint
├── routes.py               # All API routes
├── models.py               # SQLAlchemy User model
├── utils.py                # Password hashing utils
├── config.py               # Config for DB connection
├── database.py             # init_app() + db setup
├── init_db.py              # Seeds DB with test users
├── test_app.py             # Unit tests
├── requirements.txt        # Python deps
├── README.md               # You're here
└── CHANGES.md              # Refactoring summary
```

---

🧪 Running Tests

```bash
python test_app.py
```
---

🤖 AI Usage Declaration

ChatGPT was used for suggestions on password hashing, structure, and writing tests.

All code was written manually and verified.

---

