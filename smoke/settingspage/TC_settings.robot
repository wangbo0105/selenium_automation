*** Settings ***
Documentation    Settingspage test
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.SettingsLibrary
Library  services.LoginLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
go settings page
    Given login   ${usrname}  ${password}
    When go settings page
    Then should be settings page

edit user information
    Given go settings page
    When edit user information   ${_name}   ${_username}   ${_des}
    And refresh current window
    Then check user information was modified successfully    ${_name}   ${_username}   ${_des}

*** Variables ***
${_name}        test_name
${_username}    test_username
${_des}         test_description