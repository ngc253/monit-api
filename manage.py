from flask_cors import CORS

from src.app import create_app
from src.extensions import db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

CORS(app)

if __name__ == "__main__":
    manager.run()
