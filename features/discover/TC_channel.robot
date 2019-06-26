*** Settings ***
Documentation   channel test
Suite Setup  load veer
Test Setup  go page  discover
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.HomeLibrary

*** Test Cases ***
channel list select
    Given select channel list  动画
    Then check current channel  动画

channel list switch
    Given select channel list  动画
    Then check current channel  动画
    Then select channel list  付费专区
    Then check current channel  付费专区

channel content jump：动画
    Given select channel list  动画
    When go channel content detail page  动画
    Then should be content detail page

channel content jump: 付费专区
    Given select channel list  付费专区
    When go channel content detail page  付费专区
    Then should be content detail page

turnpage in category tab
    Given select channel list  付费专区
    Then turn channel page  right
    And turn channel page  left
