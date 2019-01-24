*** Settings ***
Documentation   Experience smoke test
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.ExpLibrary

*** Test Cases ***
互动体验首页跳转
    Given go page  互动体验
    Then is exp page

互动体验详情页跳转
    Given go page  互动体验
    Then click item  了解更多
    Then is exp detail page
