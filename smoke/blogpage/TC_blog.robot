*** Settings ***
Documentation   blog smoke test
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.ExternalLibrary

*** Test Cases ***
go blog page
    Given go page  blog
    Then should be blog page
