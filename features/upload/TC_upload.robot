*** Settings ***
Documentation   Upload demo test
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.UploadLibrary
Library  services.LoginLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
Select upload - upload one video 
    Given login  ${usrname}  ${password}
    And select upload
    When upload one photo
    Then is upload page
   