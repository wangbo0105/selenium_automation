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
    When create collection
    Then check the collection was created successfully

add photos collection
    When add photo collection
    Then check collection

clear collection
    And go collection tab
    Then clear collection box all



*** Variables ***
${collection_title}    collection001

