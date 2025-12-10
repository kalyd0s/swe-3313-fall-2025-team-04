from Market import db, bcrypt, login_manager
from flask_login import UserMixin
from sqlalchemy.orm import backref
from datetime import datetime
import pytz

_est = pytz.timezone("US/Eastern")

def _format_currency(amount: int) -> str:
    stringified = str(amount)
    length_check = len(stringified)

    if length_check <= 3:
        result = f"{stringified} $"
    else:
        split_point = length_check - 3
        left_portion = stringified[:split_point]
        right_portion = stringified[split_point:]
        result = f"{left_portion},{right_portion} $"

    return result

def _encode_password(plain: str) -> str:
    hashed_bytes = bcrypt.generate_password_hash(plain)
    decoded_string = hashed_bytes.decode("utf-8")
    return decoded_string

def _verify_password(stored_hash: str, attempt: str) -> bool:
    verification_result = bcrypt.check_password_hash(stored_hash, attempt)
    return verification_result

class _DeleteMixin:

    @classmethod
    def _delete_by_id(cls, ident: int) -> bool:
        query_result = cls.query.filter_by(id=ident)
        found_object = query_result.first()

        success = False
        if found_object is not None:
            db.session.delete(found_object)
            db.session.commit()
            success = True

        return success

@login_manager.user_loader
def load_user(user_id):
    parsed_id = int(user_id)
    user_object = User.query.get(parsed_id)
    return user_object


class User(db.Model, UserMixin, _DeleteMixin):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email_address = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(60), nullable=False)
    budget = db.Column(db.Integer, default=10000, nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)

    items = db.relationship(
        "Item",
        backref="owned_user",
        lazy=True
    )
    cart_items = db.relationship(
        "CartItem",
        backref=backref("user", lazy=True),
        lazy=True,
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        username_repr = repr(self.username)
        return f"<User username={username_repr}>"

    @property
    def prettier_budget(self):
        current_budget = self.budget
        formatted = _format_currency(current_budget)
        return formatted

    @property
    def password(self):
        stored_hash = self.password_hash
        return stored_hash

    @password.setter
    def password(self, plain_text_password):
        encoded_hash = _encode_password(plain_text_password)
        self.password_hash = encoded_hash

    def password_check(self, password_attempt):
        current_hash = self.password_hash
        is_valid = _verify_password(current_hash, password_attempt)
        return is_valid

    def can_purchase(self, item_obj):
        item_cost = getattr(item_obj, "price", 0)
        user_funds = self.budget
        has_enough = user_funds >= item_cost
        return has_enough

    def can_sell(self, item_obj):
        owned_items = self.items
        is_owned = item_obj in owned_items
        return is_owned

    @staticmethod
    def delete_user(user_id):
        deletion_result = User._delete_by_id(user_id)
        return deletion_result


class Item(db.Model, _DeleteMixin):
    __tablename__ = "item"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    barcode = db.Column(db.String(50), unique=True)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    image_url = db.Column(db.String(255))
    owner = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        name_repr = repr(self.name)
        return f"<Item name={name_repr}>"

    @property
    def prettier_price(self):
        item_price = self.price
        formatted_price = _format_currency(item_price)
        return formatted_price

    def _adjust_balance_and_commit(self, user, amount: int):
        current_budget = user.budget
        new_budget = current_budget + amount
        user.budget = new_budget
        db.session.commit()

    def buy(self, user):
        user_identifier = user.id
        self.owner = user_identifier
        item_cost = self.price
        negative_cost = -item_cost
        self._adjust_balance_and_commit(user, negative_cost)

    def sell(self, user):
        self.owner = None
        item_value = self.price
        self._adjust_balance_and_commit(user, item_value)

    @staticmethod
    def delete_item(item_id):
        deletion_result = Item._delete_by_id(item_id)
        return deletion_result

    def update_item(self, name, price, description, image_url=None):
        self.name = name
        self.price = price
        self.description = description

        if image_url is not None:
            self.image_url = image_url

        db.session.commit()


class CartItem(db.Model):
    __tablename__ = "cart_item"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey("item.id"), nullable=False, unique=True)

    item = db.relationship(
        "Item",
        backref=backref("cart_item", uselist=False)
    )

    def __repr__(self):
        uid = self.user_id
        iid = self.item_id
        return f"<CartItem user={uid} item={iid}>"


class SalesRecord(db.Model):
    __tablename__ = "sales_record"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    items_text = db.Column(db.String(2048))
    total = db.Column(db.Integer, nullable=False)
    shipping_cost = db.Column(db.Integer, nullable=False, default=0)
    tax = db.Column(db.Integer, nullable=False, default=0)

    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=lambda: datetime.now(_est)
    )

    user_email = db.Column(db.String(150))
    full_name = db.Column(db.String(150))

    def __repr__(self):
        record_id = self.id
        associated_user = self.user_id
        return f"<SalesRecord id={record_id} user={associated_user}>"
