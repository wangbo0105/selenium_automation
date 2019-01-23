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
    Then go photo detail
    Then is photo detail page

select featured tab
    Given go page  全景图
    Then click featured tab
    Then is featured tab

select popular tab
    Given go page  全景图
    Then click popular tab
    Then is popular tab

select recent tab
    Given go page  全景图
    Then click recent tab
    Then is recent tab

turn page
    Given go page  全景图
    Then turn page
    Then is turned page

turn more photo content page
    Given go page  全景图
    Then go photo detail
    Then click more photo content
    Then is more photo content page
