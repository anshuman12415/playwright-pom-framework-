import pytest
import allure
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def context(browser, request):
    context = browser.new_context(record_video_dir="reports/videos/")
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield context
    context.tracing.stop(path=f"reports/traces/{request.node.name}_trace.zip")
    context.close()

@pytest.fixture(scope="function")
def page(context, request):
    page = context.new_page()
    yield page
    video_path = page.video.path()
    if request.node.rep_call.failed:
        allure.attach.file(
            video_path,
            name="test-video",
            attachment_type=allure.attachment_type.WEBM
        )
    page.close()

def pytest_runtest_makereport(item, call):
    if "page" in item.fixturenames:
        if call.when == "call":
            item.rep_call = call
