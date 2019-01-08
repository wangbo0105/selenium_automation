*** Settings ***
Documentation   Video page jump validation
Test Setup  open my browser
Test Teardown  close my browser
Library  VideoLibrary
Library  CommonLibrary

*** Test Cases ***
go video_page
    go video
    is video page

go video detail page
    go video
    go video detail
    is video detail page
