*** Settings ***
Documentation   Tag test
Suite Setup  Run Keywords  load veer  AND  login  ${usrname}  ${password}
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.SearchLibrary
Library  services.TagLibrary
Library  services.LoginLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
Click Search - input 2018 and select tag - tag page
    Given search content  2018
    And switch tab tag
    When enter tag page
    Then match tag page
Check Tag page - upload 
    Given search content  2018
    And switch tab tag
    When enter tag page
    When select upload
    Then match upload page
Check popular video - more
    Given search content  2018
    And switch tab tag
    When enter tag page
    And select popular video more
    Then select first video play 
Check popular photo - more 
    Given search content  2018
    And switch tab tag
    When enter tag page
    And select popular photo more
    Then select first photo play 
Check recent experience - more 
    Given search content  2018
    And switch tab tag
    When enter tag page
    And select recent experience more
    Then select first experience play
Check recent contents - more
    Given search content  2018
    And switch tab tag
    When enter tag page
    And select recent content more
    Then select first content play 
Check tag has activity description
    Given search content  2018
    And switch tab tag
    When enter tag page
    Then check this tag has activity description







