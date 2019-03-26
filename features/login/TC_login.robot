*** Settings ***
<<<<<<< HEAD
Documentation   login smoke test
Suite Setup  load veer
Suite Teardown  close my browser
Test Template     loginDDT
Library  services.CommonLibrary
Library  services.LoginLibrary


*** Test Cases ***    Usrname             Password    ExpectedResult
usrnameLogin          xuan736             111113      False
                      xuan736             111111      True
                      xuan1               111111      False
                      {EMPTY}             111111      False
                      xuan736             {EMPTY}
mobileLogin           18810309857         111111      False
emailLogin            veerqa@veer.tv      123456      True
                      985825282@qq.com    123987      False


*** Keywords ***
loginDDT
    [Arguments]    ${usrname}    ${password}    ${expectedResult}
    all login   ${usrname}  ${password}   ${expectedResult}
=======
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





    
>>>>>>> test
