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
Library  services.PhotoLibrary
Library  services.VideoLibrary
Library  services.ExpLibrary
Library  services.HomeLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
go personal center like tab
    Given go liked tab
    Then check tabs is selected  喜欢

add photos like
    Given go page  photo
    Then photo_click_item  photo_content
    When add content like
    Then check content is liked   liked_photo

remove liked content
    Given go liked tab
    Then click liked content in liked tab  liked_photo
    When remove content liked
    Then check liked content is remove in detail
    And check liked content is removed in liked tab  liked_photo

add videos like
    Given go page  video
    Then video_click_item  video_content
    When add content like
    Then check content is liked   liked_video

add experiences like
    Given go page  experience
    Then exp click item  learn_more
    When add content like
    Then check content is liked   liked_experience

add collection_box like
    Given go follower homepage
    Then switch nav tab  合辑
    And go collection box detail
    When add content like
    Then check content is liked   liked_collection

remove collection_box like
    Given go follower homepage
    Then switch nav tab  合辑
    And go collection box detail
    When remove content liked
    Then check liked content is remove in detail
    And check liked content is removed in liked tab  liked_collection

clear all liked content
    Given go liked tab
    Then clear all liked content