from database import init_app, db
from models import User
from utils import hash_password

app = init_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    users = [
        User(name="John Doe", email="john@example.com", password=hash_password("password123")),
        User(name="Jane Smith", email="jane@example.com", password=hash_password("secret456")),
        User(name="Bob Johnson", email="bob@example.com", password=hash_password("qwerty789")),
    ]
    db.session.bulk_save_objects(users)
    db.session.commit()

print("Database initialized with sample users.")
