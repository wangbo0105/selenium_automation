*** Settings ***
Documentation   recommended test
#Suite Setup  Run Keywords  load veer  AND  login  ${usrname}  ${password}
Suite Setup  load veer
Test Setup  go page  discover
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.HomeLibrary
Library  services.CommonLibrary
Library  services.LoginLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
go discover page
    Given go page  discover
    Then should be expected page  discover
    And url should be matching  discover

go recommend index page
    Given click feeds item  推荐
    Then should be recommended page

go recommended content detail page
    Given go recommended content detail page
    Then should be recommended content detail page

recommended show more
    Given click more recommended
    Then check recommended show more successful