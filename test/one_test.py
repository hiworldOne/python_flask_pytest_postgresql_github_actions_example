from app import Users


def test_check_status_code(client):
    """
    check status code 200 page home
    :param client: object client
    """
    res = client.get('/')
    assert res.status_code == 200


def test_check_html(app, client):
    """
    check html home page
    :param app: object app
    :param client: object client
    """
    with app.app_context():
        res = client.get('/')
        for r in Users.query.all():
            r = f"<p>name: {r.name}</p>" \
                f"<p>email: {r.email}</p>"
            assert r in res.data.__str__()
