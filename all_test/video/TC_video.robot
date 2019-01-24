*** Settings ***
Documentation   video test
Test Setup  load veer
Suite Teardown  close my browser
Library  services.VideoLibrary
Library  services.CommonLibrary

*** Test Cases ***
导航栏 视频首页跳转
    Given go page  视频
    Then is video page

视频详情页跳转
    Given go page  视频
    Then click item  视频作品
    Then is video detail page

更多视频跳转
    Given go page  视频
    Then click item  视频作品
    Then get more video href
    Then click item  更多视频
    Then is more video page
