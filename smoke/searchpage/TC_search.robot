*** Settings ***
Documentation   search page jump & search result validation

Test Setup        open my browser
Test Teardown     close my browser
Library           CommonLibrary
Library           SearchLibrary

*** Test Cases ***
jump & search result validation
    search  2018