*** Settings ***
Documentation   login regression test
Suite Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.LoginLibrary
Library  services.SignupLibrary

Resource  ../../testdata/userdata.robot

*** Test Cases ***

Check forget password - wrong email
    Given go page  login
    When select forget password
    Then check forget password modal
    And input email   985825282
    And select next step
    And check prompt wrong format email





    
