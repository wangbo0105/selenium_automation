*** Settings ***
Documentation   video test
Test Setup  load veer
Suite Teardown  close my browser
Library  services.VideoLibrary
Library  services.CommonLibrary

*** Test Cases ***
go video_page
    Given go video
    Then is video page

go video detail page
    Given go video
    Then go video detail
    Then is video detail page
