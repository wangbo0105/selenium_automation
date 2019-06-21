*** Settings ***
Documentation   Photo page test
Suite Setup  Run Keywords  load veer  AND  login  ${usrname}  ${password}
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.PhotoLibrary
Library  services.LoginLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
go photo mainpage
    Given go page  photo
    Then should be expected page  photo
    And url should be matching  photo

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

turn more photo content page
    Given go page  photo
    And photo click item  photo_content
    When click more photo content
    Then should be more photo content page

turn page in photos content list
    Given go page  photo
    When turn current tab page  next_page
    Then check page turned  page_2
    When turn current tab page  last_page
    Then check page turned  page_1
    When turn current tab page  page_3
    Then check page turned  page_3
