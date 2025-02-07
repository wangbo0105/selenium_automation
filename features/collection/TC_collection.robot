*** Settings ***
Documentation    content collection test
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
    Then create collection box  ${True}
    Then check create collection box results  ${True}

create collection: empty title
    Given go collection tab
    Then create collection box  ${True}  0
    Then check collection title error type  empty
    And cancel create collection page

create collection: title less than 3 characters
    Given go collection tab
    Then create collection box  ${True}  2
    Then check collection title error type  less 3
    And cancel create collection page

create collection: title equal 3 characters
    Given go collection tab
    Then create collection box  ${True}  3
    Then check create collection box results  ${True}

edit collection in collection tab
    Given go collection tab
    When edit collection
    Then check create collection box results

edit collection in collection detail
    Given go collection tab
    Then edit collection  detail
    Then go collection tab
    And check create collection box results

switch privacy type
    Given go collection tab
    Then switch privacy type    personal
    Then check privacy select type  personal
    When switch privacy type    public
    Then check privacy select type  public
    And cancel create collection page

delete collection box: Cancel
    Given go collection tab
    Then delete collection box  ${False}
    And check delete collection results  ${False}

delete collection box: Delete
    Given go collection tab
    Then delete collection box  ${True}
    And check delete collection results  ${True}

delete collection box in detail page
    Given go collection tab
    Then delete collection box in detail  ${True}
    And check delete collection results  ${True}

