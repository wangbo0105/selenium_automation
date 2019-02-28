*** Settings ***
Documentation       Testing the Signup System in homepage given lots of inputs

Test Setup  load veer
Suite Teardown  close my browser

Test Template     signupDDT

Library  services.CommonLibrary
Library  services.SignupLibrary

Resource  ../../testdata/userdata.robot


*** Test Cases ***               Email                     Usrname             Password          ExpectedResult
Invalid Email                    invalid            ${Valid fullname}     ${Valid password}      False
Invalid Password                 ${Valid email}     ${Valid fullname}     12345                  False
Invalid Email And Password       invalid            ${Valid fullname}     12345                  False
Empty Email                      ${EMPTY}           ${Valid fullname}     ${Valid password}      False
Empty Password                   ${Valid email}     ${Valid fullname}     ${EMPTY}               False
Empty Email And Password         ${EMPTY}           ${Valid fullname}     ${EMPTY}               False
Email Already Registered         juxuan@veer.tv     ${Valid fullname}     ${Valid password}      False

*** Keywords ***
signupDDT
    [Arguments]    ${email}    ${username}    ${password}     ${ExpectedResult}
    Given go page  signup  
    When sign up   ${email}    ${username}    ${password}     ${ExpectedResult}



    
