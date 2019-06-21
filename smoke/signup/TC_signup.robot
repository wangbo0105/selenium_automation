*** Settings ***
Documentation       Signup modal test

Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.SignupLibrary
Resource  ../../testdata/userdata.robot

*** Test cases ***
SimpleSignup
    ${Random int} =         Evaluate    random.randint(0, 1000000)    modules=random
    Given go page  login
    When select signup
    When sign up   juxuan+${Random int}@veer.tv      qatest${Random int}     ${password}   ${fullname}
    Then signup success