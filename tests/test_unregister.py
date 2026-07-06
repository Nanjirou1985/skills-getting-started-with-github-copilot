import pytest
from fastapi.testclient import TestClient

from src.app import app, activities


@pytest.fixture(autouse=True)
def reset_activities():
    original = {
        name: {
            **details,
            "participants": list(details.get("participants", [])),
        }
        for name, details in activities.items()
    }
    activities.clear()
    activities.update(original)
    yield
    activities.clear()
    activities.update(original)


def test_unregistering_participant_removes_them():
    client = TestClient(app)
    activity_name = "Chess Club"
    email = "student@mergington.edu"

    activities[activity_name]["participants"].append(email)

    response = client.post(f"/activities/{activity_name}/unregister?email={email}")

    assert response.status_code == 200
    assert email not in activities[activity_name]["participants"]
    assert response.json()["message"] == f"Unregistered {email} from {activity_name}"
