*** Settings ***
Documentation   个人中心页面测试集
Suite Setup     open_my_browser   ${url_stg2}  ${browser_chrome}
Suite Teardown  close_my_browser
Test Setup      Login   ${usrname}  ${password}
Test Teardown
Library         Selenium2Library
Resource        ../Base/Browser.robot
Resource        ../Page/PersonalCenter.robot
Resource        ../BusinessServices/Login.robot
Resource        ../TestData/UserData.robot

*** Test Cases ***
TC_Login
    hover_my_tab