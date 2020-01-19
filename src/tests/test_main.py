
def test_ping(test_app):
  response = test_app.get("/ping")
  assert response.status_code == 200
  assert response.json() == {"ping": "pong"}

def test_balancer(test_app):
  response = test_app.get("/balance")
  assert response.status_code == 200
  assert response.json() == {"Balance": "10,000"}
