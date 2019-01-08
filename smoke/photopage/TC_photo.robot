*** Settings ***
Documentation   Photo page jump validation
Test Setup  open my browser
Test Teardown  close my browser
Library  CommonLibrary
Library  PhotoLibrary

*** Test Cases ***
go photo_page
    go photo
    is photo page

go photo detail page
    go photo
    go photo detail
