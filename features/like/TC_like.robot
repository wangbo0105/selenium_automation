*** Settings ***
Documentation    like test
Suite Setup  Run Keywords  load veer  AND  login  ${usrname}  ${password}
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.FollowLibrary
Library  services.CollectionLibrary
Library  services.LikeLibrary
Library  services.LoginLibrary
Library  services.PersonalLibrary
Library  services.HomeLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
go personal center like tab
    Given go liked tab
    Then check tabs is selected  喜欢

add photos like
    Given click feeds content item  精选图片
    When add content like
    Then check content is liked   liked_photo

remove liked content
    Given go liked tab
    Then click liked content in liked tab  liked_photo
    When remove content liked
    Then check liked content is remove in detail
    And check liked content is removed in liked tab  liked_photo

add videos like
    Given click feeds content item  精选视频
    When add content like
    Then check content is liked   liked_video

add experiences like
    Given click feeds content item  精选互动
    When add content like
    Then check content is liked   liked_experience

add collection_box like
    Given go follower page
    Then go follower homepage
    And switch nav tab  合辑
    And go collection box detail
    Given add content like
    Then check content is liked   liked_collection


clear all liked content
    Given go liked tab
    Then clear all liked content