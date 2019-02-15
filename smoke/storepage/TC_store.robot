
*** Settings ***
Documentation   Store page smoke test
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary


*** Test Cases ***
go store page
    Given go page  store
    Then switch window
    Then url should be matching  store
