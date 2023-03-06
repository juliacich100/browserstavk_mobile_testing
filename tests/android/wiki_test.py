import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser


def test_search_article():
    with allure.step("Tap wiki_search field"):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
    with allure.step("Enter request"):
        browser.element(
            (AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")
        ).send_keys("Automation")
    with allure.step("Check search results"):
        browser.all(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')
        ).should(have.size_greater_than(0))