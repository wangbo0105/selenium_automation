*** Settings ***
Documentation    follow smoke test
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.FollowLibrary
Library  services.LoginLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
follow creater
    Given login  ${usrname}   ${password}
    When follow creater
    Then check the creator is focused on success