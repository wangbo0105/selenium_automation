*** Settings ***
Documentation    follow feature test
Suite Setup  Run Keywords  load veer  AND  login  ${usrname}  ${password}
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.FollowLibrary
Library  services.LoginLibrary
Library  services.HomeLibrary
Library  services.OthersCenterLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
go following page
    Given go following page
    Then check current page is following page

go follower page
    Given go follower page
    Then check current page is follower page

follow creater in content detail page
    Given click feeds content item  精选图片
    When click follow btn
    Then check follow state in detail page  ${True}
    Then check followed num  1
    And check follow state in following page  ${True}

content page :cancel follw alert select cancle
    Then click feeds content item  精选图片
    When click followed btn
    And choose follow operation  ${False}
    Then check follow state in detail page  ${True}
    Then check followed num  1
    And check follow state in following page  ${True}

content page :cancel follw alert select unfollow
    Then click feeds content item  精选图片
    When click followed btn
    And choose follow operation  ${True}
    Then check follow state in detail page  ${False}
    Then check followed num  0
    And check follow state in following page  ${False}

follow creater in follower page
    Given go follower page
    When click follow btn
    Then check follow state in following page  ${True}
    And go following page
    Then check follow state in following page  ${True}

follower page :cancel follw alert select cancle
    Given go follower page
    When click followed btn
    And choose follow operation  ${False}
    Then check follow state in following page  ${True}

follower page :cancel follw alert select unfollow
    Given go follower page
    When click followed btn
    And choose follow operation  ${True}
    Then check follow state in following page  ${False}

follow creater in others center page
    Given follow creater in creater home page
    Then check follow state in following page  ${True}
    And go following page
    Then check follow state in following page  ${True}

following page :cancel follw alert select cancle
    Given go following page
    Then click followed btn
    When choose follow operation  ${False}
    Then check follow state in following page  ${True}

following page :cancel follw alert select unfollow
    Given go following page
    Then click followed btn
    When choose follow operation  ${True}
    Then check follow state in following page  ${False}

clear following
    Given go following page
    Then clear following