*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Register Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kallekolme  kallenkolmass
    Output Should Contain  New user registered


*** Keywords ***
Create User And Input Register Command
    Create User  kalle  kallekalle
    Input Register Command

