*** Settings ***
Documentation   Blog page jump validation
Library  BlogLibrary

*** Test Cases ***
go blog_page
    open my browser
    go blog
    close my browser
