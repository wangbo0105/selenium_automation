*** Settings ***
Documentation   Upload test
Suite Setup  Run Keywords  load veer  AND  login  ${usrname}  ${password}
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.UploadLibrary
Library  services.LoginLibrary
Resource  ../../testdata/stg_userdata.robot


*** Test Cases ***
go upload page
    Given go page  upload
    Then should be expected page  upload
    And url should be matching  upload

   
      
   