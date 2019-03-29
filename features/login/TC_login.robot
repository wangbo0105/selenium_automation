*** Settings ***
Documentation   login regression test
Suite Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.LoginLibrary
Library  services.SignupLibrary

Resource  ../../testdata/userdata.robot

*** Test Cases ***
Signup modal -login 
    Given go page  signup
    When select login
    Then all login  ${usrname}  ${password}   True
    
Check WeChat modal
    Given go page  login
    When select WeChat
    Then check WeChat modal

Check forget password - wrong email
    Given go page  login
    When select forget password
    Then check forget password modal
    And input email  985825282
    And select next step
    And check prompt wrong format email
    
Check forget password - resent email
    Given go page  login
    When select forget password
    And input email    985825282@qq.com
    And select next step
    Then select resent email

Check forget password - close modal
    Given go page  login
    When select forget password
    Then close forget password modal

Check forget password - right email
    Given go page  login
    When select forget password
    And input email   985825282@qq.com
    Then select next step
    And check sent email modal
    And close sent email modal