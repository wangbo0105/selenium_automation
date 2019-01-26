*** Settings ***
Documentation   Photo page test
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.PhotoLibrary

*** Test Cases ***
go photo mainpage
    Given go page  photo
    Then should be photo page

go photo content detail page
    Given go page  photo
    When photo click item  photo_content
    Then should be photo detail page

select featured tab
    Given go page  photo
    When photo click item  featured
    Then the banner tab should be selected  featured

select popular tab
    Given go page  photo
    When photo click item  popular
    Then the banner tab should be selected  popular

select recent tab
    Given go page  photo
    When photo click item  recent
    Then the banner tab should be selected  recent

turn page
    Given go page  photo
    When turn page
    Then the pages should turned

turn more photo content page
    Given go page  photo
    And photo click item  photo_content
    When click more photo content
    Then should be more photo content page
