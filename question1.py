import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_foreign_exchange_rate(date, currency_code):
    # 设置浏览器选项，确保浏览器不弹出提示框
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # 启动浏览器
    driver = webdriver.Chrome(options=options)
    driver.get(f"https://www.boc.cn/sourcedb/whpj/{date}.html")

    try:
        # 等待页面加载完成
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//table[@align='center']")))
        
        # 找到对应货币代码的行
        rows = driver.find_elements_by_xpath("//table[@align='center']//tr")
        for row in rows:
            cells = row.find_elements_by_tag_name("td")
            if len(cells) > 0 and cells[0].text.strip() == currency_code:
                exchange_rate = cells[6].text.strip()  # 现汇卖出价
                break
        else:
            raise ValueError("Currency code not found")
    finally:
        # 关闭浏览器
        driver.quit()

    return exchange_rate

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("请输入: python3 yourcode.py <date> <currency_code>")
        sys.exit(1)

    date = sys.argv[1]
    currency_code = sys.argv[2].upper()

    exchange_rate = get_foreign_exchange_rate(date, currency_code)

    print(exchange_rate)

    # 将结果写入 result.txt 文件
    with open("result.txt", "w") as f:
        f.write(f"{currency_code} exchange rate on {date}: {exchange_rate}\n")
