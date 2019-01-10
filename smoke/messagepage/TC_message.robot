*** Settings ***
Documentation   Message page jump validation
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.MessageLibrary
Library  services.LoginLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
go message_page
    When login  ${usrname}   ${password}
    Then go message
    Then is message page
