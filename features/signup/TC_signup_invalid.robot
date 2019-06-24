*** Settings ***
Documentation       Testing the Signup System in homepage given lots of inputs

Test Setup  load veer
Suite Teardown  close my browser

Test Template     signupDDT

Library  services.CommonLibrary
Library  services.SignupLibrary

Resource  ../../testdata/userdata.robot

*** Test Cases ***               Email                     Usrname             Password                       
Invalid Email                    invalid            ${Valid fullname}     ${Valid password}      
Invalid Password                 ${Valid email}     ${Valid fullname}     12345                      
Invalid Email And Password       invalid            ${Valid fullname}     12345                                
Empty Email                      ${EMPTY}           ${Valid fullname}     ${Valid password}                    
Empty Password                   ${Valid email}     ${Valid fullname}     ${EMPTY}                         
Empty Email And Password         ${EMPTY}           ${Valid fullname}     ${EMPTY}                       
Email Already Registered         juxuan@veer.tv     ${Valid fullname}     ${Valid password}                  

*** Keywords ***
signupDDT
    [Arguments]    ${email}    ${username}    ${password}     
    Given go page  login
    And select signup  
    When sign up   ${email}    ${username}    ${password}     qatest     ${signupFailed}



    
