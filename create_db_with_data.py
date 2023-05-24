from app import app, Users, db

# create db table
with app.app_context():
    db.create_all()

# generation data and create in table Users
for i in range(2, 11):
    data = Users(email=f'{i}@test.com', name=f'user{i}')
    with app.app_context():
        db.session.add(data)
        db.session.commit()
