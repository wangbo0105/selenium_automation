*** Settings ***
Documentation   message page test
Suite Setup  Run Keywords  load veer  AND  login  ${usrname}  ${password}
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.MessageLibrary
Library  services.LoginLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
go message page from headerbar
    When go page  message
    Then should be expected page  message
    And url should be matching  message


go message page form see all
    Then hover_and_click_seeallmessage
    Then should be expected page  message
    And url should be matching  message