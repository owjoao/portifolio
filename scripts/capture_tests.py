import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(channel='msedge', headless=True)
        
        # 1. Desktop 1366px (Hero & Header)
        page = await browser.new_page(viewport={'width': 1366, 'height': 800})
        await page.goto('http://localhost:8080/index.html')
        await page.wait_for_timeout(1000)
        await page.screenshot(path='test_1366.png')
        
        # 2. Test niche search omnibar
        input_el = page.locator('#niche-omnibar-input')
        await input_el.scroll_into_view_if_needed()
        await input_el.fill('energia solar')
        await page.wait_for_timeout(600)
        await page.screenshot(path='test_niche_search.png')
        
        # 3. Test opening full catalog
        toggle_btn = page.locator('#toggle-full-catalog-btn')
        await toggle_btn.scroll_into_view_if_needed()
        await toggle_btn.click()
        await page.wait_for_timeout(600)
        await page.screenshot(path='test_catalog_opened.png')
        
        # 4. Transparência Total section
        transp_el = page.locator('#transparencia')
        await transp_el.scroll_into_view_if_needed()
        await page.wait_for_timeout(600)
        await page.screenshot(path='test_transparencia.png')
        
        # 5. Mobile Viewport 390px (Header & Hero)
        page_m = await browser.new_page(viewport={'width': 390, 'height': 844})
        await page_m.goto('http://localhost:8080/index.html')
        await page_m.wait_for_timeout(800)
        await page_m.screenshot(path='test_mobile_header.png')
        
        # 6. Mobile Drawer Open
        burger_btn = page_m.locator('#mobile-menu-toggle')
        await burger_btn.click()
        await page_m.wait_for_timeout(500)
        await page_m.screenshot(path='test_mobile_drawer.png')
        
        # Close drawer and check footer
        close_btn = page_m.locator('#mobile-drawer-close')
        await close_btn.click()
        await page_m.wait_for_timeout(300)
        
        footer_el = page_m.locator('footer')
        await footer_el.scroll_into_view_if_needed()
        await page_m.wait_for_timeout(500)
        await page_m.screenshot(path='test_mobile_footer.png')
        
        await browser.close()
        print('All test screenshots captured successfully!')

if __name__ == '__main__':
    asyncio.run(run())
