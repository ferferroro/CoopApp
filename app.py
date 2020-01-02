from main import app, db
from main.models import user
# from flask_migrate import Migrate

# migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)