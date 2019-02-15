*** Settings ***
Documentation   blog smoke test
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary


*** Test Cases ***
go blog page
    Given go page  blog
    Then should be expected page  blog
    And url should be matching  blog
