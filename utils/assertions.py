def assert_todo_present(todo_page, todo_text: str) -> None:
    todos = todo_page.get_todos_text()
    assert todo_text in todos, f"Expected '{todo_text}' in {todos}, but it was missing."


def assert_todo_not_present(todo_page, todo_text: str) -> None:
    todos = todo_page.get_todos_text()
    assert todo_text not in todos, f"'{todo_text}' should not be present, but found in {todos}."


def assert_todo_completed(todo_page, todo_text: str) -> None:
    assert todo_page.is_todo_completed(todo_text), f"'{todo_text}' should be marked completed but is not."
