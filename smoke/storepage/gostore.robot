*** Settings ***
Documentation   Store page jump validation
Library  StoreLibrary

*** Test Cases ***
go store_page
    open my browser
    go store
    close my browser
