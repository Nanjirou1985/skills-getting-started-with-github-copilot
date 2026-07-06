import copy

import pytest

from src.app import activities


BASE_ACTIVITIES = copy.deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities():
    activities.clear()
    activities.update(copy.deepcopy(BASE_ACTIVITIES))
    yield
    activities.clear()
    activities.update(copy.deepcopy(BASE_ACTIVITIES))
