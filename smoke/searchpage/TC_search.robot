*** Settings ***
Documentation   search page jump & search result validation
Suite Setup  Run Keywords  load veer  AND  login  ${usrname}  ${password}
Test Setup        load veer
Test Teardown     close my browser
Library           services.CommonLibrary
Library           services.SearchLibrary
Library  services.LoginLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
jump & search result validation
    Given search content  2018
    Then check search result
    And url should be matching  search