from datetime import datetime
from ext import app, db
from models import Product, Users
import json

with open('data/products.json', 'r') as file:
    products = json.load(file)


for product in products:
    try:
        product["date"] = datetime.strptime(product["date"], "%d.%m.%y").date()
    except ValueError:
        # If it fails, try another format
        product["date"] = datetime.strptime(product["date"], "%m.%d.%y").date()

with open('data/db.json', 'r') as file:
    admin_user = json.load(file)

with app.app_context():

    db.create_all()

    for product in products:

        existing_product = Product.query.filter_by(name=product["name"]).first()
        if not existing_product:
            new_product = Product(
                name=product["name"],
                title=product["title"],
                platform=product["platform"],
                condition=product["condition"],
                price=product["price"],
                date=product["date"],
                img=product["image"],
                category=product["category"]
            )
            db.session.add(new_product)


    existing_admin = Users.query.filter_by(username=admin_user["username"]).first()
    if not existing_admin:
        new_admin = Users(
            username=admin_user["username"],
            password=admin_user["password"],
            role=admin_user["role"]
        )
        db.session.add(new_admin)
        print("Admin user created successfully.")
    else:
        print("Admin user already exists.")


    db.session.commit()
    print("Database initialized successfully.")

    admin_user_to_delete = Users.query.filter_by(username="admin").first()
    if admin_user_to_delete:
        db.session.delete(admin_user_to_delete)
        db.session.commit()
        print("Default admin user deleted.")

