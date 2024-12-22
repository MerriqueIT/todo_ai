import pytest
from datetime import datetime, timedelta
from freezegun import freeze_time
from unittest.mock import patch
from core.todos.create_todo import init_todo
import uuid


def test_create_minimal_valid_todo():
    mock_uuid = uuid.UUID('d9a01f2b-b9e1-4683-96cd-a72f4a0a0687')

    with freeze_time("2024-12-12"), patch('uuid.uuid4', return_value=mock_uuid):
        name = 'My task name'
        todo = init_todo(name=name)

        assert todo == {
            'name': name,
            'status': 'pending',
            "id": mock_uuid,
            "created_at": datetime(2024, 12, 12)
        }


def test_create_todo_with_empty_name():
    with pytest.raises(ValueError, match='Name is required'):
        init_todo(name='')


def test_create_todo_with_invalid_name():
    with pytest.raises(ValueError, match='Name is required'):
        init_todo(name='    ')


@pytest.mark.skip(reason="Not implemented yet")
def test_create_todo_with_all_options():
    with freeze_time("2024-12-12"):
        payload = {
            'name': 'My task name',
            'description': 'My description',
            'start_datetime': datetime.now() + timedelta(days=1),
            'duration': timedelta(minutes=10),
            'estimated_duration': timedelta(minutes=15),
            'type': 'Meeting',
            'priority': 'low',
        }

        todo = create_todo(**payload)

        assert todo == {**payload, "id": 1, "status": "pending", "created_at": datetime(2024, 12, 12)}


def test_create_todo_with_past_datetime():
    pass


def test_create_todo_with_non_positive_duration():
    pass


def test_create_todo_with_non_positive_estimated_duration():
    pass
