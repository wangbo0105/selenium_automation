*** Settings ***
Documentation   featured test
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.HomeLibrary
Library  services.CommonLibrary
Library  services.PhotoLibrary
Library  services.VideoLibrary
Library  services.ExpLibrary

*** Test Cases ***
featured photo page jump
    When click feeds item  精选图片
    Then should be expected page  photo

featured photo content jump
    When click feeds content item  精选图片
    Then should be photo detail page

featured video page jump
    When click feeds item  精选视频
    Then should be expected page  video

feature video content jump
    When click feeds content item  精选视频
    Then should be video detail page

featured experience content jump
    When click feeds content item  精选互动
    Then should be experience details page

featured content list turned right
    When turning list  right
    Then check turned right
