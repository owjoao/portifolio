from playwright.sync_api import sync_playwright

edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=edge_path)
    
    # 1. CRM Servicos Dark
    ctx = browser.new_context(viewport={'width': 1440, 'height': 900})
    page = ctx.new_page()
    page.goto('http://localhost:8080/crm-servicos/index.html')
    page.evaluate("applyTheme('dark')")
    page.wait_for_timeout(1200) # allow counter and chart bar animations to finish
    page.screenshot(path='crm_servicos_animated_dark.png')
    
    # 2. CRM Servicos Light
    page.evaluate("applyTheme('light')")
    page.wait_for_timeout(600)
    page.screenshot(path='crm_servicos_animated_light.png')

    # 3. CRM Vendas Dark
    page.goto('http://localhost:8080/crm-vendas/index.html')
    page.evaluate("applyTheme('dark')")
    page.wait_for_timeout(1200)
    page.screenshot(path='crm_vendas_animated_dark.png')

    # 4. CRM Vendas Light
    page.evaluate("applyTheme('light')")
    page.wait_for_timeout(600)
    page.screenshot(path='crm_vendas_animated_light.png')

    browser.close()
    print('All animated screenshots captured successfully.')
