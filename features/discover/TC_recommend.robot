*** Settings ***
Documentation   recommended test
Suite Setup  load veer
Test Setup  go page  discover
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.HomeLibrary

*** Test Cases ***
go recommend index page
    Given go recommend page
    Then should be recommended page

go recommended content detail page
    Given go recommended content detail page
    Then should be content detail page

recommended show more
    Given click more recommended
    Then check recommended show more successful