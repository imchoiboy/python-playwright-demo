# from playwright.sync_api import Page, Locator
#
# class TodoPage:
#     URL = "https://demo.playwright.dev/todomvc"
#
#     def __init__(self, page: Page):
#         self.page = page
#         self.new_todo_input: Locator = page.locator(".new-todo")
#         self.todo_items: Locator = page.locator(".todo-list li")
#         self.todo_count: Locator = page.locator(".todo-count strong")
#         self.clear_completed_button: Locator = page.locator(".clear-completed")
#         self.filters: Locator = page.locator(".filters a")
#
#     def go_to(self):
#         self.page.goto(self.URL)
#
#     def add_todo(self, text: str):
#         self.new_todo_input.fill(text)
#         self.new_todo_input.press("Enter")
#
#     def delete_todo(self, index: int):
#         todo = self.todo_items.nth(index)
#         todo.hover()
#         todo.locator(".destroy").click()
#
#     def get_todos_text(self):
#         elements = self.todo_items.all()
#         return [el.text_content() for el in elements]
#
#     def clear_completed(self):
#         self.clear_completed_button.click()
#
#
#     def get_all_todos_text(self):
#         # Shortcut method that returns all text contents in the list
#         return self.todo_items.all_text_contents()
#
#     def toggle_todo(self, index: int):
#         self.todo_items.nth(index).locator(".toggle").click()
#
#     def filter_todos(self, filter_name: str):
#         # Filters: "All", "Active", "Completed"
#         self.filters.filter(has_text=filter_name).click()
#
#     def get_todo_count(self) -> int:
#         return int(self.todo_count.text_content())
#
#     def edit_todo(self, index: int, new_text: str):
#         todo_label = self.todo_items.nth(index).locator("label")
#         todo_label.dblclick()
#         edit_input = self.todo_items.nth(index).locator(".edit")
#         edit_input.fill(new_text)
#         edit_input.press("Enter")

from playwright.sync_api import Page, Locator

class TodoPage:

    def __init__(self, page: Page) -> None:
        self.page: Page = page
        self.new_todo_input: Locator = page.locator("input.new-todo")
        self.todo_items: Locator = page.locator("ul.todo-list li")
        self.todo_labels: Locator = page.locator("ul.todo-list li label")
        self.todo_checkboxes: Locator = page.locator("ul.todo-list li .toggle")
        self.todo_delete_buttons: Locator = page.locator("ul.todo-list li button.destroy")

    def navigate(self) -> None:
        """Open the TodoMVC app base URL (set in Config)."""
        self.page.goto("/")

    def add_todo(self, todo_text: str) -> None:
        """Add a new todo item."""
        self.new_todo_input.fill(todo_text)
        self.new_todo_input.press("Enter")

    def toggle_todo(self, todo_text: str) -> None:
        """Mark a todo item as completed by its text."""
        item = self.page.locator(f"//label[text()='{todo_text}']/preceding-sibling::input[@class='toggle']")
        item.check()

    def delete_todo(self, todo_text: str) -> None:
        """Delete a todo item by hovering over it first, then clicking delete."""
        item = self.page.locator(f"//label[text()='{todo_text}']/..")
        delete_button = item.locator("button.destroy")
        item.hover()  # 👈 makes delete button visible
        delete_button.click()

    # --------------------
    # Assertions / Helpers
    # --------------------
    def get_todos_text(self) -> list[str]:
        """Return a list of visible todo texts."""
        return self.todo_labels.all_text_contents()

    def is_todo_completed(self, todo_text: str) -> bool:
        """Check if a specific todo is marked completed."""
        completed_item = self.page.locator(f"//li[contains(@class,'completed')]//label[text()='{todo_text}']")
        return completed_item.is_visible()
