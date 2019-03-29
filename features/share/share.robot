*** Settings ***
Documentation    share test
Suite Setup  Run Keywords  load veer  AND  login  ${usrname}  ${password}
Test Setup  load veer
Suite Teardown  close my browser
Library  services.FollowLibrary
Library  services.CollectionLibrary
Library  services.PersonalLibrary
Library  services.CommonLibrary
Library  services.ShareLibrary
Library  services.PhotoLibrary
Library  services.VideoLibrary
Library  services.LoginLibrary
Library  services.HomeLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
share: wchat
    Given click feeds content item  精选图片
    When click channels  wechat
    Then check channels results  wechat

share: moment
    Given click feeds content item  精选视频
    When click channels  moment
    Then check channels results  moment

share: weibo
    Given go follower homepage
    Then switch nav tab  合辑
    And go collection box detail
    When click channels  weibo
    Then check channels results  weibo

share: qq
    Given click feeds content item  精选互动
    When click channels  qq
    Then check channels results  qq

share: qq_zone
    Given click feeds content item  精选图片
    When click channels  qq_zone
    Then check channels results  qq_zone

cope content link
    Given click feeds content item  精选图片
    When click channels  content_link
    Then check share link  content_link

cope Html embed link
    Given click feeds content item  精选图片
    When click channels  html_embed_link
    Then check share link  html_embed_link
