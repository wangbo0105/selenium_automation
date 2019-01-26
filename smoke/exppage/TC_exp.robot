*** Settings ***
Documentation   experience smoke test
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.ExpLibrary

*** Test Cases ***
Interactive experience home page jump verification
    Given go page  experience
    Then should be experience page

Interactive experience details page jump verification
    Given go page  experience
    When exp click item  learn_more
    Then should be experience details page
