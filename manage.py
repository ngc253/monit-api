from app import create_app
from extensions import db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@app.after_request
def after_request(response):
    # Enable CORS
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = \
        'Accept, Content-Type, Origin, X-Requested-With'
    response.headers['Access-Control-Allow-Methods'] = \
        'GET, POST, PUT, OPTIONS, DELETE'
    return response


if __name__ == "__main__":
    manager.run()