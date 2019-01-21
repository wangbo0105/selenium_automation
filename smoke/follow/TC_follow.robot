*** Settings ***
Documentation    content follow test
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
    Then check follow