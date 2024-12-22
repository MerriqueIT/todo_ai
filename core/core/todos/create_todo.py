from datetime import datetime
import uuid


def init_todo(name: str) -> dict[str, str | uuid.UUID | datetime]:
	"""
	This function creates a new to-do item with a given name. It ensures the name is not empty,
	trims any leading or trailing whitespace, and generates additional metadata for the to-do item.

	:param name: The name of the to-do item. This must be a non-empty string.
	:type name: str
	:raises ValueError: If the provided name is empty after trimming whitespace.
	:return: A dictionary containing the to-do item's details:
	    - `name` (str): The trimmed name of the to-do item.
	    - `status` (str): The status of the to-do item, defaulting to `'pending'`.
	    - `id` (UUID): A unique identifier for the to-do item.
	    - `created_at` (datetime): The timestamp when the to-do item was created.
	:rtype: dict[str, Any]
	"""
	clean_name: str = name.strip()

	if clean_name == '':
		raise ValueError('Name is required')

	return {'name': clean_name, 'status': 'pending', 'id': uuid.uuid4(), 'created_at': datetime.now()}
