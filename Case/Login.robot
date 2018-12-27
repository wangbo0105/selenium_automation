*** Settings ***
Documentation   登录页面测试集
Suite Setup     open_my_browser   ${url_stg2}  ${browser_chrome}
Suite Teardown  close_my_browser
Library         Selenium2Library
Resource        ../Base/Browser.robot
Resource        ../Page/Login.robot
Resource        ../TestData/UserData.robot

*** Test Cases ***
TC_Login
    click_login_tab
    input_usr    ${usrname}
    input_pwd    ${password}
    click_login_button
    is_logion