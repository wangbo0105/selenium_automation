*** Settings ***
Documentation   video test
Test Setup  load veer
Suite Teardown  close my browser
Library  services.VideoLibrary
Library  services.CommonLibrary

*** Test Cases ***
go video_page
    Given go page  video
    Then should be video page

go video detail page
    Given go page  video
    When click item  视频作品
    Then should be video detail page
