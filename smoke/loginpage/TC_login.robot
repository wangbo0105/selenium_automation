*** Settings ***
Documentation   Login page test
Test Setup  open my browser
Test Teardown  close my browser
Library  CommonLibrary
Library  LoginLibrary

*** Test Cases ***
login
    login   ${usrname}  ${password}
    is login

log out
    login   ${usrname}  ${password}
    logout
    is logout


*** Variables ***
${usrname}       veerqa@veer.tv
${password}      123456
