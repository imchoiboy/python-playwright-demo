from playwright.sync_api import Page, Locator

class TodoPage:
    URL = "https://demo.playwright.dev/todomvc"

    def __init__(self, page: Page):
        self.page = page
        self.new_todo_input: Locator = page.locator(".new-todo")
        self.todo_items: Locator = page.locator(".todo-list li")
        self.todo_count: Locator = page.locator(".todo-count strong")
        self.clear_completed_button: Locator = page.locator(".clear-completed")
        self.filters: Locator = page.locator(".filters a")

    def go_to(self):
        self.page.goto(self.URL)

    def add_todo(self, text: str):
        self.new_todo_input.fill(text)
        self.new_todo_input.press("Enter")

    def delete_todo(self, index: int):
        todo = self.todo_items.nth(index)
        todo.hover()
        todo.locator(".destroy").click()

    def get_todos_text(self):
        elements = self.todo_items.all()
        return [el.text_content() for el in elements]

    def clear_completed(self):
        self.clear_completed_button.click()


    def get_all_todos_text(self):
        # Shortcut method that returns all text contents in the list
        return self.todo_items.all_text_contents()

    def toggle_todo(self, index: int):
        self.todo_items.nth(index).locator(".toggle").click()

    def filter_todos(self, filter_name: str):
        # Filters: "All", "Active", "Completed"
        self.filters.filter(has_text=filter_name).click()

    def get_todo_count(self) -> int:
        return int(self.todo_count.text_content())

    def edit_todo(self, index: int, new_text: str):
        todo_label = self.todo_items.nth(index).locator("label")
        todo_label.dblclick()
        edit_input = self.todo_items.nth(index).locator(".edit")
        edit_input.fill(new_text)
        edit_input.press("Enter")
