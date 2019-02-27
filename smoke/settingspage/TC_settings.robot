*** Settings ***
Documentation    Settingspage test
Suite Setup  Run Keywords  load veer  AND  login  ${usrname}  ${password}
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.SettingsLibrary
Library  services.LoginLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
go settings page
    When go settings page
    Then should be settings page

edit user information
    Given go settings page
    When edit user information
    And refresh current window
    Then check user information was modified successfully