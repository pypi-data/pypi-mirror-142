from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import Fore

import zipfile
import requests
import time
import sys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')

def translate(text,translate_to = "en"):
    try:
        driver = Chrome("chromedriver.exe", options=chrome_options)
    except Exception as e:
        print(f"{Fore.RED}[-] chromedriver exe file was not found in path{Fore.RESET}")
        if input(f"{Fore.BLUE}[*] {Fore.YELLOW}do you want to install the last stable version now? ({Fore.GREEN}y{Fore.YELLOW}/{Fore.RED}n{Fore.YELLOW}){Fore.RESET}").lower() == "y":
            last_version = requests.get("https://chromedriver.storage.googleapis.com/LATEST_RELEASE").text
            print(f"{Fore.BLUE}[+] {Fore.GREEN}found latest stable version |{last_version}|\n{Fore.BLUE}[*]{Fore.YELLOW}searching for last stable version chromedriver exe file")
            if sys.platform.startswith("win"):
                href = f"https://chromedriver.storage.googleapis.com/{last_version}/chromedriver_win32.zip"
            elif sys.platform.startswith("linux"):
                href = f"https://chromedriver.storage.googleapis.com/{last_version}/chromedriver_linux64.zip"
            else:
                print(f"{Fore.RED}[-] {Fore.LIGHTRED_EX}this installation process is only supported on linux and windows!")
                print(f"{Fore.BLUE}[*] {Fore.YELLOW}you can install chromedriver from this url: https://chromedriver.storage.googleapis.com/index.html?path={last_version}/")
                raise e
            print(f"{Fore.BLUE}[+] {Fore.GREEN}last stable version chromedriver file found|{last_version}|\n{Fore.BLUE}[*]{Fore.YELLOW}starting downloading zip")
            f = open("chromedriver.zip","wb")
            f.write(requests.get(href).content)
            f.close()
            print(f"{Fore.BLUE}[+] {Fore.GREEN}zip download finished\n{Fore.BLUE}[*]{Fore.YELLOW}starting extracting process for zip zip file")
            with zipfile.ZipFile("chromedriver.zip", 'r') as zip_ref:
                zip_ref.extractall("")
            print(f"{Fore.GREEN}[+] done! chromedriver.exe should be in this path (folder)")
            print(f"{Fore.YELLOW}[*] checking for chromedriver please wait...")
            time.sleep(1)
            try:
                driver = Chrome("chromedriver.exe", options=chrome_options)
                print(f"{Fore.GREEN}[+] starting function again!")
            except:
                print(f"{Fore.RED}[-] error happened you will need to install chromedriver.exe from this link: {Fore.BLUE}https://chromedriver.storage.googleapis.com/index.html?path={last_version}/")
                raise e

    driver.get(f"https://translate.google.co.il/?sl=auto&tl={translate_to}&text={text}")

    while True:
        try:
            text = WebDriverWait(driver, 0.1).until(EC.presence_of_element_located((By.XPATH,"/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div[6]/div/div[1]/span[1]/span/span")))
            return text.text
        except:
            pass