*** Settings ***
Documentation    comment test
Suite Setup  Run Keywords  load veer  AND   login  ${usrname}  ${password}
Test Setup  refresh_current_window
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.CommentLibrary
Library  services.LoginLibrary
Library  services.PhotoLibrary
Library  services.PersonalLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
post comment
    Given view own content
    Then post comment
    Then check the comment is successful

reply comment
    Given reply comment
    Then check reply comment

give comment like
    Given give comment like
    Then check comment like type  ${True}

give comment unlike
    Given give comment like
    Then check comment like type  ${False}
