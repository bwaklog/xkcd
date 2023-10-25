# xkcd comics fetched using terminal 🥳

![xkcd](https://github.com/bwaklog/xkcd-grab/assets/91192289/29085083-88b4-45af-ad4c-ef6e9000150f)


Hey 👋
This is a small project, made with python to fetch a comic of your choice from the thousands of xkcd comic stack using the existing xkcd api.


# Table of Contents
1. [Usage](#usage)
    - [Commands Available](#commands-available)  
2. [Cool Stuff](#cool-stuff)
3. [Yet To Come](#yet-to-come)
4. [Requirements](#requirements)
5. [Demo](#demo)

## Usage: 
<a name="usage"></a>
- Clone the repository with `git clone https://github.com/bwaklog/xkcd-grab`
- What is supposed to work doesn't 🫠...To install the requirements and _hop_ into the venv, run the script
  ```shell
  ./install.sh
  ```
    <img width="540" alt="image" src="https://github.com/bwaklog/xkcd-grab/assets/91192289/972e96eb-9e6a-4002-a78f-753ec14c5037">
- So for some reason, it doesn't automatically use the `venv` as the source, so just go ahead and run the command
  ```shell
  . venv/bin/activate 
  ```
  And another issue, it is supposed to create an alias to the shell command `./xkcd.sh` which for some reason doesn't work so gotta look into that. So for that purpose, to make your cli commands _neater_ use this
  ```shell
  alias xkcd='./xkcd.sh'
  ```
  Now you are mostly ready to go 🔥
- Here is a small cheat sheet for the commands that are available

  ### Commands Available
  <a name="commands-available"></a>
  ```
  usage: xkcd [ -l | --latest | <a valid comic number>] [ -q | --ql ]

  These are some of the xkcd commands that can be used in various situations

  To fetch comics
    latest comic [ -l | --latest ]        This is flag passed to fetch the latest comic
    comic [ <valid comic number: int> ]   Pass a valid integer to get that comic num

  Using quick Look ( 🍎 MacOS only )
    [ -q | --ql ]                         This creates a buffer image to show the comic
                                          instead of clicking the external link

  More commands yet to come 😁
  ```


## Cool stuff: 
<a name="cool-stuff"></a>
- currently has quick look integration 🤯🤯

## Yet to come 
<a name="yet-to-come"></a>
- _Create a web interface using **flask**._..<br />
  May or may not go ahead with this option cuz using the website is a better option🫠, but here is what I want to achieve by creating a local running web interface (or hopefully one hosted on something like heroku which is a pain to work with)
  - 💾 Local Storage options for comics
  - ❤️ Creating Bookmark/Liking features
  - 📩 Creating a sharing option. Send your favorite comics to your friends with a few clicks!
  - Umm...A neat interface cuz I don't want get myself using tkinter or some other boring looking tool.
- There was supposed to be an `install.sh` script to add the `xkcd.sh` script to your alias but that didn't seem to work cuz idk how to do that
  <br /><br />

### Tabulated stuff for professionalism 🫡
  |ツ|**Feature**|**Progress**|
  ---|---|---
  |💾|Local Storage Option|🔘|
  |❤️|Liking\Bookmarking option to save comic no and not on local storage|🔘|
  |📩|Sharing feature (undecided)|WAP|
  |🤔|Flask generated page|TBA|


## Requirements 
<a name="requirements"></a>
What i'm using for this program:
- This isn't really a disclaimer but if you don't have quick-look (MacOS only), that's no problem! But for now all you get is:
  - 🔗 A link to the image of the post. You can open it in your default browser
  - A _very very very_ descriptive info of the post you requested for ツ
- Yeah, I haven't used this on a windows pc so far, and some of these..._**most of these**_ commands are _UNIX_ commands so, **join the the Force with BASH 🕺**
- running this in a venv for development, so do make sure you install all the requirements from `requirements.txt`
- That's it for now...nothing else to force you to install..**other than python3**🐍


## Demo 
<a name="demo"></a>
here is a small demo from an _old recording_
![xkcd_cli](https://github.com/bwaklog/xkcd_view/assets/91192289/e475f168-6286-4636-a4f4-fc8ba1e00351)
