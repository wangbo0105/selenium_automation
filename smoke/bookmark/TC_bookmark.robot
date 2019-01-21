*** Settings ***
Documentation    content bookmark test
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.BookMarkLibrary
Library  services.LoginLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
photo_bookmark
    Given login  ${usrname}   ${password}
    When photo bookmark
    Then check bookmark

clear bookmark
    Given go page  VR书签
    Then clear bookmark
