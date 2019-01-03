*** Settings ***
Documentation   Login page test
Library  LoginLibrary

*** Test Cases ***
login
    open my browser
    login   ${usrname}  ${password}
    close my browser

log out
    open my browser
    login   ${usrname}  ${password}
    logout
    close my browser


*** Variables ***
${usrname}       veerqa@veer.tv
${password}      123456
