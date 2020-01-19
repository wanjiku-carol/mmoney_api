def test_send(test_app):
  response = test_app.get("/send")
  assert response.status_code == 200
  assert response.json() == {"Amount": "10,000"}
