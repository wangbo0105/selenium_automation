*** Settings ***
Documentation    share test
Suite Setup  Run Keywords  load veer  AND  login  ${usrname}  ${password}
Test Setup  refresh_current_window
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
    Given go page  video
    Then video click item  video_content
    When click channels  wechat
    Then check channels results  wechat

share: moment
    Given click channels  moment
    Then check channels results  moment

share: weibo
    Given click channels  weibo
    Then check channels results  weibo

share: qq
    Given click channels  qq
    Then check channels results  qq

share: qq_zone
    Given click channels  qq_zone
    Then check channels results  qq_zone

cope content link
    Given click channels  content_link
    Then check share link  content_link

cope Html embed link
    Given click channels  html_embed_link
    Then check share link  html_embed_link
