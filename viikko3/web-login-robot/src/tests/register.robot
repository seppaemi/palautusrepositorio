*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  janika
    Set Password  janika123
    Set Password Confirmation  janika123
    Submit Register Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ab
    Set Password  abcd1234
    Set Password Confirmation  abcd1234
    Submit Register Credentials
    Register Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  abcd
    Set Password  abc
    Set Password Confirmation  abc
    Submit Register Credentials
    Register Should Fail

Register With Nonmatching Password And Password Confirmation
    Set Username  abcd
    Set Password  abcd1234
    Set Password Confirmation  abc
    Submit Register Credentials
    Register Should Fail

Login After Successful Registration
    Set Username  janika
    Set Password  janika123
    Set Password Confirmation  janika123
    Submit Register Credentials
    Go To Login Page
    Set Username  janika
    Set Password  janika123
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  ja
    Set Password  janika123
    Set Password Confirmation  janika123
    Submit Register Credentials
    Register Should Fail
    Go To Login Page
    Set Username  ja
    Set Password  janika123
    Submit Login Credentials
    Login Should Fail

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Register Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Register Should Fail
    Register Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Login Should Fail
    Login Page Should Be Open