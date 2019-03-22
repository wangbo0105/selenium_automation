*** Settings ***
Documentation    Settingspage test
Suite Setup  Run Keywords  load veer  AND  login  ${usrname}  ${password}
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.SettingsLibrary
Library  services.LoginLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
go settings page
    Given go settings page
    Then should be settings page

edit user information
    Given edit user information
    And refresh current window
    Then check user information was modified successfully