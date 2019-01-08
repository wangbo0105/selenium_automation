*** Settings ***
Documentation   Store page jump validation
Test Setup  open my browser
Test Teardown  close my browser
Library  CommonLibrary
Library  StoreLibrary

*** Test Cases ***
go store_page
    go store
    is store page
