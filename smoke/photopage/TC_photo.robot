*** Settings ***
Documentation   Photo page jump validation
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.PhotoLibrary

*** Test Cases ***
go photo_page
    Given go page  全景图
    Then is photo page

go photo detail page
    Given go page  全景图
    Then click item  图片作品
    Then is photo detail page
