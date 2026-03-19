#Q1
'''''from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://demowebshop.tricentis.com")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.LINK_TEXT,"Books").click()
time.sleep(2)
driver.find_element(By.XPATH,"(//input[@value='Add to cart'])[1]").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT,"Shopping cart").click()
time.sleep(2)
product=driver.find_element(By.XPATH,"//td[@class='product']/a")
print("Product is present in cart" if product.is_displayed() else "Product not found")
driver.quit()'''''

#Q2
'''''from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://demowebshop.tricentis.com")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.LINK_TEXT,"Electronics").click()
time.sleep(3)
driver.find_element(By.XPATH,"//div[@class='sub-category-item']//a[contains(text(),'Cell phones')]").click()
time.sleep(2)
driver.quit()'''''

#Q3
'''''from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
driver.maximize_window()
driver.find_element(By.XPATH,"//button").click()
text=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"finish")))
print(text.text)
driver.quit()'''''

#Q4
'''''from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_controls")
driver.maximize_window()
driver.find_element(By.XPATH,"//button[text()='Remove']").click()
wait=WebDriverWait(driver,10)
wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Add']"))).click()
driver.quit()'''''

#Q5
'''''from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Chrome()
driver.get("https://demoqa.com/select-menu")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.ID,"withOptGroup").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[text()='Group 2, option 1']").click()
time.sleep(2)
value=driver.find_element(By.XPATH,"//div[@id='withOptGroup']//div[contains(@class,'singleValue')]").text
print(value)
driver.quit()'''''

#Q6
'''''from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time
driver=webdriver.Chrome()
driver.get("https://demoqa.com/select-menu")
driver.maximize_window()
time.sleep(3)
multi=driver.find_element(By.ID,"cars")
ActionChains(driver).move_to_element(multi).perform()
select=Select(multi)
select.select_by_visible_text("Volvo")
select.select_by_visible_text("Saab")
select.select_by_visible_text("Opel")
for option in select.all_selected_options:
    print(option.text)
driver.quit()'''''

#Q7
'''''from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Chrome()
driver.get("https://demoqa.com/menu/")
driver.maximize_window()
time.sleep(3)
actions=ActionChains(driver)
main=driver.find_element(By.XPATH,"//a[text()='Main Item 2']")
actions.move_to_element(main).perform()
time.sleep(2)
sub=driver.find_element(By.XPATH,"//a[text()='SUB SUB LIST »']")
actions.move_to_element(sub).perform()
time.sleep(2)
driver.find_element(By.XPATH,"//a[text()='Sub Sub Item 1']").click()
time.sleep(2)
driver.quit()'''''

#Q8
'''from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Chrome()
driver.get("https://demoqa.com/droppable")
driver.maximize_window()
time.sleep(3)
drag=driver.find_element(By.ID,"draggable")
drop=driver.find_element(By.ID,"droppable")
ActionChains(driver).drag_and_drop(drag,drop).perform()
time.sleep(2)
print(driver.find_element(By.ID,"droppable").text)
print("done step 8")
driver.quit()'''

#Q9
'''from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']").click()
time.sleep(1)
driver.switch_to.alert.accept()
time.sleep(1)
print(driver.find_element(By.ID,"result").text)
print("done step 9")
driver.quit()'''

#Q10-->
#from selenium import webdriver
#from selenium.webdriver.common.by import By
#import time
#driver=webdriver.Chrome()
#driver.get("https://the-internet.herokuapp.com/upload")
#driver.maximize_window()
#time.sleep(3)
#driver.find_element(By.ID,"file-upload").send_keys(r"C:\Users\KIIT\Downloads\ResumeUpdated.pdf")
#driver.find_element(By.ID,"file-submit").click()
#time.sleep(2)
#print(driver.find_element(By.ID,"uploaded-files").text)
#print("done step 10")
#driver.quit()

#Q11-->
#from selenium import webdriver
#from selenium.webdriver.common.by import By
#import time,os
#download_path=r"C:\Users\KIIT\Downloads"
#options=webdriver.ChromeOptions()
#prefs={"download.default_directory":download_path}
#options.add_experimental_option("prefs",prefs)
#driver=webdriver.Chrome(options=options)
#driver.get("https://the-internet.herokuapp.com/download")
#driver.maximize_window()
#time.sleep(3)
#file=driver.find_element(By.XPATH,"(//div[@class='example']//a)[1]")
#name=file.text
#file.click()
#time.sleep(5)
#print("Downloaded" if name in os.listdir(download_path) else "Not Downloaded")
#driver.quit()'''

#Q12-->
'''from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://demowebshop.tricentis.com")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.LINK_TEXT,"Books").click()
time.sleep(2)
driver.find_element(By.XPATH,"(//input[@value='Add to cart'])[1]").click()
driver.find_element(By.XPATH,"(//input[@value='Add to cart'])[2]").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT,"Shopping cart").click()
time.sleep(2)
products=driver.find_elements(By.XPATH,"//td[@class='product']/a")
print("2 products added" if len(products)==2 else "Not correct")
driver.quit()'''

#Q13-->
'''from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://demowebshop.tricentis.com")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.LINK_TEXT,"Books").click()
time.sleep(3)
books=driver.find_elements(By.XPATH,"//div[@class='product-item']")
for b in books:
    price=float(b.find_element(By.CLASS_NAME,"price").text.replace("$",""))
    if price<20:
        b.find_element(By.XPATH,".//input[@value='Add to cart']").click()
        time.sleep(1)
driver.quit()'''

#Q14-->
'''import xlrd
wb = xlrd.open_workbook("test1.xlsx")
sheet = wb.sheet_by_index(0)
for i in range(sheet.nrows):
    print(sheet.row_values(i))'''

#Q15-->
#by using attribute
'''driver.find_element(By.XPATH,"//tag[@attribute='value']")'''
#by using text
'''driver.find_element(By.XPATH,"//tag[text()='value']")'''
#by using group indexing
'''driver.find_element(By.XPATH,"(//tag[@attribute='value'])[1]")'''
#by using contains
'''driver.find_element(By.XPATH,"//tag[contains(@attribute,'value')]")'''

'''1. Which locator is generally the fastest in Selenium?
2. Which wait is recommended for handling dynamic elements in Selenium?
3. Which Selenium class is used to handle dropdown listboxes?

Answers->
1. ID
2. Explicit Wait (WebDriverWait) 
3. Select '''





