*** Settings ***
Documentation   login smoke test
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.LoginLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
login
    Given login   ${usrname}  ${password}
    Then check you are logged in

logout
    Given log out
    Then check you are logged out


