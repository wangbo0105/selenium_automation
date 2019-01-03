*** Settings ***
Documentation   Message page jump validation
Library  MessageLibrary

*** Test Cases ***
go message_page
    open my browser
    login  veerqa@veer.tv   123456
    go message
    close my browser
