import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

BASE_PATH = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.update(
    SQLALCHEMY_DATABASE_URI=f"sqlite:///{os.path.join(BASE_PATH, 'BigBang.db')}",
    SECRET_KEY=os.urandom(16).hex()
)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "LoginPage"
login_manager.login_message_category = "info"


def _patch_table(tablename, column, definition):
    try:
        with db.engine.begin() as link:
            meta = link.execute(db.text(f"PRAGMA table_info('{tablename}')")).fetchall()
            exists = any(entry[1] == column for entry in meta)
            if not exists:
                link.execute(db.text(f"ALTER TABLE {tablename} ADD COLUMN {column} {definition}"))
    except Exception:
        pass


def _sync_user_admin():
    _patch_table("user", "is_admin", "BOOLEAN NOT NULL DEFAULT 0")


def _sync_item_image():
    _patch_table("item", "image_url", "VARCHAR(255)")


def _sync_item_barcode():
    _patch_table("item", "barcode", "VARCHAR(50)")


with app.app_context():
    try:
        db.create_all()
        _sync_user_admin()
        _sync_item_image()
        _sync_item_barcode()
    except Exception:
        pass


@app.before_request
def run_table_sync():
    try:
        _sync_user_admin()
        _sync_item_image()
        _sync_item_barcode()
    except Exception:
        pass


from Market import routes
from Market import models
