*** Settings ***
Documentation   Upload page jump validation
Test Setup  open my browser
Test Teardown  close my browser
Library  UploadLibrary
Library  CommonLibrary

*** Test Cases ***
go upload_page
    go upload
    is upload page