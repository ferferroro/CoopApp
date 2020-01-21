from main import app, db
import config

if __name__ == '__main__':
    # load the configurations
    app.config.from_object('config.DevConfig')
    app.run(debug=True)