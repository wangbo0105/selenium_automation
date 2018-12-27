*** Keywords ***
Login
    [Arguments]    ${usr}   ${pwd}
    click element    class=header-login     # 点击登录tab
    input text    id=identifier    ${usr}       # 输入用户名
    input password    id=password    ${pwd}     # 输入密码
    click button    class=submit-btn        # 点击登录button