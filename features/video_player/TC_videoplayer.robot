*** Settings ***
Documentation   video player test
Test Setup  load veer
Suite Teardown  close my browser
Library  services.VideoLibrary
Library  services.VideoPlayerLibrary
Library  services.CommonLibrary

*** Test Cases ***

auto play video
    Given go video player
    Then check video state  play


Manual pause&play video
    Given go video player
    When pause video
    Then check video state  pause
    When play video
    Then check video state  play
