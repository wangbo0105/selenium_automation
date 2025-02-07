*** Settings ***
Documentation   Experience test
Suite Setup  Run Keywords  load veer  AND  login  ${usrname}  ${password}
Test Setup  go page  experience
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.ExpLibrary
Library  services.LoginLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
Navigation bar interactive experience home page jump
    Then should be expected page  experience
    And url should be matching  experience

Upload page - learn more interactive experience home page jump
    Given go page  upload
    When exp click item  upload_learn_more
    Then should be expected page  experience
    And url should be matching  experience

Banner-Tab- learn more interactive experience play details page jump
    Given exp click item  learn_more
    Then should be experience details page

Banner-Tab-VR story switch
    Given exp click item  VR_story
    Then check banner tab is selected  VR_story

Banner-Tab-VRlog diary case switch
    Given exp click item  VRlog_diary_case
    Then check banner tab is selected  VRlog_diary_case

Banner-Tab- restaurant panorama case switch
    Given exp click item  VR_story
    And exp click item  restaurant_panorama_case
    Then check banner tab is selected  restaurant_panorama_case

Seth VeeR's home page jumps to verify
    Given exp click item  Seth_veer_page
    Then should be Seth personal page

Experience the upload page jump immediately
    Given exp click item  experience_immediately
    Then should be expected page  upload