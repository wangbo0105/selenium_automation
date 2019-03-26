*** Settings ***
Documentation   login smoke test
Suite Setup  load veer
Suite Teardown  close my browser
Test Template     loginDDT
Library  services.CommonLibrary
Library  services.LoginLibrary


*** Test Cases ***    Usrname             Password    ExpectedResult
usrnameLogin          xuan736             111113      False
                      xuan736             111111      True
                      wrongusr            111111      False
                      ${EMPTY}            111111      False
                      xuan736             ${EMPTY}    False
                      ${EMPTY}            ${EMPTY}    False
                      xuan736             46578987    False 
mobileLogin           18810309857         111111      False
emailLogin            veerqa@veer.tv      123456      True
                      985825282@qq.com    123987      False
                      123456789@.com      123456      False

*** Keywords ***
loginDDT
    [Arguments]    ${usrname}    ${password}    ${expectedResult}
    all login   ${usrname}  ${password}   ${expectedResult}
