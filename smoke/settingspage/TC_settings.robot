*** Settings ***
Documentation    Settingspage test
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.SettingsLibrary
Library  services.LoginLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
go settings
    When login   ${usrname}  ${password}
    Given go settings page
    Then is settings page

edit data
    Given go settings page
    Then edit data   ${_name}   ${_username}   ${_des}
    Then refresh current window
    Then is edit    ${_name}   ${_username}   ${_des}

*** Variables ***
${_name}        test_name
${_username}    test_username
${_des}         test_description