*** Settings ***
Documentation   search page jump & search result validation
Suite Setup  Run Keywords  load veer  AND  login  ${usrname}  ${password}
Test Setup  load veer
Suite Teardown  close my browser

Library           services.CommonLibrary
Library           services.SearchLibrary
Library  services.LoginLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
Check search content no result page 
    Given search content  askldhlakjdaljkd
    When switch tab   content
    Then check no result page

Check search collection no result page
    Given search content  askldhlakjdaljkd
    When switch tab   collection
    And check no result page

Check search tag no result page
    Given search content  askldhlakjdaljkd
    When switch tab   tag
    Then check no result page

Check search tab content jump
    Given search content  2018
    When switch tab   content
    Then select one content and play

Check search collection jump
    Given search content  2018
    When switch tab   collection
    Then select one collection

Check search user jump
    Given search content  2018
    When switch tab   user
    Then select one user