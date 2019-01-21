*** Settings ***
Documentation    content like test
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.LikeLibrary
Library  services.LoginLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
photo_like
    Given login  ${usrname}   ${password}
    When photo content like
    Then check liked
