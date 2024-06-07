def page_crawling():
    a=driver.find_elements(By.CLASS_NAME,'text-left')
    #print(a)
    time.sleep(1)
    for i in range(1,len(a)):
        p='//*[@id="listForm"]/table/tbody/tr['+str(i)+']/td[3]/div/span[1]/a'
        aa=driver.find_element(By.XPATH,p)
        driver.execute_script('arguments[0].click();',aa)


        #btn=a[i].find_elements(By.TAG_NAME,'a')
        #driver.execute_script('arguments[0].click();',btn[0])

        pyo=driver.find_elements(By.CLASS_NAME, 'sw-board-td.sw-board-ft')

        title.append(pyo[0].text)
        period.append(pyo[1].text)
        postdate.append(pyo[2].text)
        modifydate.append(pyo[3].text)
        person.append(pyo[4].text)
        view.append(pyo[5].text)
        category.append(pyo[6].text)
        details.append(pyo[7].text)
        section.append(pyo[8].text) #분실, 습득, 학생처습득 세 종류임
        process.append(pyo[9].text)
        phonenum_yn.append(pyo[10].text)
        phonenum.append(pyo[11].text)
        place.append(pyo[12].text)
        place_details.append(pyo[13].text)
        state.append(pyo[14].text)
        text.append(driver.find_element(By.CLASS_NAME,'pd-0').text)

        try:
            img=driver.find_element(By.CLASS_NAME,'pd-0').find_element(By.CLASS_NAME,'wp100.mgb-10').find_element(By.TAG_NAME,'img')
            image.append(img.get_attribute('data-url'))
            driver.back()

        except:
            image.append('no image')
            driver.back()

    print("*************complete*************")