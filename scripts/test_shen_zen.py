import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(channel='msedge', headless=True)
        
        # 1. Desktop 1440px (Hero & Header inicial)
        page = await browser.new_page(viewport={'width': 1440, 'height': 900})
        await page.goto('http://localhost:8080/acupunturista/index.html')
        await page.wait_for_timeout(800)
        await page.screenshot(path='shen_zen_desktop_1440.png')
        
        # 2. Desktop 1366px Scrolled (Verificar redução do header e backdrop-blur)
        page_1366 = await browser.new_page(viewport={'width': 1366, 'height': 800})
        await page_1366.goto('http://localhost:8080/acupunturista/index.html')
        await page_1366.wait_for_timeout(500)
        await page_1366.evaluate('window.scrollTo(0, 150)')
        await page_1366.wait_for_timeout(600)
        await page_1366.screenshot(path='shen_zen_header_scrolled.png')
        
        # 3. Tablet 768px
        page_tablet = await browser.new_page(viewport={'width': 768, 'height': 1024})
        await page_tablet.goto('http://localhost:8080/acupunturista/index.html')
        await page_tablet.wait_for_timeout(600)
        await page_tablet.screenshot(path='shen_zen_tablet_768.png')
        
        # 4. Mobile 390px (Header & Hero)
        page_mobile = await browser.new_page(viewport={'width': 390, 'height': 844})
        await page_mobile.goto('http://localhost:8080/acupunturista/index.html')
        await page_mobile.wait_for_timeout(600)
        await page_mobile.screenshot(path='shen_zen_mobile_390.png')
        
        # 5. Mobile Drawer Open
        toggle_btn = page_mobile.locator('#zen-mobile-toggle')
        await toggle_btn.click()
        await page_mobile.wait_for_timeout(400)
        await page_mobile.screenshot(path='shen_zen_mobile_drawer.png')
        
        # Close drawer and check Como Funciona / Meridianos
        close_btn = page_mobile.locator('#zen-drawer-close')
        await close_btn.click()
        await page_mobile.wait_for_timeout(300)
        
        # 6. Compact Mobile 360px
        page_compact = await browser.new_page(viewport={'width': 360, 'height': 740})
        await page_compact.goto('http://localhost:8080/acupunturista/index.html')
        await page_compact.wait_for_timeout(600)
        await page_compact.screenshot(path='shen_zen_mobile_360.png')
        
        await browser.close()
        print('All Shen Zen verification screenshots captured successfully!')

if __name__ == '__main__':
    asyncio.run(run())
