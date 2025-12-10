from Market import app, db
from Market.models import Item, User, CartItem, SalesRecord
from Market.forms import (
    RegisterForm,
    LoginForm,
    AddToCartForm,
    RemoveFromCartForm,
    CheckoutForm,
    PromoteAdminForm,
    AdminItemForm,
)
from uuid import uuid4
from sqlalchemy import text

def _auto_barcode(name):
    return f"auto-{name}-{uuid4().hex[:6]}"
from flask import render_template, redirect, url_for, flash, request, session
from flask_login import login_user, logout_user, login_required, current_user

@app.route("/")
def HomePage():
    return redirect(url_for('LoginPage'))

@app.route("/market", methods=['GET', 'POST'])
@login_required
def MarketPage():
    try:
        from Market import _ensure_item_image_column
        _ensure_item_image_column()
    except Exception:
        pass
    planet_catalog = [
        {"name": "Mercury", "price": 100_000_000_000, "description": "The first of four inner terrestrial planets consisting of rock. The closest planet to the sun and the smallest planet in the solar system."},
        {"name": "Venus", "price": 120_000_000_000, "description": "Second planet from the sun. A rocky world cloaked in dense clouds and extreme heat, often called Earth’s twin in size."},
        {"name": "Earth", "price": 175_000_000_000, "description": "Our home planet and the only known world with liquid water oceans and life. A balanced terrestrial sphere with a protective atmosphere."},
        {"name": "Mars", "price": 140_000_000_000, "description": "The red planet, famous for its iron-rich dust, towering Olympus Mons volcano, and the Valles Marineris canyon system."},
        {"name": "Saturn", "price": 200_000_000_000, "description": "The second of the four outer planets. A gas giant that is the second largest planet in the solar system known for its rings."},
        {"name": "Jupiter", "price": 250_000_000_000, "description": "First of the four outer planets. A gas giant with the iconic 'Great Red Spot' known to be the largest planet in the solar system."},
        {"name": "Uranus", "price": 190_000_000_000, "description": "An ice giant tilted on its side with faint rings and a cold, methane-rich atmosphere that gives it a blue-green hue."},
        {"name": "Neptune", "price": 180_000_000_000, "description": "The last of the four outer planets and the most distant planet from the sun. An ice giant that is not visible to the naked eye."},
    ]
    planet_names = [p["name"] for p in planet_catalog]
    planet_images = {
        "mercury": "https://upload.wikimedia.org/wikipedia/commons/2/24/Transparent_Mercury.png",
        "venus": "https://upload.wikimedia.org/wikipedia/commons/8/85/Venus_globe.jpg",
        "earth": "https://upload.wikimedia.org/wikipedia/commons/9/97/The_Earth_seen_from_Apollo_17.jpg",
        "mars": "https://upload.wikimedia.org/wikipedia/commons/0/02/OSIRIS_Mars_true_color.jpg",
        "saturn": "https://www.nicepng.com/png/full/381-3811493_saturn-planet-ring-saturneye-space-saturn-planet-transparent.png",
        "jupiter": "https://pngimg.com/d/jupiter_PNG20.png",
        "uranus": "https://upload.wikimedia.org/wikipedia/commons/3/3d/Uranus2.jpg",
        "neptune": "https://upload.wikimedia.org/wikipedia/commons/7/7d/Transparent_Neptune.png",
        "default": "https://upload.wikimedia.org/wikipedia/commons/6/68/Solar_sys8.jpg",
    }
    def ensure_planet_inventory():
        # Ensure image_url column exists (sqlite migration)
        try:
            cols = db.engine.execute(db.text("PRAGMA table_info('item')")).fetchall()
            has_image = any(col[1] == 'image_url' for col in cols)
            if not has_image:
                db.engine.execute(db.text("ALTER TABLE item ADD COLUMN image_url VARCHAR(255)"))
        except Exception:
            pass
        # Remove auto-respawn of planets; only seed if DB empty
        if Item.query.count() == 0:
            for planet in planet_catalog:
                db.session.add(Item(
                    name=planet["name"],
                    barcode=_auto_barcode(planet["name"]),
                    price=planet["price"],
                    description=planet["description"],
                    image_url=planet_images.get(planet["name"].lower(), planet_images["default"])
                ))
            db.session.commit()
    ensure_planet_inventory()
    if request.method == "POST":
        item_obj = Item.query.filter_by(name=request.form.get('add_to_cart_item')).first()
        if item_obj:
            if item_obj.owner:
                flash(f"Sorry, {item_obj.name} has already been purchased.", category='danger')
            elif CartItem.query.filter_by(item_id=item_obj.id).first():
                flash(f"{item_obj.name} is already in another cart.", category='warning')
            else:
                db.session.add(CartItem(user_id=current_user.id, item_id=item_obj.id))
                db.session.commit()
                flash(f"{item_obj.name} was added to your cart.", category='success')
        else:
            flash("We couldn't find that item to add to your cart.", category='danger')
        return redirect(url_for('MarketPage'))
    
    if request.method == "GET":
        search_query = request.args.get('q', '').strip()
        carted_item_ids = db.session.query(CartItem.item_id).subquery()
        items_query = Item.query.filter(
            Item.owner.is_(None),
            ~Item.id.in_(carted_item_ids)
        )
        if search_query:
            terms = [t for t in search_query.split() if t]
            for term in terms:
                pattern = f"%{term}%"
                items_query = items_query.filter(
                    db.or_(
                        Item.description.ilike(pattern),
                        Item.name.ilike(pattern)
                    )
                )
        items = items_query.all()
        cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
        return render_template(
            'MARKET.html',
            title='Market',
            items=items,
            cart_items=cart_items,
            add_to_cart_form=AddToCartForm(),
            planet_images=planet_images,
            search_query=search_query
        )

@app.route("/register", methods=['GET', 'POST'])
def RegisterPage():
    form = RegisterForm()
    if form.validate_on_submit():
        create_user = User(username=form.username.data, email_address=form.email_address.data, password=form.password1.data)
        db.session.add(create_user)
        db.session.commit()
        login_user(create_user)
        flash(f'Account created successfully! You are now logged in as: {create_user.username}', category='success')
        return redirect(url_for('MarketPage'))
    
    if form.errors != {}:
        for error in form.errors.values():
            flash(f'There was an error with creating a user: {error}', category='danger')
    return render_template('REGISTER.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def LoginPage():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.password_check(password_attempt=form.password.data):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            if attempted_user.username == 'admin':
                return redirect(url_for('AdminPage'))
            return redirect(url_for('MarketPage'))
        flash('Username or password is incorrect! Please try again', category='danger')
    return render_template('LOGIN.html', title='Login', form=form)


@app.route("/admin")
@login_required
def AdminPage():
    if not (current_user.is_admin or current_user.username == 'admin'):
        flash('Please login as admin to access admin actions.', category='danger')
        return redirect(url_for('LoginPage'))
    return render_template('ADMIN_ACTIONS.html')

@app.route("/admin-actions")
@login_required
def AdminActionsPage():
    return redirect(url_for('AdminPage'))

@app.route("/admin-panel", methods=['GET', 'POST'])
@login_required
def AdminPanelPage():
    if not (current_user.is_admin or current_user.username=='admin'):
        flash('Please login as admin to access the admin panel!', category='danger')
        return redirect(url_for('LoginPage'))
    create_form = AdminItemForm()
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'create':
            if create_form.validate_on_submit():
                db.session.add(Item(
                    name=create_form.name.data,
                    barcode=_auto_barcode(create_form.name.data),
                    price=create_form.price.data,
                    description=create_form.description.data,
                    image_url=create_form.image_url.data
                ))
                db.session.commit()
                flash("Item created.", category='success')
                return redirect(url_for('AdminPanelPage'))
            flash("Please fix errors in the form.", category='danger')
        elif action == 'update':
            item_id = request.form.get('item_id')
            item = Item.query.get(item_id)
            if item:
                item.name = request.form.get('name', item.name)
                try:
                    item.price = int(request.form.get('price', item.price))
                except (TypeError, ValueError):
                    pass
                item.description = request.form.get('description', item.description)
                item.image_url = request.form.get('image_url', item.image_url)
                db.session.commit()
                flash("Item updated.", category='success')
                return redirect(url_for('AdminPanelPage'))
            flash("Item not found.", category='danger')
        elif action == 'delete':
            item_id = request.form.get('item_id')
            item = Item.query.get(item_id)
            if item:
                CartItem.query.filter_by(item_id=item.id).delete(synchronize_session=False)
                db.session.delete(item)
                db.session.commit()
                flash("Item deleted.", category='info')
                return redirect(url_for('AdminPanelPage'))
            flash("Item not found.", category='danger')
    return render_template('ADMIN.html', title='Admin', items=Item.query.all(), create_form=create_form)

@app.route("/admin/promote", methods=['GET', 'POST'])
@login_required
def PromoteAdminPage():
    if not (current_user.is_admin or current_user.username == 'admin'):
        flash('Please login as admin to access this page.', category='danger')
        return redirect(url_for('LoginPage'))
    form = PromoteAdminForm()
    promoted_user = None
    error_user = None
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            error_user = "User not found."
        else:
            user.is_admin = True
            db.session.commit()
            promoted_user = user.username
    return render_template('PROMOTE_ADMIN.html', form=form, promoted_user=promoted_user, error_user=error_user)

@app.route("/admin/sales-report")
@login_required
def SalesReportPage():
    if not (current_user.is_admin or current_user.username == 'admin'):
        flash('Please login as admin to access this page.', category='danger')
        return redirect(url_for('LoginPage'))
    records = SalesRecord.query.order_by(SalesRecord.created_at.desc()).all()
    total_orders = len(records)
    total_sales = sum(r.total for r in records)
    formatted_records = []
    for record in records:
        display_items = []
        if record.items_text:
            parts = [p for p in record.items_text.split(";") if p.strip()]
            for part in parts:
                name_val = part.split(":")
                if len(name_val) >= 2:
                    name = name_val[0].strip()
                    val_raw = ":".join(name_val[1:]).strip().lstrip("$")
                    val_raw = val_raw.rstrip("B").rstrip("b").strip()
                    try:
                        val_num = float(val_raw)
                        if val_num > 1_000_000:  # assume stored raw price
                            billions = val_num / 1_000_000_000
                        else:
                            billions = val_num
                        display_items.append(f"{name}: ${billions:.1f}B")
                    except ValueError:
                        display_items.append(part.strip())
                else:
                    display_items.append(part.strip())
        formatted_records.append("; ".join(display_items) if display_items else (record.items_text or "Order"))
    return render_template('SALES_REPORT.html', records=records, records_display=formatted_records, total_orders=total_orders, total_sales=total_sales)

@app.route("/admin/sales-report.csv")
@login_required
def SalesReportCSV():
    if not (current_user.is_admin or current_user.username == 'admin'):
        flash('Please login as admin to access this page.', category='danger')
        return redirect(url_for('LoginPage'))
    import csv
    from io import StringIO
    records = SalesRecord.query.order_by(SalesRecord.created_at.desc()).all()
    si = StringIO()
    writer = csv.writer(si)
    writer.writerow(["items", "total", "shipping_cost", "tax", "email", "created_at"])
    for r in records:
        writer.writerow([r.items_text or "", r.total, r.shipping_cost, r.tax, r.user_email or "", r.created_at])
    output = si.getvalue()
    headers = {
        "Content-Disposition": "attachment; filename=sales_report.csv",
        "Content-type": "text/csv"
    }
    return output, 200, headers

@app.route("/logout")
def LogoutPage():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for('LoginPage'))

@app.route("/cart", methods=['GET', 'POST'])
@login_required
def CartPage():
    remove_form = RemoveFromCartForm()
    if request.method == 'POST':
        item_id = request.form.get('remove_item_id')
        if item_id:
            cart_entry = CartItem.query.filter_by(user_id=current_user.id, item_id=item_id).first()
            if cart_entry:
                db.session.delete(cart_entry)
                db.session.commit()
                remaining_count = CartItem.query.filter_by(user_id=current_user.id).count()
                if remaining_count == 0:
                    flash("Your cart is now empty. Taking you back to the shop.", category='info')
                    return redirect(url_for('MarketPage'))
                flash("Item removed from your cart.", category='info')
        return redirect(url_for('CartPage'))
    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
    if not cart_items:
        flash("Your cart is empty. Add items from the shop to view your cart.", category='info')
        return redirect(url_for('MarketPage'))
    total_price = sum(cart_item.item.price for cart_item in cart_items if cart_item.item)
    planet_images = {
        "mercury": "https://upload.wikimedia.org/wikipedia/commons/2/24/Transparent_Mercury.png",
        "venus": "https://upload.wikimedia.org/wikipedia/commons/9/93/Venus_globe_-_transparent_background.png",
        "earth": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pngarts.com%2Fexplore%2F66026&psig=AOvVaw21Fc6e0JUeGldYCmP8s5q0&ust=1765405929178000&source=images&cd=vfe&opi=89978449&ved=0CBYQjRxqFwoTCNjTud7HsZEDFQAAAAAdAAAAABBH",
        "mars": "https://upload.wikimedia.org/wikipedia/commons/0/02/OSIRIS_Mars_true_color.jpg",
        "saturn": "https://www.nicepng.com/png/full/381-3811493_saturn-planet-ring-saturneye-space-saturn-planet-transparent.png",
        "jupiter": "https://pngimg.com/d/jupiter_PNG20.png",
        "uranus": "https://upload.wikimedia.org/wikipedia/commons/3/3d/Uranus2.jpg",
        "neptune": "https://upload.wikimedia.org/wikipedia/commons/7/7d/Transparent_Neptune.png",
        "default": "https://upload.wikimedia.org/wikipedia/commons/6/68/Solar_sys8.jpg",
    }
    return render_template('CART.html', title='Cart', cart_items=cart_items, remove_form=remove_form, total_price=total_price, planet_images=planet_images)

@app.route("/checkout", methods=['GET', 'POST'])
@login_required
def CheckoutPage():
    checkout_form = CheckoutForm()
    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
    if not cart_items:
        flash("Your cart is empty, add items before checking out.", category='info')
        return redirect(url_for('MarketPage'))
    total_price = sum(cart_item.item.price for cart_item in cart_items if cart_item.item)
    if checkout_form.validate_on_submit():
        shipping_map = {"overnight": 29, "three_day": 19, "ground": 0}
        shipping_choice = checkout_form.shipping_option.data or "ground"
        shipping_cost = shipping_map.get(shipping_choice, 0)
        subtotal = total_price
        tax_rate = 0.06
        tax_cost = int(subtotal * tax_rate)
        order_total = subtotal + tax_cost + shipping_cost
        order_summary = {
            "line_items": [{"name": c.item.name, "price": c.item.price} for c in cart_items if c.item],
            "shipping_label": shipping_choice,
            "shipping_cost": shipping_cost,
            "tax": tax_cost,
            "total": order_total,
            "full_name": checkout_form.full_name.data,
            "email": checkout_form.email.data,
            "address": f"{checkout_form.address1.data} {checkout_form.address2.data}".strip(),
            "zip_code": checkout_form.zip_code.data,
            "card_last4": (checkout_form.card_number.data or "")[-4:],
            "item_ids": [c.item.id for c in cart_items if c.item],
        }
        session['order_review'] = order_summary
        return redirect(url_for('ReviewOrderPage'))
    return render_template('CHECKOUT.html', title='Checkout', cart_items=cart_items, checkout_form=checkout_form, total_price=total_price)

@app.route("/review-order", methods=['GET', 'POST'])
@login_required
def ReviewOrderPage():
    order = session.get('order_review')
    if not order:
        flash("No order to review. Please complete checkout first.", category='info')
        return redirect(url_for('CheckoutPage'))
    if request.method == 'POST':
        item_ids = order.get('item_ids', [])
        cart_entries = CartItem.query.filter_by(user_id=current_user.id).all()
        for entry in cart_entries:
            if entry.item_id in item_ids:
                db.session.delete(entry)
        db.session.commit()
        # save sales record
        record = SalesRecord(
            user_id=current_user.id,
            items_text="; ".join([f"{i['name']}: ${'%.1f' % (i['price'] / 1000000000)}B" for i in order.get('line_items', [])]),
            total=order.get('total', 0),
            shipping_cost=order.get('shipping_cost', 0),
            tax=order.get('tax', 0),
            user_email=order.get('email')
        )
        db.session.add(record)
        db.session.commit()
        if item_ids:
            Item.query.filter(Item.id.in_(item_ids)).delete(synchronize_session=False)
            db.session.commit()
        return redirect(url_for('ThankYouPage'))
    return render_template('REVIEW.html', order=order)

@app.route("/thank-you")
@login_required
def ThankYouPage():
    order = session.get('order_review')
    if not order:
        flash("No order found. Please shop first.", category='info')
        return redirect(url_for('MarketPage'))
    session.pop('order_review', None)
    return render_template('THANKYOU.html', order=order)
