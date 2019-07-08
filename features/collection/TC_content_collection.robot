*** Settings ***
Documentation    collection test
Suite Setup  Run Keywords  load veer  AND  login  ${usrname}  ${password}
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.CollectionLibrary
Library  services.LoginLibrary
Library  services.PersonalLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
create collection and add content
    When create collection and add content
    Then check content has collected

remove content from collection detail: Cancle
    Given go collection tab
    When remove content from collection detail  ${False}
    Then check remove content results  ${False}

remove content from collection detail: Remove
    Given go collection tab
    When remove content from collection detail
    Then check remove content results

add content to collection
    When add content to collection
    Then check content has collected

remove content from content detail: Remove
    Given add content to collection
    Then check content has removed from content detail

clear collection
    Given go collection tab
    Then clear collection box all
