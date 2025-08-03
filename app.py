from database import init_app, db
from routes import api
from models import User

app = init_app()
app.register_blueprint(api)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
