from fastapi.testclient import TestClient

from src.app import app, activities


def test_get_activities_returns_activity_data():
    # Arrange
    client = TestClient(app)

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    assert "Chess Club" in response.json()


def test_signup_adds_participant():
    # Arrange
    client = TestClient(app)
    email = "student@mergington.edu"

    # Act
    response = client.post(f"/activities/Chess Club/signup?email={email}")

    # Assert
    assert response.status_code == 200
    assert email in activities["Chess Club"]["participants"]


def test_signup_rejects_duplicate_participant():
    # Arrange
    client = TestClient(app)
    email = "student@mergington.edu"
    client.post(f"/activities/Chess Club/signup?email={email}")

    # Act
    response = client.post(f"/activities/Chess Club/signup?email={email}")

    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up for this activity"
