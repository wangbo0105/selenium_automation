*** Settings ***
Documentation    bookmark test
Suite Setup  Run Keywords  load veer  AND  login  ${usrname}  ${password}
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.BookMarkLibrary
Library  services.LoginLibrary
Library  services.PersonalLibrary
Library  services.PhotoLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
go bookmark tab
    Given go bookmark tab
    Then check tabs is selected  VR书签

add bookmark in detail page
    Given bookmark in detail page
    Then check the bookmark has been added

remove bookmark in detail page
    Given remove bookmark in detail
    Then check remove bookmark in detail
    And check remove bookmark in personal

add bookmark in cover page
    Given bookmark in cover page
    Then check the bookmark has been added

bookmark helper alter
    Given go page  photo
    And photo click item  photo_content
    When click bookmark helper button
    Then check bookmark helper alert

switch screen type in bookmark tab
    Given go bookmark tab
    When screen bookmark type  视频
    Then check current screen type  视频
    When screen bookmark type    照片
    Then check current screen type  照片
    When screen bookmark type  互动体验
    Then check current screen type  互动体验
    When screen bookmark type  所有书签
    Then check current screen type  所有书签

remove bookmarks
    Given go bookmark tab
    Then clear bookmark data
