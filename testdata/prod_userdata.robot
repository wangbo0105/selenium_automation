*** Variables ***
${usrname}       pro_veer@veer.tv
${username}      pro_veer
${password}      123456
${nickname}      pro_veer
${fullname}      veerqa

###仅用于验证是一个有效的邮箱格式
${Valid email}            veerqa+999@veer.tv
${Valid fullname}         qatest
${Valid nickname}         qatest
${Valid password}         111111
${Random int} =         Evaluate    random.randint(0, 1000000)    modules=random