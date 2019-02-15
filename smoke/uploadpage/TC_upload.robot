*** Settings ***
Documentation   Upload page smoke test
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary

*** Test Cases ***
go upload page
    Given go page  upload
    Then should be expected page  upload
    And url should be matching  upload