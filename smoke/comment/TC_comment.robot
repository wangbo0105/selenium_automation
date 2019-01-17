*** Settings ***
Documentation    comment test
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
    Then go photo
    Then go photo detail
    Then post comment  ${comment_text}


*** Variables ***
${comment_text}    comment_001