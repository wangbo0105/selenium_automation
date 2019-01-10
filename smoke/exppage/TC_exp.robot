*** Settings ***
Documentation   Experience page jump validation
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.ExpLibrary

*** Test Cases ***
go exp page
    Given go exp
    Then is exp page

go exp detail page
    Given go exp
    Then go exp detail
    Then is exp detail page
