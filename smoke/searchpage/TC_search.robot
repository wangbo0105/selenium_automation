*** Settings ***
Documentation   search page jump & search result validation

Test Setup        load veer
Test Teardown     close my browser
Library           services.CommonLibrary
Library           services.SearchLibrary

*** Test Cases ***
jump & search result validation
    Given search content  2018
    Then check search result
