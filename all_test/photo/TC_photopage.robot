*** Settings ***
Documentation   Photo page test
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.PhotoLibrary

*** Test Cases ***
go photo mainpage
    Given go page  全景图
    Then is photo page

go photo content detail page
    Given go page  全景图
    Then click item  图片作品
    Then is photo detail page

select featured tab
    Given go page  全景图
    Then click item  featured
    Then is selected banner tab  featured

select popular tab
    Given go page  全景图
    Then click item  popular
    Then is selected banner tab  popular

select recent tab
    Given go page  全景图
    Then click item  recent
    Then is selected banner tab  recent

turn page
    Given go page  全景图
    Then turn page
    Then is turned page

turn more photo content page
    Given go page  全景图
    Then click item  图片作品
    Then click more photo content
    Then is more photo content page
