*** Settings ***
Documentation    collection test
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.CollectionLibrary
Library  services.LoginLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
create_collection_box
    Given login  ${usrname}   ${password}
    Then go collection tab
    Then create collection  ${title}

photo_collection
    When add photo collection
    Then check collection in detail page
    Then go collection tab
    Then go collection box
    Then check collection in collection box


*** Variables ***
${title}    collection001

