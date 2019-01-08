*** Settings ***
Documentation   Message page jump validation
Test Setup  open my browser
Test Teardown  close my browser
Library  CommonLibrary
Library  MessageLibrary
Library  LoginLibrary

*** Test Cases ***
go message_page
    login  veerqa@veer.tv   123456
    go message
    is message page
