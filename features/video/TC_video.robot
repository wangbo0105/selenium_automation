*** Settings ***
Documentation   video test
Test Setup  load veer
Suite Teardown  close my browser
Library  services.VideoLibrary
Library  services.CommonLibrary

*** Test Cases ***
Navigation bar video home page jump
    Given go page  video
    Then should be video page

Video details page jump
    Given go page  video
    When video click item  video_content
    Then should be video detail page

More video jumps
    Given go page  video
    Then video click item  video_content
    When video click item  more_video
    Then should be more video page
