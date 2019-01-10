*** Settings ***
Documentation   Blog page jump validation
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.BlogLibrary

*** Test Cases ***
go blog_page
    Given go blog
    Then is blog page
