from playwright.sync_api import sync_playwright
import urllib.parse

def get_estate_data(region, property_type):
    results = []
    query = urllib.parse.quote(f"{region} {property_type}")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"https://land.naver.com/map?query={query}")
        page.wait_for_selector("div.detail_item")
        items = page.query_selector_all("div.detail_item")
        for item in items:
            # 예시 셀렉터: 제목, 가격, 주소
            title = item.query_selector("span.title").inner_text().strip()
            price = item.query_selector("span.price").inner_text().replace(",", "").strip()
            addr_elem = item.query_selector("span.addr")
            address = addr_elem.inner_text().strip() if addr_elem else ""
            tokens = address.split()
            city = tokens[0] if len(tokens) >= 1 else ""
            district = tokens[1] if len(tokens) >= 2 else ""
            results.append({
                "type": property_type,
                "title": title,
                "price": price,
                "city": city,
                "district": district
            })
        browser.close()
    return results