from playwright.sync_api import Page, Locator

from utils.config import Config


class TodoPage:

    def __init__(self, page: Page) -> None:
        self.page: Page = page
        self.new_todo_input: Locator = page.locator("input.new-todo")
        self.todo_items: Locator = page.locator("ul.todo-list li")
        self.todo_labels: Locator = page.locator("ul.todo-list li label")
        self.todo_checkboxes: Locator = page.locator("ul.todo-list li .toggle")
        self.todo_delete_buttons: Locator = page.locator("ul.todo-list li button.destroy")

    def navigate(self) -> None:
        self.page.goto(Config.BASE_URL)

    def add_todo(self, todo_text: str) -> None:
        self.new_todo_input.fill(todo_text)
        self.new_todo_input.press("Enter")

    def toggle_todo(self, todo_text: str) -> None:
        item = self.page.locator(f"//label[text()='{todo_text}']/preceding-sibling::input[@class='toggle']")
        item.check()

    def delete_todo(self, todo_text: str) -> None:
        item = self.page.locator(f"//label[text()='{todo_text}']/..")
        delete_button = item.locator("button.destroy")
        item.hover()
        delete_button.click()

    # Assertions / Helpers
    def get_todos_text(self) -> list[str]:
        return self.todo_labels.all_text_contents()

    def is_todo_completed(self, todo_text: str) -> bool:
        completed_item = self.page.locator(f"//li[contains(@class,'completed')]//label[text()='{todo_text}']")
        return completed_item.is_visible()
