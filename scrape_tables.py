from playwright.sync_api import sync_playwright
import re

# 👉 Replace these with the actual Seed links given in your assignment
SEED_URLS = [
    "https://sanand0.github.io/tdsdata/js_table/?seed=27",
    "https://sanand0.github.io/tdsdata/js_table/?seed=28",
    "https://sanand0.github.io/tdsdata/js_table/?seed=29",
    "https://sanand0.github.io/tdsdata/js_table/?seed=30",
    "https://sanand0.github.io/tdsdata/js_table/?seed=31",
    "https://sanand0.github.io/tdsdata/js_table/?seed=32",
    "https://sanand0.github.io/tdsdata/js_table/?seed=33",
    "https://sanand0.github.io/tdsdata/js_table/?seed=34",
    "https://sanand0.github.io/tdsdata/js_table/?seed=35",
    "https://sanand0.github.io/tdsdata/js_table/?seed=36",
]

def extract_numbers(text):
    """Extract all numbers from text"""
    return [float(x) for x in re.findall(r"-?\d+\.?\d*", text)]

total_sum = 0

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    for url in SEED_URLS:
        print(f"Visiting: {url}")

        page.goto(url, wait_until="networkidle")

        # wait for tables to appear (important for dynamic pages)
        page.wait_for_selector("table")

        tables = page.locator("table")
        table_count = tables.count()

        for i in range(table_count):
            table_text = tables.nth(i).inner_text()
            numbers = extract_numbers(table_text)
            total_sum += sum(numbers)

    browser.close()

print("====================================")
print(f"FINAL TOTAL SUM = {total_sum}")
print("====================================")