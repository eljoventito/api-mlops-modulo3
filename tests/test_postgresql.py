from fastapi.testclient import TestClient
from app.main import app
import psycopg2
from unittest.mock import patch

client = TestClient(app)


def test_check_db_connection_success():
    with patch("psycopg2.connect") as mock_connect:
        response = client.get("/api/check-db")
        assert response.status_code == 200
        assert response.json() == {
            "status": "success",
            "message": "Connected to the database successfully."
        }
        mock_connect.assert_called_once()


def test_check_db_connection_failure():
    with patch("psycopg2.connect", side_effect=Exception("Fake error")):
        response = client.get("/api/check-db")
        assert response.status_code == 500
        assert response.json()["detail"]["status"] == "error"
        assert "Database connection failed" in response.json()["detail"]["message"]
