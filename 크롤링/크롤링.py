page_num=1
for i in range(15):
    print("page_num", page_num)
    page_crawling()
    page_num=page_move(page_num)
    driver.implicitly_wait(1)