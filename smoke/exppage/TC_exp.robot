*** Settings ***
Documentation   Experience page jump validation
Test Setup  open my browser
Test Teardown  close my browser
Library  CommonLibrary
Library  ExpLibrary

*** Test Cases ***
go exp page
    go exp
    is exp page

go exp detail page
    go exp
    go exp detail
    is exp detail page
