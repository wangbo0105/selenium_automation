*** Settings ***
Documentation    bookmark smoke test
Suite Setup  Run Keywords  load veer  AND  login  ${usrname}  ${password}
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
    Given bookmark in detail page
    Then check the bookmark has been added

remove bookmark in detail page
    Given remove bookmark in detail
    Then check remove bookmark in detail
    And check remove bookmark in personal