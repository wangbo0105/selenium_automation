*** Settings ***
Documentation    like test
Suite Setup  Run Keywords  load veer  AND  login  ${usrname}  ${password}
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.LikeLibrary
Library  services.LoginLibrary
Library  services.PersonalLibrary
Library  services.PhotoLibrary
Library  services.HomeLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
go personal center like tab
    Given go liked tab
    Then check tabs is selected  喜欢

add photos like
    Given go page  photo
    Then photo click item  photo_content
    When add content like
    Then check content is liked   liked_photo

clear all liked content
    Given go liked tab
    Then clear all liked content
