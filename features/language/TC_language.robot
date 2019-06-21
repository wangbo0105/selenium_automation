*** Settings ***
Documentation    Switch language test
Suite Setup  Run Keywords  load veer  AND  login  ${usrname}  ${password}
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.LanguageLibrary
Library  services.LoginLibrary
Resource  ../../testdata/userdata.robot

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
