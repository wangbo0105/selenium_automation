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
    Then close bookmark alert
    Then check bookmark in detail page
    Then go bookmark tab
    Then check bookmark in personal page

clear bookmark
    Given go bookmark tab
    Then clear bookmark
