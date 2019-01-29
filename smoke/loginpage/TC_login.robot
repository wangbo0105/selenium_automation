*** Settings ***
Documentation   login smoke test
Test Setup  load veer
Suite Teardown  close my browser
Test Template     loginDDT
Library  services.CommonLibrary
Library  services.LoginLibrary


*** Test Cases ***    Usrname             Password    ExpectedResult    Logout
usrnameLogin          xuan736             111113      False             True
                      xuan736             111111      True              True
emailLogin            veerqa@veer.tv      123456      True              True
                      985825282@qq.com    123987      False             True
mobileLogin           18810309857         111111      False             True

*** Keywords ***
loginDDT
    [Arguments]    ${usrname}    ${password}    ${expectedResult}   ${logout}
    login   ${usrname}  ${password}   ${expectedResult}   ${True}
