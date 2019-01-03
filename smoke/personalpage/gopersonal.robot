*** Settings ***
Documentation   Personal center page jump validation
Library  PersonalLibrary

*** Test Cases ***
go personal_page
    open my browser
    login  veerqa@veer.tv   123456
    go personal
    close my browser
