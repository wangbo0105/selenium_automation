*** Settings ***
Documentation    collection smoke test
Suite Setup  Run Keywords  load veer  AND  login  ${usrname}  ${password}
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.CollectionLibrary
Library  services.LoginLibrary
Library  services.PersonalLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
create collection
    Given go collection tab
    When create collection box  ${True}
    Then check create collection box results  ${True}

add content to collection
    When add content to collection
    Then check content has collected

clear collection
    And go collection tab
    Then clear collection box all


