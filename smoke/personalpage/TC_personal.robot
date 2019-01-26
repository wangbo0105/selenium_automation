*** Settings ***
Documentation   Personal center smoke test
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.PersonalLibrary
Library  services.LoginLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
go personal page
    Given login  ${usrname}   ${password}
    When go personal center
    Then should be personal page
