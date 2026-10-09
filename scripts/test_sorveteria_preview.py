from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel='msedge', headless=True)
        context = browser.new_context(viewport={'width': 1440, 'height': 900})
        page = context.new_page()

        print("Navigating to sorveteria...")
        page.goto('http://localhost:8080/sorveteria/index.html')
        page.wait_for_timeout(1000)

        # Full page screenshot
        page.screenshot(path='docs/screenshots/test_sorveteria_full.png', full_page=True)
        print("Captured test_sorveteria_full.png")

        # Hero viewport screenshot
        page.screenshot(path='docs/screenshots/test_sorveteria_hero.png')
        print("Captured test_sorveteria_hero.png")

        # Mobile viewport test
        mobile_context = browser.new_context(viewport={'width': 390, 'height': 844})
        mobile_page = mobile_context.new_page()
        mobile_page.goto('http://localhost:8080/sorveteria/index.html')
        mobile_page.wait_for_timeout(1000)
        mobile_page.screenshot(path='docs/screenshots/test_sorveteria_mobile.png')
        print("Captured test_sorveteria_mobile.png")

        browser.close()
        print("Finished sorveteria screenshots.")

if __name__ == '__main__':
    run()
