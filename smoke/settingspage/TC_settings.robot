*** Settings ***
Documentation    Settingspage test
Test Setup  open my browser
Test Teardown  close my browser
Library  CommonLibrary
Library  SettingsLibrary
Library  LoginLibrary

*** Test Cases ***
#go settings
#    login   ${usrname}  ${password}
#    go settings page
#    is settings page

edit data
    login   ${usrname}  ${password}
    go settings page
    edit data   ${_name1}   ${_username1}   ${_des1}
    refresh current page
    is edit    ${_name1}   ${_username1}   ${_des1}

*** Variables ***
${usrname}       veerqa@veer.tv
${password}      123456
${_name1}        name1
${_username1}    username1
${_des1}         description1