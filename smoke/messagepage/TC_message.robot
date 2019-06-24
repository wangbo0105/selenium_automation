*** Settings ***
Documentation   message page smoke test
Suite Setup  Run Keywords  load veer  AND  login  ${usrname}  ${password}
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary

Library  services.LoginLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
go message page
    Given go page  message
    Then should be expected page  message
    And url should be matching  message
