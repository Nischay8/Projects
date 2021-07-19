from selenium import webdriver
import time
url="https://www.hapag-lloyd.com/en/online-business/schedule/interactive-schedule/interactive-schedule-solution.html"
chrome_path="C:\Development\chromedriver.exe"
driver= webdriver.Chrome(executable_path=chrome_path)
driver.get(url)
time.sleep(5)
starting_button=driver.find_element_by_xpath("//button[@id='accept-recommended-btn-handler']").click()
start_locations=driver.find_element_by_id("schedules_interactive_f:hl19").send_keys("NHAVA SHEVA")
print(start_locations)
departure_locations=driver.find_element_by_xpath("//input[@id='schedules_interactive_f:hl62']").send_keys("ANTWERP")
time.sleep(3)
find_button=driver.find_element_by_xpath("//button[@id='schedules_interactive_f:hl116']").click()