*** Settings ***
Documentation   Home page jump validation
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.HomeLibrary

*** Test Cases ***
go home_page
    Then is home page