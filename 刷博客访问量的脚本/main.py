# 双访问量的脚本
# python3.5.0
# selenium3.141.0
# Chrome 67
# Chrome driver 2.41

# 导入模块
from selenium import webdriver
# 创建实例
driver = webdriver.Chrome()
# 打开徽标统计的链接
driver.get("https://visitor-badge.laobi.icu/badge?page_id=411message")

# 一直刷新就完了
while (1):
    driver.refresh()
