*** Settings ***
Documentation   Upload page jump validation
Library  UploadLibrary

*** Test Cases ***
go upload_page
    open my browser
    go upload
    close my browser
