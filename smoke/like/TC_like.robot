*** Settings ***
Documentation    content like smoke test
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.LikeLibrary
Library  services.LoginLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
add photos like
    Given login  ${usrname}   ${password}
    When add photos like
    Then check the photo is liked
