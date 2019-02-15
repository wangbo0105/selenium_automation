*** Settings ***
Documentation   video test
Test Setup  load veer
Suite Teardown  close my browser
Library  services.VideoLibrary
Library  services.CommonLibrary

*** Test Cases ***
go video_page
    Given go page  video
    Then should be expected page  video
    And url should be matching  video

go video detail page
    Given go page  video
    When video click item  video_content
    Then should be video detail page