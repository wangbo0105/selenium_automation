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
    Then go page  合辑
    Then create collection  ${collection_title}

photo_collection
    When add photo collection
    Then check collection

#clear collection box
#    Given go page  合辑
#    Then clear collection box all


*** Variables ***
${collection_title}    collection001

