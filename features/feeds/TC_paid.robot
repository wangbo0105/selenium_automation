*** Settings ***
Documentation   top paid test
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.HomeLibrary
Library  services.CommonLibrary
Library  services.PaidLibrary

*** Test Cases ***
go top-paid page
    When click feeds item  付费专区
    Then should be paid page

go top-paid content detail page
    When click feeds content item  付费专区
    Then should be paid content page
