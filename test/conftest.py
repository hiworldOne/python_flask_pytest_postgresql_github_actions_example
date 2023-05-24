import pytest
from app import app as flask_app
from app import Users, db


@pytest.fixture
def app():
    # context need for database
    with flask_app.app_context():
        db.create_all()
    # create users
    for i in range(2, 11):
        data = Users(email=f'{i}@test.com', name=f'user{i}')
        with flask_app.app_context():
            db.session.add(data)
            db.session.commit()
    # app
    yield flask_app
    # delete users
    with flask_app.app_context():
        for i in Users.query.all():
            db.session.delete(i)
        db.session.commit()


@pytest.fixture()
def client(app):
    """"
    client for requests to server(get or post)
    """
    return app.test_client()
