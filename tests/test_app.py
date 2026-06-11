from todo_project import app

def test_app_exists():
    assert app is not None

def test_login_page_loads():
    client = app.test_client()
    response = client.get("/login")
    assert response.status_code in [200, 302]

def test_register_page_loads():
    client = app.test_client()
    response = client.get("/register")
    assert response.status_code in [200, 302]
