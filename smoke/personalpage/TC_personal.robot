*** Settings ***
Documentation   Personal center page jump validation
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.PersonalLibrary
Library  services.LoginLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
go personal_page
    When login  ${usrname}   ${password}
    Then go personal
    Then is personal page
