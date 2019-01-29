*** Settings ***
Documentation    Switch language smoke test
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.LanguageLibrary

*** Test Cases ***
switch english
    Given switch english
    Then check english

switch japanese
    Given switch japanese
    Then check japanese