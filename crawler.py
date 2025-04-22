from playwright.sync_api import sync_playwright
import urllib.parse

def get_estate_data(region, property_type):
    results = []
    query = urllib.parse.quote(f"{region} {property_type}")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"https://land.naver.com/map?query={query}")
        page.wait_for_selector("div.detail_item")  # 예시 셀렉터
        items = page.query_selector_all("div.detail_item")
        for item in items:
            # 여기에서 실제 셀렉터에 맞춰서 내용 추출
            title = item.query_selector("span.title").inner_text().strip()
            price = item.query_selector("span.price").inner_text().replace(",", "").strip()
            # 단순 예시 처리
            results.append({
                "type": property_type,
                "title": title,
                "price": price
            })
        browser.close()
    return results