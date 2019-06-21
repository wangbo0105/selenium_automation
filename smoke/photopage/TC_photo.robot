*** Settings ***
Documentation   photo page smoke test
Suite Setup  Run Keywords  load veer  AND  login  ${usrname}  ${password}
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.PhotoLibrary
Library  services.HomeLibrary
Library  services.LoginLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
go photo page
    Given go page  photo
    Then should be expected page  photo
    And url should be matching  photo

go photo detail page
    Given go page  photo
    Then photo click item  photo_content
    Then should be photo detail page