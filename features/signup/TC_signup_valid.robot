*** Settings ***
Documentation       Signup modal test and user can skip/close purpose madal

Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.SignupLibrary
Resource  ../../testdata/userdata.robot

*** Test cases ***
Simple Signup Purpose Select one ->Close 
    ${Random int} =         Evaluate    random.randint(0, 1000000)    modules=random
    Given go page  signup
    And sign up   juxuan+${Random int}@veer.tv      ${usrname}   ${password}
    When has purpose modal
    Then check one purpose
    And close purpose modal and sign out

Simple Signup Purpose Check one And Uncheck one -> Skip
    ${Random int} =         Evaluate    random.randint(0, 1000000)    modules=random
    Given go page  signup
    And sign up   juxuan+${Random int}@veer.tv      ${usrname}   ${password}
    When has purpose modal
    Then check one purpose 
    And check cancel one purpose
    And skip purpose and sign out 

Simple Signup Purpose Modal -> Done
    ${Random int} =         Evaluate    random.randint(0, 1000000)    modules=random
    Given go page  signup
    And sign up   juxuan+${Random int}@veer.tv      ${usrname}   ${password}
    When has purpose modal
    Then check one purpose 
    Then select done and sign out 