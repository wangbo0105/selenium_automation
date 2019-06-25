*** Settings ***
Documentation   video test
Suite Setup  Run Keywords  load veer  AND  login  ${usrname}  ${password}
Test Setup  load veer
Suite Teardown  close my browser
Library  services.VideoLibrary
Library  services.CommonLibrary
Library  services.LoginLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
Navigation bar video home page jump
    Given go page  video
    Then should be expected page  video
    And url should be matching  video

Video details page jump
    Given go page  video
    When video click item  video_content
    Then should be video detail page

More video jumps
    Given go page  video
    Then video click item  video_content
    And get more video href
    When video click item  video_content
    Then should be more video page