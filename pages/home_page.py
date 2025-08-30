from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.search_box = "#Wikipedia1_wikipedia-search-input"
        self.search_button = "input.wikipedia-search-button"

    def navigate(self):
        self.page.goto("https://testautomationpractice.blogspot.com/")

    def search(self, text: str):
        self.page.fill(self.search_box, text)
        self.page.click(self.search_button)
