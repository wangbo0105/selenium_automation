*** Settings ***
Documentation    Switch language
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.LanguageLibrary

*** Test Cases ***
switch english
    Given switch english
    Then is english

switch japanese
    Given switch japanese
    Then is japanese