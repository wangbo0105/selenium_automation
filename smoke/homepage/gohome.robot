*** Settings ***
Documentation   Home page jump validation
Library  BrowserLibrary

*** Test Cases ***
go home_page
    open my browser
    close my browser