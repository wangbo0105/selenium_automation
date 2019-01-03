*** Settings ***
Documentation   Experience page jump validation
Library  ExpLibrary

*** Test Cases ***
go exp page
    open my browser
    go exp
    close my browser

go exp detail page
    open my browser
    go exp
    go exp detail
    close my browser
