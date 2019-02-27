*** Settings ***
Documentation    content like smoke test
Suite Setup  Run Keywords  load veer  AND   login  ${usrname}  ${password}
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.LikeLibrary
Library  services.LoginLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
add photos like
    When add photos like
    Then check the photo is liked

clear like
    When go liked tab
    Then clear like
