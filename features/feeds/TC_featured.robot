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
    Given click feeds item  精选图片
    Then should be expected page  photo

featured photo content jump
    Given click feeds content item  精选图片
    Then should be photo detail page

featured video page jump
    Given click feeds item  精选视频
    Then should be expected page  video

feature video content jump
    Given click feeds content item  精选视频
    Then should be video detail page

featured experience content jump
    Given click feeds content item  精选互动
    Then should be experience details page

featured content list turned wrapper
    Given turning list  right
    Then check turned wrapper  right
    Given turning list  left
    Then check turned wrapper  left
