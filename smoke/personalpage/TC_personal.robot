*** Settings ***
Documentation   Personal center page jump validation
Test Setup  open my browser
Test Teardown  close my browser
Library  CommonLibrary
Library  PersonalLibrary
Library  LoginLibrary

*** Test Cases ***
go personal_page
    login  veerqa@veer.tv   123456
    go personal
    is personal page
