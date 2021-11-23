*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kallek
    Set Password  kallekaksi2
    Set Password Confirmation  kallekaksi2
    Submit Registration

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kallekaksi2
    Set Password Confirmation  kallekaksi2
    Submit Registration
    Registration Should Fail With Message  Username has to be at least 3 characters long
    
Register With Valid Username And Too Short Password
    Set Username  kallek
    Set Password  kallek7
    Set Password Confirmation  kallek7
    Submit Registration
    Registration Should Fail With Message  Password has to be at least 8 symbols long and can't contain only letters


Register With Nonmatching Password And Password Confirmation
    Set Username  kallek
    Set Password  kallek7
    Set Password Confirmation  kallek6
    Submit Registration
    Registration Should Fail With Message  Passwords did not match

*** Keywords ***
Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Registration
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}


Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Create User And Go To Register Page
    Create User  kalle  kallekalle
    Go To Register Page
    Register Page Should Be Open
