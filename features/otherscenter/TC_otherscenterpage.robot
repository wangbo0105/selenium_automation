*** Settings ***
Documentation   otherscenter page test
Suite Setup  Run Keywords  load veer  AND  login  ${usrname}  ${password}
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.OthersCenterLibrary
Library  services.PersonalLibrary
Library  services.LoginLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
go otherscenter page from username of listpage
    Given click username from list
    Then should be otherscenter page

go otherscenter page from username of content detail page
    Given click content
    Then click username from list
    Then should be otherscenter page

change tab home
    Given click username from list
    Then switch nav tab  主页
    Then check tabs is selected  主页

change tab upload
    Given click username from list
    Then switch nav tab  作品
    Then check tabs is selected  作品

change tab collection
    Given click username from list
    Then switch nav tab  合辑
    Then check tabs is selected  合辑
