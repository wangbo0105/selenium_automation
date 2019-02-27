*** Settings ***
Documentation    comment somke test
Suite Setup  Run Keywords  load veer  AND   login  ${usrname}  ${password}
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.CommentLibrary
Library  services.LoginLibrary
Library  services.PhotoLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
post comment
    Given go page  photo
    Then photo click item  photo_content
    Then post comment
    Then check the comment is successful