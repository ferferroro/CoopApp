from main import app, db
import config

# load the configurations
app.config.from_object('config.HerokuProdConfig')

if __name__ == '__main__':
    app.run()