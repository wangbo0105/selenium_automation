
*** Settings ***
Documentation   Store page smoke test
Suite Setup  Run Keywords  load veer  AND  login  ${usrname}  ${password}
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.LoginLibrary
Resource  ../../testdata/userdata.robot


*** Test Cases ***
go store page
    Given go page  store
    Then switch window
    Then url should be matching  store
