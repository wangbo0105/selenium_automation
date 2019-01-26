*** Settings ***
Documentation   Upload page smoke test
Test Setup  load veer
Suite Teardown  close my browser
Library  services.UploadLibrary
Library  services.CommonLibrary

*** Test Cases ***
go upload page
    Given go page  upload
    Then should be upload page