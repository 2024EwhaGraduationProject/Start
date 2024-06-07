username= 'username'
password='password'

login_url='https://ewportal.ewha.ac.kr/login.do'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(3)
driver.get(login_url)
driver.maximize_window()

#로그인
a=driver.find_element(By.CLASS_NAME,'box-con')
username_input=a.find_element(By.CLASS_NAME,'login-input').find_element(By.NAME, "loginId")
username_input.send_keys(username)
password_input=a.find_element(By.CLASS_NAME,'login-input').find_element(By.NAME, "userPass")
password_input.send_keys(password)
submit_button = a.find_element(By.CLASS_NAME,'login-btn')
submit_button.click()

#분실물 게시판으로 이동
lost_url='https://ewportal.ewha.ac.kr/portal/menu/goPage.do?anyoneId=MU7d6ab73e12fd4287bdcd127e26c3b214&nodeId=MU7d6ab73e12fd4287bdcd127e26c3b214&nodeType=SIDE_MENU'
driver.get(lost_url)

title=[];period=[];postdate=[];modifydate=[]
person=[];view=[];category=[];details=[]
section=[];process=[];phonenum_yn=[];phonenum=[]
place=[];place_details=[];state=[]
image=[];text=[]