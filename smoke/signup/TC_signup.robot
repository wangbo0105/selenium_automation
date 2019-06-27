*** Settings ***
Documentation       Signup modal test

Test Setup  load veer
Suite Teardown  close my browser
Library     DateTime
Library     services.CommonLibrary
Library     services.SignupLibrary
Resource    ../../testdata/userdata.robot

*** Test Cases ***
SimpleSignup
    ${Random int} =         Evaluate    random.randint(0, 1000000)    modules=random
    ${date} =       get_current_date
    ${current date} =     Convert Date       ${date}    result_format=%m%d%Y%H%M
    Given go page  login
    When select signup
    When sign up   juxuan+${current date}@veer.tv      qatest${current date}     ${password}   ${fullname}
    Then signup success