*** Settings ***
Documentation    bookmark smoke test
Suite Setup  load veer and login    ${usrname}   ${password}
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.BookMarkLibrary
Library  services.LoginLibrary
Library  services.PersonalLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
go bookmark tab
    When go bookmark tab
    Then check tabs is selected  VR书签

add bookmark in detail page
    When bookmark in detail page
    Then check the bookmark has been added

add bookmark in cover page
    When bookmark in cover page
    Then check the bookmark has been added
