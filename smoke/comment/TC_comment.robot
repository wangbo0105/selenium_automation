*** Settings ***
Documentation    comment somke test
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.CommentLibrary
Library  services.LoginLibrary
Library  services.PhotoLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
post comment
    Given login  ${usrname}   ${password}
    Then go page  photo
    Then photo click item  photo_content
    Then post comment  ${comment_text}
    Then check the comment is successful  ${comment_text}


*** Variables ***
${comment_text}    good_content