import datetime
from hocapontas import json_db
from contracts import contract

db = json_db.JsonDB()
today = str(datetime.date.today())


@contract
def add_item(deadline, description, comments, priority, completed=False):
    """
    Builds a list of task item attributes from the given
    input parameters and writes the item to database after
    proper validation.

    :param deadline: YYYY-mm-dd str of deadline for this task.
    :type deadline: str
    :param description: Description of what the task is about.
    :type description: str
    :param comments: Any comments related to this task.
    :type comments: list
    :param priority: Priority value used to compare items.
    :type priority: int
    :param completed: Indication of an item's completion. **Optional**
    :type completed: bool
    :returns: The newly created item.
    :rtype: dict

    :raises: ValueError
    """
    item = [deadline, description, comments, priority, completed]
    err = is_valid_item(*item)
    if err:
        raise ValueError(err)
    json_item = db.write(item)
    return json_item


@contract
def is_valid_item(deadline, description, comments, priority, completed):
    """
    Validates the attributes of a task item and accumulates
    any error messages along the way. If no errors can be
    found, the item is valid and the return string is empty.

    :param deadline: YYYY-mm-dd str of a viable date.
    :type deadline: str
    :param description: Description of what the task is about.
    :type description: str
    :param comments: Any comments related to this task.
    :type comments: list
    :param priority: Priority value used to compare items.
    :type priority: int
    :param completed: Indication of an item's is completion.
    :type completed: bool
    :returns: An empty or messages describing any invalid values.
    :rtype: str
    """
    is_valid_date(deadline)
    err = ''
    attribute = 'Attribute [description]'
    if type(description) is not str:
        err += '{}: Expected type string, got {}.\n'.format(
            attribute, type(description)
        )
    if len(description) <= 0 or len(description) > 300:
        err += '{}: Expected len > 0 and <= 300, got {}.\n'.format(
            attribute, len(description)
        )
    attribute = 'Attribute [comments]'
    if type(comments) is not list:
        err += '{}: Expected type list, got {}.\n'.format(
            attribute, type(comments)
        )
    if len(comments) > 20:
        err += '{}: Expected len <= 20, got {}\n'.format(
            attribute, len(comments)
        )
    attribute = 'Attribute [priority]'
    if type(priority) is not int:
        err += '{}: Expected type int, got {}.\n'.format(
            attribute, type(priority)
        )
    if priority < 0 or priority > 10:
        err += '{}: Expected len <= 20, got {}.\n'.format(
            attribute, priority
        )
    attribute = 'Attribute [completed]'
    if type(completed) is not bool:
        err += '{}: Expected type bool, got {}.\n'.format(
            attribute, type(completed)
        )
    return err


@contract
def is_valid_date(date):
    """
    Checks if a date string of format YYYY-mm-dd is valid
    and can be parsed into a datetime date object.

    :param date: The date str ('YYYY-mm-dd').
    :type date: str
    :returns: Th validity of a deadline date string.
    :rtype: bool
    :raises: ValueError
    """
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
        return True
    except ValueError as e:
        err = 'Expected valid date str (YYYY-mm-dd), got {}.'.format(date)
        raise ValueError(err) from e


@contract
def list_by_id(item_id):
    """
    Queries the database for an item with the given item_id
    and returns it if found.

    :param item_id: The ID of the target item.
    :type item_id: int
    :returns: The task item or None.
    :rtype: dict
    """
    for task in db.read():
        if item_id == task['id']:
            return task


@contract
def list_in_range(date_from=today, date_to=today):
    """
    Lists all tasks which have a deadline within the given
    range of dates. Defaults to the actual date of when it's
    being called.

    :param date_from: Valid YYYY-mm-dd lower date str
    :type date_from: str
    :param date_to: Valid YYYY-mm-dd upper date str
    :type date_to: str
    :returns: A list of items sorted by earliest deadline first.
    :rtype: list(dict)
    """
    for date in [date_from, date_to]:
        is_valid_date(date)

    results = []
    for task in db.read():
        if date_from <= task['deadline'] <= date_to:
            results.append(task)
    return sorted(results, key=lambda k: k['deadline'])


@contract
def update_item(item_id, **kwargs):
    """
    Updates the field of an item using the given keyword
    arguments. Raises a KeyError if an invalid key is given..

    :param item_id: The id of the target item to update.
    :type item_id: int
    :param kwargs: The key:value fields to update.
    :type kwargs: dict
    :returns: The updated item and a status message.
    :rtype: dict
    :raises: KeyError
    """
    item = list_by_id(item_id)
    for key, value in kwargs.items():
        if key not in item:
            raise KeyError('{}  is not a valid key.'.format(key))
        item[key] = value
    db.update(item_id, item)
    return item


def toggle_completed(item_id):
    """
   Toggles the completion status of an item between True
   and False given by the item id.

    :param item_id: The id of the target item to update.
    :type item_id: int
    :returns: The updated item.
    :rtype: dict
    """
    item = list_by_id(item_id)
    item['completed'] = not item['completed']
    db.update(item_id, item)
    return item


@contract
def delete_item(item_id):
    """
    Deletes any item with the given item_id from the
    database. Returns True if the item was found and
    deleted or False if the item was not found.

    :param item_id: The id of the target to delete.
    :type item_id: int
    :returns: Status of the operation.
    :rtype: bool
    """
    for item in db.read():
        if item_id == item['id']:
            db.delete(item)
            return True
    return False


def reset_db():
    """
    Completely removes and recreates an empty database.
    """
    db.reset()
