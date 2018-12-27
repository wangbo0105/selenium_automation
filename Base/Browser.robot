*** Variables ***
${Browser_chrome}      chrome
${url_stg2}          http://stg2.veervr.tv
${url_stg}           http://stg.veervr.tv
${url}               http://veervr.tv
${time_out}          10

*** Keywords ***
open_my_browser
    [Arguments]    ${url}   ${browser}
    open browser    ${url}    ${browser}
    set browser implicit wait  ${time_out}

close_my_browser
    Close Browser
