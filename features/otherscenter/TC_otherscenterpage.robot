*** Settings ***
Documentation   otherscenter page test
Suite Setup  Run Keywords  load veer  AND  login  ${usrname}  ${password}
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.OthersCenterLibrary
Library  services.PersonalLibrary
Library  services.LoginLibrary
Library  services.PhotoLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
go othercenter page : from content detail
    Given go page  photo
    Then photo click item  photo_content
    Given go other center
    Then should be other center page

change tab home
    Given go page  photo
    And photo click item  photo_content
    Then go other center
    Then switch nav tab  主页
    Then check tabs is selected  主页
    Then switch nav tab  作品
    Then check tabs is selected  作品
    Then switch nav tab  合辑
    Then check tabs is selected  合辑
