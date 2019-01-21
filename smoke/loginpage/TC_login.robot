*** Settings ***
Documentation   Login page test
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.LoginLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
login
    Given login   ${usrname}  ${password}
    Then is login

log out
    Given go page  退出登录
    Then is logout


