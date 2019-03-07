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

create collection: without safe
    Given go collection tab
    When create collection box  ${False}
    Then check create collection box results  ${False}

create collection: save
    Given go collection tab
    When create collection box  ${True}
    Then check create collection box results  ${True}

create collection：empty title
    Given go collection tab
    When create collection box  ${True}  0
    Then check collection title error type  empty

create collection: title less than 3 characters
    Given go collection tab
    When create collection box  ${True}  2
    Then check collection title error type  less 3

create collection: title equal 3 characters
    Given go collection tab
    When create collection box  ${True}  3
    Then check create collection box results  ${True}

edit collection
    Given go collection tab
    When edit collection
    Then check create collection box results

edit collection in detail page
    Given go collection tab
    When edit collection  detail
    Then go collection tab
    And check create collection box results

switch_privacy_type
    Given go collection tab
    When switch privacy type    personal
    Then check privacy select type  personal
    When switch privacy type    public
    Then check privacy select type  public

upload collection cover img
    Given go collection tab
    When upload cover
    Then check cover replaced

delete collection box: Cancel
    Given go collection tab
    When delete collection box  ${False}
    Then check delete collection results  ${False}

delete collection box: Delete
    Given go collection tab
    When delete collection box  ${True}
    Then check delete collection results  ${True}

delete collection box in detail page
    Given go collection tab
    When delete collection box in detail  ${True}
    And check delete collection results  ${True}

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
    Given remove content in content detail
    Then check content has removed from content detail

clear collection
    And go collection tab
    Then clear collection box all

