*** Settings ***
Documentation    collection smoke test
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.CollectionLibrary
Library  services.LoginLibrary
Library  services.PersonalLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
create collection
    Given login  ${usrname}   ${password}
    And go collection tab
    When create collection  ${collection_title}
    Then check the collection was created successfully  ${collection_title}

add photos collection
    When add photo collection
    Then check collection


*** Variables ***
${collection_title}    collection001

