*** Settings ***
Documentation   Home smoke test
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.HomeLibrary

*** Test Cases ***
go home page
    Given go page  logo
    Then should be home page