*** Settings ***
Documentation   Upload page jump validation
Test Setup  load veer
Suite Teardown  close my browser
Library  services.UploadLibrary
Library  services.CommonLibrary

*** Test Cases ***
go upload_page
    Given go page  上传
    Then is upload page