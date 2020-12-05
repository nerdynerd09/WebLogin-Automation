from selenium import webdriver
import sqlite3
import time
from os import system


try:
    connDB = sqlite3.connect(r"Student.db")
    create_Student_Table = "create table Student_Info(Name txt, username txt, password txt)"
    connDB.execute(create_Student_Table)

    name = input("Enter your name: ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    insertData = "insert into Student_Info(name, username, password) values(?,?,?)"
    connDB.execute(insertData, (name,username,password))
    connDB.commit()
    print("Registered Successfully!!\n")
    time.sleep(2)
    system('cls')
except Exception:
    print("DB already created.")



print("""           Welcome to WebLogin
    Instagram - @hackersarena0""")

print("""\nYou want to login into
[1] Blackboard
[2] SAP Portal""")

userInput = int(input("Enter your choice --> "))

#Log in into Blackboard
if(userInput == 1):
    # print("User chose 1")
    retrieveData = "select username,password,Name from Student_Info"
    result = connDB.execute(retrieveData)
    for i in result:
        print("Logging in as", i[2])
        send_user = i[0]
        send_pass = i[1]
        time.sleep(1)
    driver = webdriver.Chrome(executable_path="C:\\WebDriver\\chromedriver.exe")
    driver.get("https://learn.upes.ac.in/webapps/bb-social-learning-BBLEARN/execute/mybb?cmd=display&toolId=AlertsOnMyBb_____AlertsTool")

    driver.find_element_by_id("user_id").send_keys(send_user)
    driver.find_element_by_id("password").send_keys(send_pass)
    driver.find_element_by_id("entry-login").click()
    print("Logged in Successfully!!")

#Login in into SAP Portal
elif(userInput == 2):

    retrieveData = "select username,password,Name from Student_Info"
    result = connDB.execute(retrieveData)
    for i in result:
        print("Logging in as",i[2])
        send_user = i[0]
        send_pass = i[1]
    driver = webdriver.Chrome("C:\\WebDriver\\chromedriver.exe")
    driver.get("https://sappro.delhi.upes.ac.in:8443/sap/bc/webdynpro/sap/zupes_student_portal#")
    print("Program will take a break for 8 sec. Q ki wo thak gya hai.")
    time.sleep(8)

    username_textbox = driver.find_element_by_id("WD2E")
    username_textbox.send_keys(send_user)

    password_textbox = driver.find_element_by_id("WD34")
    password_textbox.send_keys(send_pass)

    login_button = driver.find_element_by_id("WD3F")
    login_button.click()

    print("Login Successfull")
else:
    print("Chose a number between 1 and 2")

