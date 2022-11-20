*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  janika  janika123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ab  abcd1234
    Output Should Contain  väh. 3 merkkiä

Register With Valid Username And Too Short Password
    Input Credentials  abcdabcd  abc234
    Output Should Contain  väh. 8 merkkiä

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  abcdabcd  abcdabcd
    Output Should Contain  ei pelkkiä kirjaimia

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command