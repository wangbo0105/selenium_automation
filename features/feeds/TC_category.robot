*** Settings ***
Documentation   recommended test
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.HomeLibrary
Library  services.CommonLibrary
Library  services.VideoLibrary


*** Test Cases ***
feeds category Travel jump
    Given click feeds item  旅游
    Then check category page  旅游

feeds category Travel content jump
    Given click feeds content item  旅游
    Then should be video detail page

feeds category Documentary jump
    Given click feeds item  记录
    Then check category page  记录

category page tab switch
    Given go page  video
    When click category tab  旅游
    Then check category page  旅游
    When click category tab  记录
    Then check category page  记录


