*** Settings ***
Documentation   Video page jump validation
Library  VideoLibrary

*** Test Cases ***
go video_page
    open my browser
    go video
    close my browser

go video detail page
    open my browser
    go video
    go video detail
    close my browser
