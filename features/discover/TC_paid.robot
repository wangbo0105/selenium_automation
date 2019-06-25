*** Settings ***
Documentation   top paid test
Suite Setup  Run Keywords  load veer  AND  login  ${usrname}  ${password}
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.HomeLibrary
Library  services.CommonLibrary
Library  services.PaidLibrary
Library  services.LoginLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
go top-paid page
    When click feeds item  付费专区
    Then should be paid page

go top-paid content detail page
    When click feeds content item  付费专区
    Then should be paid content page
