*** Settings ***
Documentation    follow smoke test
Suite Setup  Run Keywords  load veer  AND  login  ${usrname}  ${password}
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.FollowLibrary
Library  services.LoginLibrary
Library  services.HomeLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
follow creater in content detail page
    Given click feeds content item  精选图片
    When click follow btn
    Then check follow state in detail page  ${True}
    Then check followed num  1
    And check follow state in following page  ${True}

following page :cancel follw alert select unfollow
    Given go following page
    Then click followed btn
    When choose follow operation  ${True}
    Then check follow state in following page  ${False}

clear following
    Given go following page
    Then clear following