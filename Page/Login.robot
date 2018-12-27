*** Keywords ***
click_login_tab
    click element    ${login_tab}

input_usr
    [Arguments]    ${usr}
    input text    ${username_box}    ${usr}

input_pwd
    [Arguments]    ${pwd}
    input password    ${password_box}    ${pwd}

click_login_button
    click button    ${login_button}

is_logion
    page should contain element  class=user-avatar

*** Variables ***
${login_tab}    class=header-login
${username_box}     id=identifier
${password_box}     id=password
${login_button}     class=submit-btn