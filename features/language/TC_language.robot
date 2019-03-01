*** Settings ***
Documentation    Switch language smoke test
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.LanguageLibrary

*** Test Cases ***
switch english
    Given switch language  English
    Then check current language  English

switch japanese
    Given switch language  Japanese
    Then check current language  Japanese

switch chinese
    Given switch language  Chinese
    Then check current language  Chinese
