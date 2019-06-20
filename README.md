Automation
=============

## Setup
* Install python3
* Install chromedriver
* Install required python libs: robotframework, selenium

### For Mac OS X

```
brew install python3
brew cask install chromedriver
pip3 install -r requirements.txt
```

## Run
```
./entrypoint.sh <type> <target>
```


## References
- Why page object: https://martinfowler.com/bliki/PageObject.html
- Page object wrapper of selenium: https://github.com/wgnet/webium
- Selenium wrapper for easy use: http://seleniumbase.com



## Usage

### docker based

* pull image from 155086154000.dkr.ecr.us-west-2.amazonaws.com/test/cyclops:latest  
* docker run 155086154000.dkr.ecr.us-west-2.amazonaws.com/test/cyclops \<type\> \<target\>


### ci based

* using image 155086154000.dkr.ecr.us-west-2.amazonaws.com/test/cyclops:latest  
* set run command to \<type\> \<target\>


## Parameter Explaining

#### \<type\>

* regression  
* smoking

#### \<target\>

* staging  
* production
