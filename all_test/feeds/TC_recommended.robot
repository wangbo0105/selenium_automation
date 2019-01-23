*** Settings ***
Documentation   recommended test
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.HomeLibrary
Library  services.CommonLibrary

*** Test Cases ***
go recommended page
    Given go recommended page
    Then is recommended page

go recommended content detail page
    Given go recommended content detail page
    Then is recommended content detail page

recommended show more
    Given show more recommended
    Then is recommended show more