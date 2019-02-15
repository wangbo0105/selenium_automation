*** Settings ***
Documentation   message page smoke test
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary

Library  services.LoginLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
go message page
    Given login  ${usrname}   ${password}
    When go page  message
    Then should be expected page  message
    And url should be matching  message
