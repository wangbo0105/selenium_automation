*** Settings ***
Documentation   Store page jump validation
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.StoreLibrary

*** Test Cases ***
go store_page
    Given go store
    Then is store page
