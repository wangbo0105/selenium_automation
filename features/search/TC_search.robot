*** Settings ***
Documentation   Check top content list & Check tag filter
Suite Setup  Run Keywords  load veer  AND  login  ${usrname}  ${password}
Test Setup        load veer
Test Teardown     close my browser

Library           services.CommonLibrary
Library           services.SearchLibrary
Library  services.LoginLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
Check top content list
  Given search content  ab123456cdefg--
  When check top content list
  Then select one content play

Check search video filter
  Given search content  2018
  When filter video
  Then check this is a video and play

Check search photo filter
  Given search content  2018
  When filter photo
  Then select one content and play

Check search experience filter
  Given search content  2018
  When filter experience
  Then select one content and play

Check search all content filter
  Given search content  2018
  When filter all content
  Then select one content and play
  






