
# NBA Stat Tracker

## Introduction

Welcome to the NBA Stat Tracker, a web application designed to view season averages of NBA players.

## Project Objectives

The goal of the project is to transform static numbers into a dynamic, interactive experience. The NBA Stat Tracker, powered by the [balldontlie API](https://www.balldontlie.io/home.html#get-all-teams), provides real-time data, offering insights into player performances and game statistics. The application is structured on MVC architecture, ensuring a clean separation between:

- **Model**: The data layer that handles NBA statistics.
- **View**: The presentation layer that users interact with.
- **Controller**: The business logic layer managing user requests and data processing.

## Methodology

 Flask was choosen for its lightweight and flexible nature, ideal for a streamlined and effective development process. Key features of the application include:

- **Flask Framework**: Utilized for its simplicity and efficiency, perfect for both backend and frontend development.
- **balldontlie API**: This API is the cornerstone of the application, offering up-to-date and comprehensive player stats.
- **User-Centric Design**: Crafted with HTML, CSS, Bootstrap, JavaScript and Python.
- **Efficient Data Handling**: Leveraging Flask's capabilities to provide a seamless and responsive data experience.

## Setup & Use

To use the application, you need to run the following git command on your Terminal if you have a Apple Mac computer. Use the Command prompt if you have a Windows computer. 

```
git clone https://github.com/DanielGonzalezGil/NBA-Stat-Tracker
```

After running the command, you should have a folder called *NBA-Stat-Tracker*  and within that folder, there should be another folder called *my_flask_app* with the following files on your local machine:

- `app.py`
- `stats.py`
- `api_handler.py`
- `player.py`
- `index.html`
- `main.css`

To execute the program, open the *NBA-Stat-Tracker* folder in a Code editor (like Visual Studio Code) and go to the `app.py` file. Once you are in the file, execute the file in your code editor. You should be prompted by the Terminal (if you are using a Mac) or the Command prompt (if you are using a Windows computer) with a local http host address. copy that address into a web browser and you should be able to use the application now. 


