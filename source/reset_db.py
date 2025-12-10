from Market import app, db, bcrypt
from Market.models import User, Item

with app.app_context():
    # Reset DB
    db.drop_all()
    db.create_all()

    # Admin User
    hashed_pw = bcrypt.generate_password_hash("admin").decode("utf-8")
    admin = User(
        username="admin",
        email_address="admin@admin.com",
        password_hash=hashed_pw,
        is_admin=True,
        budget=999999
    )
    db.session.add(admin)

    # All 8 planets (finalized)
    planets = [
        # Mercury
        (
            "Mercury",
            "mer-001",
            100_000_000_000,   # $100B
            "The first of four inner terrestrial planets consisting of rock. "
            "The closest planet to the sun and the smallest planet in the solar system.",
            "https://upload.wikimedia.org/wikipedia/commons/2/24/Transparent_Mercury.png"
        ),

        # Venus
        (
            "Venus",
            "ven-001",
            150_000_000_000,   # $150B (you can change this)
            "Second planet from the sun with a dense, toxic atmosphere. "
            "Known for extreme surface temperatures and volcanic terrain.",
            "https://upload.wikimedia.org/wikipedia/commons/e/e5/Venus-real_color.jpg"
        ),

        # Earth
        (
            "Earth",
            "ear-001",
            300_000_000_000,   # $300B (you can change)
            "The third planet from the sun and the only known world to support life. "
            "Features vast oceans, landmasses, and a protective atmosphere.",
            "https://upload.wikimedia.org/wikipedia/commons/9/97/The_Earth_seen_from_Apollo_17.jpg"
        ),

        # Mars
        (
            "Mars",
            "mar-001",
            120_000_000_000,   # $120B (you can change)
            "The fourth planet from the sun, known as the 'Red Planet' due to its iron-rich soil. "
            "Home to the tallest volcano and deepest canyon in the solar system.",
            "https://upload.wikimedia.org/wikipedia/commons/0/02/OSIRIS_Mars_true_color.jpg"
        ),

        # Jupiter
        (
            "Jupiter",
            "jup-001",
            250_000_000_000,   # $250B
            "First of the four outer planets. A gas giant with the iconic 'Great Red Spot' "
            "known to be the largest planet in the solar system.",
            "https://pngimg.com/d/jupiter_PNG20.png"
        ),

        # Saturn
        (
            "Saturn",
            "sat-001",
            200_000_000_000,   # $200B
            "The second of the four outer planets. A gas giant that is the second-largest "
            "planet in the solar system known for its spectacular rings.",
            "https://www.nicepng.com/png/full/381-3811493_saturn-planet-ring-saturneye-space-saturn-planet-transparent.png"
        ),

        # Uranus
        (
            "Uranus",
            "ura-001",
            170_000_000_000,   # $170B (you can change)
            "An ice giant with a unique sideways rotation. It has a pale blue color due to methane "
            "in its atmosphere and faint ring systems.",
            "https://upload.wikimedia.org/wikipedia/commons/3/3d/Uranus2.jpg"
        ),

        # Neptune
        (
            "Neptune",
            "nep-001",
            180_000_000_000,   # $180B
            "The last of the four outer planets and the most distant planet from the sun. "
            "An ice giant not visible to the naked eye, known for its deep blue color.",
            "https://upload.wikimedia.org/wikipedia/commons/7/7d/Transparent_Neptune.png"
        ),
    ]

    # Insert planets
    for name, barcode, price, desc, img in planets:
        db.session.add(
            Item(
                name=name,
                barcode=barcode,
                price=price,
                description=desc,
                image_url=img
            )
        )

    db.session.commit()
    print("DATABASE RESET COMPLETE!")
