*** Settings ***
Documentation   Experience test
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.ExpLibrary
Library  services.LoginLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
Navigation bar interactive experience home page jump
    When go page  experience
    Then should be expected page  experience
    And url should be matching  experience

Upload page - learn more interactive experience home page jump
    Given go page  upload
    When exp click item  upload_learn_more
    Then should be expected page  experience
    And url should be matching  experience

Banner-Tab- learn more interactive experience play details page jump
    Given go page  experience
    When exp click item  learn_more
    Then should be experience details page

Banner-Tab-VR story switch
    Given go page  experience
    When exp click item  VR_story
    Then check banner tab is selected  VR_story

Banner-Tab-VRlog diary case switch
    Given go page  experience
    When exp click item  VRlog_diary_case
    Then check banner tab is selected  VRlog_diary_case

Banner-Tab- restaurant panorama case switch
    Given go page  experience
    When exp click item  VR_story
    And exp click item  restaurant_panorama_case
    Then check banner tab is selected  restaurant_panorama_case

Seth VeeR's home page jumps to verify
    Given go page  experience
    When exp click item  Seth_veer_page
    Then should be Seth personal page

Experience the upload page jump immediately
    Given go page  experience
    When exp click item  experience_immediately
    Then check the login alert is displayed
    And login  ${usrname}  ${password}
    Then should be expected page  upload