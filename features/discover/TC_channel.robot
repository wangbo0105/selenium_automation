*** Settings ***
Documentation   recommended test
Suite Setup  load veer
Test Setup  go page  discover
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.HomeLibrary
Library  services.CommonLibrary
Library  services.VideoLibrary
Library  services.LoginLibrary
Resource  ../../testdata/userdata.robot


*** Test Cases ***
feeds category Travel jump
    Given click feeds item  动画
    Then check category page  动画

feeds category Travel content jump
    Given click feeds content item  动画
    Then should be video detail page

category page tab switch
    Given go page  video
    When click category tab  旅游
    Then check category page  旅游
    When click category tab  记录
    Then check category page  记录

turnpage in category tab
    Given click feeds item  动画
    Then click category tab  旅游
    When turn current tab page  next_page
    Then check page turned  page_2
    When turn current tab page  last_page
    Then check page turned  page_1
    When turn current tab page  page_3
    Then check page turned  page_3