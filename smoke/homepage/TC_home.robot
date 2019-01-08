*** Settings ***
Documentation   Home page jump validation
Test Setup  open my browser
Test Teardown  close my browser
Library  CommonLibrary
Library  HomeLibrary

*** Test Cases ***
go home_page
    is home page