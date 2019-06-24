*** Settings ***
Documentation       Signup modal test and user can skip/close purpose madal

Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.SignupLibrary
Resource  ../../testdata/stg_userdata.robot

*** Test cases ***
Simple Signup 
    ${Random int} =         Evaluate    random.randint(0, 1000000)    modules=random
    Given go page  login
    When select signup
    When sign up   juxuan+${Random int}@veer.tv      qatest${Random int}   ${nickname}     ${password}      ${signupSuccess}
    Then signup success