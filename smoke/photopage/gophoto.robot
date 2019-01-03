*** Settings ***
Documentation   Photo page jump validation
Library  PhotoLibrary

*** Test Cases ***
go photo_page
    open my browser
    go photo page
    close my browser

go photo detail page
    open my browser
    go photo page
    go photo detail page
    close my browser
