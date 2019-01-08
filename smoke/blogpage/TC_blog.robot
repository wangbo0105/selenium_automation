*** Settings ***
Documentation   Blog page jump validation
Test Setup  open my browser
Test Teardown  close my browser
Library  CommonLibrary
Library  BlogLibrary

*** Test Cases ***
go blog_page
    go blog
    is blog page
