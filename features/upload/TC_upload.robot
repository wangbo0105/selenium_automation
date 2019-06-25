*** Settings ***
Documentation   Upload demo test
Suite Setup  Run Keywords  load veer  AND  login  ${usrname}  ${password}
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.UploadLibrary
Library  services.LoginLibrary
Resource  ../../testdata/userdata.robot


*** Test Cases ***
Select upload - upload one video 
    Given select upload
    When upload one photo
    js upload
    Then is upload page

   
      
   