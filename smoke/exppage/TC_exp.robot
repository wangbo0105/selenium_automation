*** Settings ***
Documentation   experience smoke test
Suite Setup  Run Keywords  load veer  AND  login  ${usrname}  ${password}
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.ExpLibrary
Library  services.LoginLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
Interactive experience home page jump verification
    Given go page  experience
    Then should be expected page  experience
    And url should be matching  experience

Interactive experience details page jump verification
    Given go page  experience
    When exp click item  learn_more
    Then should be experience details page
