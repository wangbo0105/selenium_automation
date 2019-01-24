*** Settings ***
Documentation   Experience test
Test Setup  load veer
Suite Teardown  close my browser
Library  services.CommonLibrary
Library  services.ExpLibrary
Library  services.UploadLibrary
Library  services.LoginLibrary
Resource  ../../testdata/userdata.robot

*** Test Cases ***
导航栏 互动体验首页跳转
    Given go page  互动体验
    Then is exp page

上传页面-了解更多 互动体验首页跳转
    Given go page  上传
    Then click item  上传-了解更多
    Then is exp page

Banner-Tab-了解更多 互动体验播放详情页跳转
    Given go page  互动体验
    Then click item  了解更多
    Then is exp detail page

Banner-Tab-VR故事 切换
    Given go page  互动体验
    Then click item  VR故事
    Then is banner tab  VR故事

Banner-Tab-VRlog日记案例 切换
    Given go page  互动体验
    Then click item  VRlog日记案例
    Then is banner tab  VRlog日记案例

Banner-Tab-餐厅全景图案例 切换
    Given go page  互动体验
    Then click item  VR故事
    Then click item  餐厅全景图案例
    Then is banner tab  餐厅全景图案例

Seth的VeeR主页 跳转
    Given go page  互动体验
    Then click item  Seth的VeeR主页
    Then is Seth home page

立即体验 上传页跳转
    Given go page  互动体验
    Then click item  立即体验
    Then is login alert
    Then login  ${usrname}  ${password}
    Then is upload page