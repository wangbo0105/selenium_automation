*** Settings ***
Documentation    bookmark smoke test
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.BookMarkLibrary
Library  services.LoginLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
add photos bookmark
    Given login  ${usrname}   ${password}
    When bookmark photos
    Then check the photo bookmark has been added

clear bookmarks data
    Given go bookmark tab
    Then clear bookmark data
