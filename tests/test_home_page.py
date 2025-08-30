import pytest
import allure
from pages.home_page import HomePage

@allure.feature("Home Page")
@allure.story("Search functionality")
def test_search_functionality(page):
    home = HomePage(page)
    home.navigate()
    home.search("playwright")
    assert page.is_visible("ul#Wikipedia1_wikipedia-search-results")
