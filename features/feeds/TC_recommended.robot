*** Settings ***
Documentation   recommended test
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.HomeLibrary
Library  services.CommonLibrary

*** Test Cases ***
go recommended page
    Given click feeds item  推荐
    Then should be recommended page

go recommended content detail page
    Given go recommended content detail page
    Then should be recommended content detail page

recommended show more
    Given click more recommended
    Then check recommended show more successful