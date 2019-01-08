*** Settings ***
Documentation    Switch language
Test Setup  open my browser
Test Teardown  close my browser
Library  CommonLibrary
Library  LanguageLibrary

*** Test Cases ***
switch english
    switch english
    is english

switch japanese
    switch japanese
    is japanese