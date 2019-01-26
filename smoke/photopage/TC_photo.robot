*** Settings ***
Documentation   photo page smoke test
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.PhotoLibrary

*** Test Cases ***
go photo page
    Given go page  photo
    Then should be photo page

go photo detail page
    Given go page  photo
    Then photo click item  photo_content
    Then should be photo detail page
