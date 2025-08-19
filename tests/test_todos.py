import pytest
from utils.assertions import (
    assert_todo_present,
    assert_todo_not_present,
    assert_todo_completed
)

@pytest.mark.usefixtures("todo_page")
class TestTodos:
    def test_add_todo_item(self, todo_page):
        todo_text = "Learn Playwright"
        todo_page.add_todo(todo_text)

        assert_todo_present(todo_page, todo_text)

    def test_complete_todo_item(self, todo_page):
        todo_text = "Finish homework"
        todo_page.add_todo(todo_text)
        todo_page.toggle_todo(todo_text)

        assert_todo_completed(todo_page, todo_text)

    def test_delete_todo_item(self, todo_page):
        todo_text = "Buy groceries"
        todo_page.add_todo(todo_text)
        todo_page.delete_todo(todo_text)

        assert_todo_not_present(todo_page, todo_text)

    def test_add_multiple_todos(self, todo_page):
        todos = ["Task A", "Task B", "Task C"]
        for t in todos:
            todo_page.add_todo(t)

        for t in todos:
            assert_todo_present(todo_page, t)

    @pytest.mark.parametrize("item", [
        "Walk the dog",
        "Do laundry",
        "Read a book",
        "Finish coding project"
    ])
    def test_add_multiple_todos(self, todo_page, item):
        todo_page.add_todo(item)
        assert item in todo_page.get_todos_text()

    @pytest.mark.parametrize("item_list", [
        ["Task 1", "Task 2", "Task 3"],
        ["Apples", "Bananas", "Cherries"],
        ["Email boss", "Review PR", "Push updates"]
    ])
    def test_complete_todos(self, todo_page, item_list):
        for i in item_list:
            todo_page.add_todo(i)

        todo_page.toggle_todo(item_list[0])

        todos = todo_page.get_todos_text()
        assert item_list[0] in todos  # still in list
        assert "completed" in todo_page.todo_items.nth(0).get_attribute("class")