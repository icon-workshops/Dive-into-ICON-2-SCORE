# Dive-into-ICON-2-SCORE

## Prerequisite
**If you didn't attend the first workshop 'Dive into ICON - Tools', we strongly recommend you to finish the step-by-step quickstart guide below before you attend the second workshop. Don't worry, it won't take long.**

#### Quickstart part 1. Helloworld on local emulated environment
- [English Guide](https://www.icondev.io/docs/part-1-helloworld-on-local-emulated-environment)
- [Korean Guide](/docs/workshop_2_prerequisite_part_1_kr.md)

#### Quickstart part 2. Helloworld on testnet
- [English Guide](https://www.icondev.io/docs/part-2-hello-world-on-testnet)
- [Korean Guide](/docs/workshop_2_prerequisite_part_2_kr.md)


For this second workshop, following environments are required. If you have any issues, please join the facebook group, [Dive into ICON](https://www.facebook.com/groups/DiveintoICON) and post your questions there ! We are happy to help you. 

- Linux (Ubuntu 18.04 recommended) or OS X
- Python 3.6 and Python IDE (Pycharm recommended)
- Docker installed - https://docs.docker.com
- T-Bears installed
- Git required. Please clone this repo. 
- We expect you have some python experience, and have basic knowledge about ICON development tools.
- Create a directory `icon-workshop-score` & Run T-Bears docker container  
```
$ cd ~ && mkdir icon-workshop && cd icon-workshop-score
$ docker run -it -p 9000:9000 -v ${PWD}:/tbears/icon-workshop --name icon-workshop-score iconloop/tbears:1.1.0.1
``` 

## Today's Goal 

- **After this workshop, you will get hands-on experience of writing SCORE.**
- **You will learn the syntax and usage of iconservice APIs.**
- **We will review the implementation of two sample SCOREs.**

### Workshop Outline

1. Token & Crowdsale
2. IconScoreBase abstract methods
3. DB abstraction
4. Decorator, fallback
5. Type hints, exception handling
6. Global functions
7. InterfaceScore
8. Limitations

### Sample SCORE
1. Coin Flip 
2. Simple Blackjack

 
 
## Useful Links

#### 1. ICON official Github
https://github.com/icon-project


#### 2. ICON Developer portal
https://icondev.io

* ICON T-Bears Guide  
https://icondev.io/docs/development-environment
* ICON icon-rpc-server Guide  
https://icondev.io/docs/json-rpc-specification
* ICON SCORE Guide  
https://www.icondev.io/docs/overview


#### 3. Tracker
Mainnet : https://tracker.icon.foundation

Testnet : https://bicon.tracker.solidwallet.io


#### 4. ICONex (ICON wallet chrome web store for download)
https://chrome.google.com/webstore/detail/iconex/flpiciilemghbmfalicajoolhkkenfel?hl=ko

#### 5. Faucet (Testnet)
http://52.88.70.222

#### 6. Other Communities
Facebook (Dive into ICON) : https://www.facebook.com/groups/DiveintoICON/

Medium (BLOCKCHAIN STUDY GROUP) : https://medium.com/b-ock-chain

Youtube (ICON Developers) : https://www.youtube.com/channel/UC8h4kVV7w94xmfCz6FbwHhg
