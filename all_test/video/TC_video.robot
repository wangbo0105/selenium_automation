*** Settings ***
Documentation   video test
Test Setup  load veer
Suite Teardown  close my browser
Library  services.VideoLibrary
Library  services.CommonLibrary

*** Test Cases ***
go video_page
    Given go page  视频
    Then is video page

go video detail page
    Given go page  视频
    Then go video detail
    Then is video detail page
