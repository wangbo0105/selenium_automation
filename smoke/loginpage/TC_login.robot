*** Settings ***
Documentation       Login page test

Test Setup        open my browser
Test Teardown     close my browser
Test Template     loginDDT
Library           CommonLibrary
Library           LoginLibrary


*** Test Cases ***    Usrname             Password    ExpectedResult
usrnameLogin          xuan736             111113      False
                      xuan736             111111      True
emailLogin            veerqa@veer.tv      123456      True
                      985825282@qq.com    123987      False
mobileLogin           18810309857         111111      False                    

*** Keywords ***
loginDDT
    [Arguments]    ${usrname}    ${password}    ${expectedResult}
    login   ${usrname}  ${password}   ${expectedResult}
