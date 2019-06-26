*** Settings ***
Documentation   discover test
Suite Setup  load veer
Test Setup  go page  logo
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.HomeLibrary

*** Test Cases ***
go discover index page
    Given go page  discover
    Then should be expected page  discover
    And url should be matching  discover

discover tab : Video
    Given select discover item  Video
    Then should be expected page  video

discover tab : Photo
    Given select discover item  Photo
    Then should be expected page  photo

discover tab : Experience
    Given select discover item  Experience
    Then should be expected page  experience