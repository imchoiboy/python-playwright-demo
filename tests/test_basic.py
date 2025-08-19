import pytest
from pages.todo_page import TodoPage

# @pytest.fixture
# def todo_page(page):
#     todo = TodoPage(page)
#     todo.go_to()
#     return todo
#
# def test_add_todo(todo_page):
#     todo_page.add_todo("Buy milk")
#     todo_page.add_todo("Walk dog")
#     todos = todo_page.get_todos_text()
#     assert todos == ["Buy milk", "Walk dog"]
#
# def test_toggle_todo(todo_page):
#     todo_page.add_todo("Write tests")
#     todo_page.toggle_todo(0)
#     item_class = todo_page.todo_items.nth(0).get_attribute("class")
#     assert "completed" in item_class
#
# def test_delete_todo(todo_page):
#     todo_page.add_todo("Temporary task")
#     todo_page.delete_todo(0)
#     assert len(todo_page.get_todos_text()) == 0
#
# def test_clear_completed(todo_page):
#     todo_page.add_todo("Task 1")
#     todo_page.add_todo("Task 2")
#     todo_page.toggle_todo(0)
#     todo_page.clear_completed()
#     todos = todo_page.get_todos_text()
#     assert todos == ["Task 2"]


def test_add_single_todo(todo_page):
    todo_page.add_todo("Buy milk")
    assert "Buy milk" in todo_page.get_todos_text()


@pytest.mark.parametrize("item", [
    "Walk the dog",
    "Do laundry",
    "Read a book",
    "Finish coding project"
])
def test_add_multiple_todos(todo_page, item):
    todo_page.add_todo(item)
    assert item in todo_page.get_todos_text()

@pytest.mark.parametrize("items", [
    ["Task 1", "Task 2", "Task 3"],
    ["Apples", "Bananas", "Cherries"],
    ["Email boss", "Review PR", "Push updates"]
])
def test_complete_todos(todo_page, items):
    # Add multiple todos
    for i in items:
        todo_page.add_todo(i)

    # Mark first item as complete
    todo_page.toggle_todo(0)

    todos = todo_page.get_todos_text()
    assert items[0] in todos  # still in list
    # Check class attribute contains "completed"
    assert "completed" in todo_page.todo_items.nth(0).get_attribute("class")


def test_delete_todo(todo_page):
    todo_page.add_todo("Buy groceries")
    todo_page.delete_todo(0)
    assert "Buy groceries" not in todo_page.get_todos_text()
