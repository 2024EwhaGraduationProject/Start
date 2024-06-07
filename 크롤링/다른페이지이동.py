def page_move(page_num):
    n=driver.find_elements(By.CLASS_NAME, 'page-navi')

    if(page_num%10!=0):
        for i in range(2,len(n)-2):
            x=n[i].find_element(By.TAG_NAME,'a').get_attribute('title')
            if(int(x)==page_num+1):
                xx=n[i].find_element(By.TAG_NAME,'a')
                driver.execute_script('arguments[0].click();',xx)
                page_num +=1
                break

    else:
        print("*")
        n=driver.find_elements(By.CLASS_NAME, 'page-navi')
        xx=n[2].find_element(By.TAG_NAME,'a'); driver.execute_script('arguments[0].click();',xx)
        time.sleep(3)
        n=driver.find_elements(By.CLASS_NAME, 'page-navi')
        xx=n[12].find_element(By.TAG_NAME,'a'); driver.execute_script('arguments[0].click();',xx)
        page_num +=1
    return page_num