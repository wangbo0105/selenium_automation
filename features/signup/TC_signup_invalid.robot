*** Settings ***
Documentation       Testing the Signup System in homepage given lots of inputs

Test Setup  load veer
Suite Teardown  close my browser

Test Template     signupDDT

Library  services.CommonLibrary
Library  services.SignupLibrary

Resource  ../../testdata/stg_userdata.robot


*** Test Cases ***               Email                     Username             Password          Fullname          ExpectedResult
Invalid Email                    invalid            ${Valid fullname}     ${Valid password}      &{Vaild nickname}      False
Invalid Password                 ${Valid email}     ${Valid fullname}     12345                  &{Vaild nickname}      False
Invalid Email And Password       invalid            ${Valid fullname}     12345                  &{Vaild nickname}      False
Empty Email                      ${EMPTY}           ${Valid fullname}     ${Valid password}      &{Vaild nickname}      False
Empty Password                   ${Valid email}     ${Valid fullname}     ${EMPTY}               &{Vaild nickname}      False
Empty Email And Password         ${EMPTY}           ${Valid fullname}     ${EMPTY}               &{Vaild nickname}      False
Email Already Registered         juxuan@veer.tv     ${Valid fullname}     ${Valid password}      &{Vaild nickname}      False

*** Keywords ***
signupDDT
    [Arguments]    ${email}    ${username}    ${password}     &{fullname}     ${ExpectedResult}
    Given go page  login
    When select signup
    When sign up   ${email}    ${username}    ${password}     &{fullname}     ${ExpectedResult}



    
