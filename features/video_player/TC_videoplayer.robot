*** Settings ***
Documentation   video player test
Test Setup  load veer
Suite Teardown  close my browser
Library  services.VideoLibrary
Library  services.VideoPlayerLibrary
Library  services.CommonLibrary

*** Test Cases ***
#
#auto play video
#    Given go video player
#    Then check video state  play
#
#
#Manual pause&play video
#    Given go video player
#    When pause video
#    Then check video state  pause
#    When play video
#    Then check video state  play
#
#Switching resolution
#    Given go video player
#    Then switch resolution  720p
#    And check current resolution  720p
#    Then switch resolution  1080p
#    And check current resolution  1080p
#    Then switch resolution  1440p
#    And check current resolution  1440p
#    Then switch resolution  2160p
#    And check current resolution  2160p

switch fullscreen
    Given go video player
    When switch fullscreen
    Then check fullscreen state  ${true}
    When switch fullscreen
    Then check fullscreen state  ${false}