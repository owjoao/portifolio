import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(channel='msedge', headless=True)
        
        # 1. Desktop 1366px (Header & Hero)
        page = await browser.new_page(viewport={'width': 1366, 'height': 800})
        await page.goto('http://localhost:8080/index.html')
        await page.wait_for_timeout(800)
        await page.screenshot(path='test_portal_new_button.png')
        
        # Close-up of the header button
        header_btn = page.locator('#site-header a[href*="wa.me"]')
        await header_btn.screenshot(path='test_btn_closeup.png')
        
        # Close-up of the logo
        logo_el = page.locator('#site-header a[href="#hero"]')
        await logo_el.screenshot(path='test_logo_closeup.png')
        
        # Mobile 390px
        page_m = await browser.new_page(viewport={'width': 390, 'height': 844})
        await page_m.goto('http://localhost:8080/index.html')
        await page_m.wait_for_timeout(600)
        await page_m.screenshot(path='test_portal_mobile_header.png')
        
        # Footer
        footer_btn = page.locator('footer a[href*="wa.me"]')
        await footer_btn.scroll_into_view_if_needed()
        await footer_btn.screenshot(path='test_footer_btn_closeup.png')

        await browser.close()
        print('New button and logo screenshots captured successfully!')

if __name__ == '__main__':
    asyncio.run(run())
