# xkcd-grab v2
## xkcd comics fetched using terminal 🥳

![xkcd](https://github.com/bwaklog/xkcd-grab/assets/91192289/29085083-88b4-45af-ad4c-ef6e9000150f)


Hey 👋
This is a CLI tool utilising API's for retrieving user-requested xkcd comics. Its a relatively small sized project, which is WIP cuz of a lack of data. This project is somewhat of a playground for me to explore different searching and querying techniques. 

Due to data limitation, I wanted to make it a goal to make it super easy to find a specific comic based on query. The roadmap of this current is to make a smart cli tool to find the most relevant comic based on a search query.


# Table of Contents
1. [Installation and Usage](#usage)
    - [Commands Available](#commands-available)  
2. [Cool Stuff](#cool-stuff)
3. [Yet To Come](#yet-to-come)
4. [Requirements - covered in Installation](#requirements)

## Installation and Usage: 
<a name="usage"></a>

- Clone this repository
  ```bash
  git clone https://github.com/bwaklog/xkcd-grab
  ```

- Install requirements
  Some **pre-requisites**
	 1. Python3+
	 2. tesseract OCR engine that is going to be implemented in the future updates
  ```bash
  ./install.sh
  ```

![install.sh command](https://i.imgur.com/8QlLgXx.jpg)

- Add xkcd alias to the path for easier commands
    Add alias to the path manually, I still have to figure out how to automate this. 
  ```bash
  alias xkcd='./xkcd.sh'
  ```
	
	*Sidenote* :  the script creates a virtual env `venv`, so you might want to start using it
	
  ```bash
  . venv/bin/activate
  ```
  

  ### Commands Available
  <a name="commands-available"></a>

*PS* even if u mess up the commands, there is a help file to guide you...which I am yet to complete :P

Here is a boiler plate of how the CLI commands must follow

```
xkcd <type of request> <extra commands>
```

### 1. Type of request

|     | type of request                                                                   | flags                |
| --- | --------------------------------------------------------------------------------- | -------------------- |
| ✅  | **latest** comic                                                                      | -l, --latest         |
| ✅  | **specific** comic number                                                         | integer<br/> ex: 297 |
| ✅  | **Fuzzy search** comic titles                                                   | -f, --fuzzy          |
| ✅  | **Regular** searching something like an SQL syntax                                | -s, --search         |
| ✅  | **Web Scraping** search using google's searching algo to find the best result | -g, --google         | 

###  2. Extra Commands
|     | type of request                                                                                                                                  | flags    |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------ | -------- |
| ✅  | **quick look** comic<br/> - uses system quicklook on MacOS to display comics<br/> - uses system default app on other platforms to display comics | -q, --ql |
| 🔘  | **Saving** Comics Feature (Currently can be done by saving image opened by quicklook)                                                       | TBA      |
| 🔘  | **Sharing** Comics Feature (Currently can be done by saving image opened by quicklook)                                                      | TBA      |

## Cool stuff: 
<a name="cool-stuff"></a>
- For MacOS systems, image is opened using the system quicklook. This has been done by utilising the `qlmanage` command
- Web Scraping uses googles best matches to find the comic you are searching for. All you need to type is a search query(anything that describes the comic)
  <br />
  <iframe src="https://i.imgur.com/xCOmCyX.mp4" allow="fullscreen" allowfullscreen="" style="height: 100%; width: 100%; aspect-ratio: 16 / 9;"></iframe>
## Yet to come 
<a name="yet-to-come"></a>

This project is somewhat of a playground for me to explore different searching algorithms and querying techniques. While this might have a niche target, I want to build this tool into a more robust API client. The roadmap of this current is to make a smart cli tool to find the most relevant comic based on a search query.

The current `web scraping` function that is built into the app is the goal I am trying to achieve using data from all the 2800+ comics alone. So this is still very much a work in progress 

- _Create a web interface using **flask**._..<br />
  May or may not go ahead with this option cuz the main goal was to create a cli tool. But if needed, I take a chance in making one. 
  
  - 💾 Local Storage options for comics
  - ❤️ Creating Bookmark/Liking features
  - 📩 Creating a sharing option. Send your favorite comics to your friends with a few clicks!
  - Umm...A neat interface cuz I don't want get myself using tkinter or some other boring looking tool.
- There was supposed to be an `install.sh` script to add the `xkcd.sh` script to your alias but that didn't seem to work cuz idk how to do that
  <br /><br />

### Tabulated stuff for professionalism 🫡
  
  |ツ|**Feature**|**Progress**|
  |---|---|---|
  |🔥|Smart Comic Search|🕺 In progress|
  |💾|Local Storage Option|👍 workaround available|
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
