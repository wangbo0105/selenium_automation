*** Settings ***
Documentation   search page jump & search result validation

Test Setup        open my browser
Test Teardown     close my browser
#Test Template     searchDDT
Library           CommonLibrary
Library           SearchLibrary

#*** Test Cases ***        SearchWord      ExpectedResult
#commonSearch              2018            true
*** Test Cases ***
jump & search result validation
    search  2018
   
                    
#*** Keywords ***
#searchDDT
#    [Arguments]    ${searchword}     ${expectedResult}
#    search         ${searchword}       ${expectedResult}