*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Register Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kallekolme  kallenkolmass
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kallekalle
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  kallekalle
    Output Should Contain  Username has to be at least 3 characters long

Register With Valid Username And Too Short Password
    Input Credentials  kallee  kallist
    Output Should Contain  Password has to be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kallekalle  kallekallekalle
    Output Should Contain  New user registered

*** Keywords ***
Create User And Input Register Command
    Create User  kalle  kallekalle
    Input Register Command

