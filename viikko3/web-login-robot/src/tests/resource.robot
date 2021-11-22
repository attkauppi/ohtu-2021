*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py
Test Setup  Setup chromedriver

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  chrome
${DELAY}  0.5 seconds
${HOME URL}  http://${SERVER}
${LOGIN URL}  http://${SERVER}/login
${REGISTER URL}  http://${SERVER}/register
${EXECDIR}  /usr/local/bin/chromedriver

*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Login Page Should Be Open
    Title Should Be  Login

Main Page Should Be Open
    Title Should Be  Ohtu Application main page

Go To Login Page
    Go To  ${LOGIN URL}

Create Webdriver    Chrome    executable_path=C:/WebDrivers/chromedriver.exe

Setup chromedriver
    Set Environment Variable  chrome  ${EXECDIR}

