#The given Below code is user to verfy the captcha by automatic button click< Could you make this code more better and efficent for verify the captcha?
import time
import pyautogui
import random
import itertools
import os
import requests
from selenium import webdriver
from msedge.selenium_tools import Edge, EdgeOptions
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from PIL import ImageGrab
import pytesseract
from PIL import Image
import firebase_admin
from firebase_admin import credentials, db


def captcha_process(cap_username,cap_password):
    options = EdgeOptions()
    options.use_chromium = True
    options.add_argument('--no-sandbox')  # Optional: Add any additional options as needed

    # Initialize the Edge WebDriver using the EdgeChromiumDriverManager
    browser = Edge(executable_path=EdgeChromiumDriverManager().install(), options=options) # Optional argument, if not specified will search path.
    browser.get('https://login.teletype.team/')
    time.sleep(3)
    inputElement =browser.find_element("name",'username')
    #Enter Your User Name
    inputElement.send_keys(cap_username)
    #inputElement.send_keys('ft005a001101_45561')
    #inputElement.send_keys('karthickra_6987')
    #inputElement.send_keys('ttyapmanojpushp_1817')
    #inputElement.send_keys('ttyrishkumar2_7935')

    inputElement =browser.find_element("name",'password')
    #Enter Your Password
    #inputElement.send_keys('qwerty123#')
    #rishkmar
    #inputElement.send_keys('lsnswi#5068')
    #ca22521314  
    inputElement.send_keys(cap_password)
    #manoj
    #inputElement.send_keys('psiqtj#6393')
    #Vijay
    #inputElement.send_keys('ywcpad#7109')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(5)

    browser.execute_script("""
    function ClickConnect(){
        console.log(" "); 
        try {
            document.querySelector("#root > div > div._1picb7i > div > div > div > div > div > div > div > div._1s8w8pn > div > div > div > div > div > div:nth-child(2) > div > div:nth-child(2) > div._1ve0kk4b").click();
    console.error("working");
    } catch (e) {
        console.error(" ");
        }
        }
        setInterval(ClickConnect,6000)
    """)
    time.sleep(5)

    browser.execute_script("""
    function ClickConnect(){
        console.log(" "); 
        try {
          document.querySelector("#root > div > div._1picb7i > div > div > div > div > div > div > div > div._1s8w8pn > div > div > div > div > div > div:nth-child(2) > form > div._ona0v3s > button._37ran8t > div._1ve0kk4b").click();
    console.error("working");
    } catch (e) {
        console.error(" ");
        }
        }
        setInterval(ClickConnect,6000)
    """)
    time.sleep(5)

    browser.execute_script("""
    function ClickConnect(){
        console.log(" "); 
        try {
            document.querySelector("#root > div > div._1picb7i > div > div > div > div > div > div > div > div._1s8w8pn > div > div > div > div > div > div:nth-child(2) > form > div._ona0v3s > button._37ran8t > div._1ve0kk4b").click();
    console.error("working");
    } catch (e) {
        console.error(" ");
        }
        }
        setInterval(ClickConnect,6000)

    """)
    time.sleep(5)
    browser.execute_script("""
    function ClickConnect(){
        console.log(" "); 
        try {
            document.querySelector("#root > div > div._1picb7i > div > div > div > div > div > div > div > div._1s8w8pn > div > div > div > div > div > div:nth-child(2) > div > div:nth-child(1) > div > div._1ve0kk4b").click();
    console.error("working");
    } catch (e) {
        console.error(" ");
        }
        }
        setInterval(ClickConnect,5000)
    """)
    time.sleep(5)
    browser.execute_script("""
    function ClickConnect(){
        console.log(" "); 
        try {
            document.querySelector("#root > div > div._1picb7i > div > div > div > div > div > div > div > div._1s8w8pn > div > div > div > div > div > div:nth-child(2) > form > div._ona0v3s > button._37ran8t > div._1ve0kk4b").click();
    console.error("working");
    } catch (e) {
        console.error(" ");
        }
        }
        setInterval(ClickConnect,6000)

    """)
    time.sleep(5)
    browser.execute_script("""
    function ClickConnect(){
        console.log(" "); 
        try {
            document.querySelector("#root > div > div._1picb7i > div > div > div > div > div > div > div > div._1s8w8pn > div > div > div > div > div > div:nth-child(2) > form > div._ona0v3s > button > div:nth-child(2)").click();
    console.error("working");
    } catch (e) {
        console.error(" ");
        }
        }
        setInterval(ClickConnect,6000)

    """)
    browser.execute_script("""
    try {
            document.querySelector("#root > div > div._1picb7i > div > div > div > div > div > div > div > div._1s8w8pn > div > div > div > div > div > div:nth-child(2) > form > div._ona0v3s > button > div:nth-child(2)").click();
    console.error("working");
    } catch (e) {
        console.error(" ");
        }
    """)
    time.sleep(5)
    num =999999
    i=1
    txt_len=0
    for x in itertools.repeat(None, num):
        try:
            current_url1=browser.current_url
            if(current_url1=="https://exela.teletype.team/item/load"):
                 # Replace with the URL of the webpage you want to capture
                 pass
            elif(current_url1=="https://exela.teletype.team/items/review"):
                pyautogui.press('enter')

            elif(current_url1=="https://exela.teletype.team/item/1"):
                time.sleep(3)
                x1, y1 = 270, 300
                x2, y2 = 800, 455
                folder_path = "images"
                file_name = str(i)+".png"
                # Create the folder if it doesn't exist
                input_field_element = browser.find_element_by_name('updatedValue')


                # Extract the data from the input field
                data = input_field_element.get_attribute('value')

                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                # Combine the folder path and file name
                file_path = os.path.join(folder_path, file_name)

                take_screenshot_with_coords_and_save(x1, y1, x2, y2, file_path,data)

            elif(current_url1=="https://exela.teletype.team/item/2"):
                time.sleep(3)
                x1, y1 = 270, 300
                x2, y2 = 800, 455
                folder_path = "images"
                file_name = str(i)+".png"
                # Create the folder if it doesn't exist
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                # Combine the folder path and file name
                file_path = os.path.join(folder_path, file_name)
                # Take the screenshot and save it in the specified folder
                input_field_element = browser.find_element_by_name('updatedValue')


                # Extract the data from the input field
                data = input_field_element.get_attribute('value')
                time.sleep(2)
                take_screenshot_with_coords_and_save(x1, y1, x2, y2, file_path,data)    

            elif(current_url1=="https://exela.teletype.team/item/3"):
                time.sleep(3)
                x1, y1 = 270, 300
                x2, y2 = 800, 455
                folder_path = "images"
                file_name = str(i)+".png"
                # Create the folder if it doesn't exist
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                # Combine the folder path and file name
                file_path = os.path.join(folder_path, file_name)
                input_field_element = browser.find_element_by_name('updatedValue')

                # Extract the data from the input field
                data = input_field_element.get_attribute('value')
                time.sleep(2)
                take_screenshot_with_coords_and_save(x1, y1, x2, y2, file_path,data)

            elif(current_url1=="https://exela.teletype.team/item/4"):
                time.sleep(3)
                x1, y1 = 270, 300
                x2, y2 = 800, 455
                folder_path = "images"
                file_name = str(i)+".png"
                # Create the folder if it doesn't exist
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                # Combine the folder path and file name
                file_path = os.path.join(folder_path, file_name)
                input_field_element = browser.find_element_by_name('updatedValue')

                # Extract the data from the input field
                data = input_field_element.get_attribute('value')
                # Take the screenshot and save it in the specified folder
                time.sleep(2)
                take_screenshot_with_coords_and_save(x1, y1, x2, y2, file_path,data)     
    
            elif(current_url1=="https://exela.teletype.team/item/5"):
                time.sleep(3)
                x1, y1 = 270, 300
                x2, y2 = 800, 455
                folder_path = "images"
                file_name = str(i)+".png"
                # Create the folder if it doesn't exist
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                # Combine the folder path and file name
                file_path = os.path.join(folder_path, file_name)
                input_field_element = browser.find_element_by_name('updatedValue')


                # Extract the data from the input field
                data = input_field_element.get_attribute('value')
                time.sleep(2)
                # Take the screenshot and save it in the specified folder
                take_screenshot_with_coords_and_save(x1, y1, x2, y2, file_path,data)
            else:
                print("url Not matched")  
                time.sleep(1)
                pyautogui.press('enter')

        except Exception as e:
            print(f"Error: {e}")
        finally:
            # Close the browser
            #browser.quit()
            print("finally")

        def take_screenshot_with_coords_and_save(x1, y1, x2, y2, file_path,data):
            print("Dat From Text Field",data)
            # Take the screenshot and save it in the specified folder
            screenshot = ImageGrab.grab(bbox=(x1, y1, x2, y2))
            # Save the screenshot as a PNG file in the specified folder
            screenshot.save(file_path, "PNG")
            # Capture the specified region as an RGB image
            print(file_path)
            image = Image.open(file_path)
            #image = image.convert('L')
            # Use pytesseract to extract text from the image
            extracted_text = pytesseract.image_to_string(image, lang='eng', config='--psm 6 tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
            print(type(extracted_text))
            single_line_text = extracted_text.replace("\n", " ").replace(" ", " ")
            print(single_line_text)
            single_line_text=single_line_text[6:-6]
            txt_len = len(single_line_text)
            print(type(txt_len))
            print(txt_len)
            time.sleep(4)
            process_enter(txt_len, single_line_text,data)

        def process_enter(txt_len,single_line_text,data):
            len_data=len(data)
            length_txt=int(txt_len)
            print(type(length_txt))
            if(len_data>=1):
                pyautogui.write(data)
                time.sleep(2)
                pyautogui.press('enter')
                data=""
            elif length_txt >= 5:
                pyautogui.write(single_line_text)
                time.sleep(2)
                pyautogui.press('enter')
            elif(len_data==0 or length_txt<=5 or length_txt==0):
                button = browser.find_element_by_css_selector("#root > div > div._1picb7i > div > div > div > div > div > div._18t04jo > div > div._1s8w8pn > div > div > div > div._kjo4awc > div > div:nth-child(2) > form > div._ona0v3s > div._19uylb50 > button > div._1ve0kk4b")
                # Click the button
                button.click()     
        i =i+1

def check_user_credentials(username, password):
    try:
        # Initialize Firebase Admin SDK
        cred = credentials.Certificate("captcha-login-386ec-firebase-adminsdk-x094e-7eb1d468d8.json")
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://captcha-login-386ec-default-rtdb.firebaseio.com/'
        })

        # Reference to the 'users' node in the Firebase Realtime Database
        users_ref = db.reference('users')

        # Query to search for the user with the provided username and password
        query = users_ref.order_by_child('username').equal_to(username).limit_to_first(1)
        result = query.get()

        # Check if the user exists and if the password matches
        for user_key, user_data in result.items():
            if user_data.get('password') == password:
                print("User credentials are correct.")
                print("Retrieving all row records for the user:")
                username = user_data["username"]
                password = user_data["password"]
                cap_username = user_data["cap_username"]
                cap_password = user_data["cap_password"]
                captcha_process(cap_username,cap_password)
        else:
            print("Invalid username or password.")
    except Exception as e:
        print("An error occurred:", e)

# Get input from the user
username = input("Enter username: ")
password = input("Enter password: ")

# Call the function to check credentials and retrieve records
check_user_credentials(username, password)
