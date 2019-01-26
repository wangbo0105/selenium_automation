*** Settings ***
Documentation   Store page smoke test
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.ExternalLibrary

*** Test Cases ***
go store page
    Given go page  store
    Then should be store page
