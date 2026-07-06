from fastapi.testclient import TestClient

from src.app import app, activities


def test_unregistering_participant_removes_them():
    # Arrange
    client = TestClient(app)
    activity_name = "Chess Club"
    email = "student@mergington.edu"
    activities[activity_name]["participants"].append(email)

    # Act
    response = client.post(f"/activities/{activity_name}/unregister?email={email}")

    # Assert
    assert response.status_code == 200
    assert email not in activities[activity_name]["participants"]
    assert response.json()["message"] == f"Unregistered {email} from {activity_name}"
