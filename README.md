# Three of a Kind Game

Three of a Kind Game it was developed with the intention to entertain the user/player, and force him/her to use his/her memory to make better decisions. It is a card game where the player faces the computer. Each player (user/computer) receives 4 cards, in each round has to discard an unwanted card and draw a new one from two options, current deck game (hidden) or discard deck (revealed), being able to take only the top card. The player who gets 3 of the same cards wins.

The game is deployed on Heroku and is strictly terminal-based for user interaction.

- Here is the link to the final project > [Three of a Kind Game](https://three-of-a-kind-game.herokuapp.com/)

<div align="center">
RESPONSIVE IMAGE HERE
</div>

## Contents

<details>
    <summary>Summary</summary>

- [UX/UI Design](#uxui-design).
     * [Strategy](#strategy).
     * [Scope](#scope).
     * [Structure](#structure).
     * [Skeleton](#skeleton).
       * [Flowchart](#flowchart).
     * [Surface](#surface).
       * [Colour scheme](#colour-scheme).
       * [Typography](#typography).
       * [Imagery](#imagery).
   
- [Features](#features).
   * [Existing Features](#existing-features).
     * [Home page](#home-page).
     * [Converter page](#converter-page).
     * [Quiz game page](#quiz-game-page).
   * [Features Left to Implement](#features-left-to-implement).
 
- [Testing](#testing).
   * [Funcionality](#funcionality).
   * [Navegation and Devices](#navegation-and-devices).
   * [Validator Testing](#validator-testing).
   * [Performance Testing](#performance-testing).
   * [Other Tests](#other-tests).
   * [User Story Testing](#user-story-testing).
   * [Fixed Bugs](#fixed-bugs).
   * [Unfixed Bugs](#unfixed-bugs).
 
- [Deployment](#deployment).
   * [Deployment](#deployment).
   * [Fork](#fork).
   * [Clone](#clone).
  
- [Technologies and tools](#technologies-and-tools).

- [Credits](#credits). 
   * [Content](#content).
   * [Media](#media).
   * [Inspiration](#inspiration).
 
- [Acknowledgements](#acknowledgements).
 
</details> 


## UX/UI Design

### Strategy

#### Site owner goals

- The game targets those who are excited by card games and challenges. The game was designed to be a good hobbie and an alternative way to train your mind. People who are interested in different games and games that involve cards could be a potential audience.

#### User stories

- As a user, I want to understand the purpose of the website, so I can know if it's of interest to me.
- As a user, I want to easily navigate the site/game, so I don't get lost trying to navigate/play.
- As a user, I want to be able to check my points and those of my opponent, to know my performance.
- As a user, I want to be able to restart/quit the game, if it is in my interest to start again for some reason.

### Scope

For Three of a Kind Game I have planned the following features.
	- Use of the python language efficiently to make the game dont show any problems.
	- Through the terminal-based, display as clearly as possible the cards and dynamics of the game

### Structure

The Three of a Kind Game structure is based on a single static web page with the terminal-based to run the game.

### Skeleton

#### Flowchart

- The flowchart was elaborated to guide the development of the game steps.

<details><summary>Flowchart</summary>
<div align="center">
FLOWCHART IMAGE HERE
</div>
</details>

### Surface

#### Colour scheme

- To make the game more intuitive and to highlight certain aspects such as suits, selection options or to highlight one information differently from another. I chose to use ANSI colors in the terminal.

## Features

### Existing Features

__Main menu__

<div align="center">
<img src="assets/images/main-menu.PNG">
</div>

__Rules__


<div align="center">
<img src="assets/images/main-rules.PNG">
</div>

__Quit__

<div align="center">
<img src="assets/images/quit-game.PNG">
</div>

__Flip Coin__

<div align="center">
<img src="assets/images/coin-selection.PNG">
</div>

<div align="center">
<img src="assets/images/coin-win-heads.PNG">
</div>

<div align="center">
<img src="assets/images/coin-lose-tails.PNG">
</div>

__Game__

- Player

<div align="center">
<img src="assets/images/player-discard.PNG">
</div>

<div align="center">
<img src="assets/images/player-take.PNG">
</div>

<div align="center">
<img src="assets/images/exit-option.PNG">
</div>

- Computer

<div align="center">
<img src="assets/images/computer-action.PNG">
</div>

- Win / Loss

<div align="center">
<img src="assets/images/game-win.PNG">
</div>

<div align="center">
<img src="assets/images/game-lose.PNG">
</div>

### Features Left to Implement

- To be implemented in the future, I am thinking about the possibility of adding a ranking that receives the player's name and the player's victory and defeat points. This ranking would be accessed from the menu to encourage players to try to beat the records.

## Testing

During these tests the size of the displays were adjusted, when to clean the terminal to keep the game fixed. In the end I found what I believe to be the most pleasing and intuitive look for the scope of a terminal-based game.

### Funcionality

Once the game was finished, I played it several times to find possible flaws or errors that could compromise the gameplay or interrupt the game. 
All commands are responding as they should, when some wrong selection is sent to the terminal, the answers are appearing to the user.
So far, when I finished and made the final deployment, the game is responding with no apparent errors.

### Navegation and Devices

With the project finished, I performed several tests on different browsers and different computers to check the playability and possible faults. No errors were presented during these tests

- __Desktop__
  - Sony Vaio (Laptop)
  - Dell XPS (Laptop)
  - Asus Chromebook (Laptop)
  - Macbook Air (Laptop)
  - HP (CPU)

- __Browsers__
  - Chrome
  - Firefox
  - Safari
  - Edge

### Validator Testing

- __Pyhton__
- I tested the code through PEP8 and no significant errors were presented.

### Other Tests

### User Story Testing

### Fixed Bugs

### Unfixed Bugs
    
## Deployment

### Deployment

- After finishing developing the program I deployed it on Heroku following this steps:

1. Create an account if you don't have and login into Heroku website
2. After loged in, you should click on *"New -> Create new app"* button
3. Insert your app's __Name__ (need be unique), then you need to __Choose__ your region, at the end click at the "Create App" button
4. Navigate into the Settings tab, and go to "Config vars" section, then go to *"Reveal Config Vars"*
5. Enter the __PORT__ in the KEY section and __8000__ for its value, then click *"Add"*
6. Next you need to go to *"Buildpacks"* section and click "Add buildpack"
7. Firstly add the *Python* buildpack then *NodeJs*, need to be on that order
8. Navigate to the *"Deploy"* tab, and select Github as the deployment method
9. You need to look for your repository name and select the option Connect
10. You can choose between two deployment options for your app to Heroku (Automatic or Manual).
	- With automatic deploys enabled, your app will be updated each time a change has been pushed to the repository
	- With manual deploys, your app will be updated only when you manually click to deploy it
11. After this steps the deploying is finished, a link will be provided to you for accessing your app

### Fork

- Forks let you make changes to a project without affecting the original repository. Follow this steps:
1. Go to the repository page, can be accessed [here](https://github.com/guisgrande/third-project-ci).
2. On top right, you select the Fork option and proceed.
3. A duplicate will be created inside your repository.

### Clone

- Clone let you create an identical repository to the original. Follow this steps:
1. Go to the repository page, can be accessed [here](https://github.com/guisgrande/third-project-ci).
2. Click on code drop down menu.
3. Choose if you want to clone using HTTPS, SSH or GitHub CLI. Then select de copy button.
4. Open your Git Bash in your IDE.
5. Type git clone and then paste the URL you copied before.
6. Press Enter to create your clone.

## Technologies and tools

- Programming languages used: Python 3.6
- [Gitpod](https://www.gitpod.io/) - Used to create/edit the code of the project.
- [Github](https://github.com/) - Used to create repository, hosting files and deployment of the website.
- [Heroku](https://heroku.com/) -  Used to deploy the project
- [Ludichart](https://www.lucidchart.com/) - Used to create the flowchart.
- [PEP8](http://pep8online.com/) - Used to test/validate Python code.

## Credits

### Inspiration
 

## Acknowledgements

- Code Institute for all the support and the team always ready to help.
- My mentor [Ben Kavanagh](https://github.com/BAK2K3) for all the instructions, advice and knowledge that helped me to improve the project.
- My parents, my wife and my friends for motivating me to achieve my best.
- Everyone in the Slack community for tips and opinions. 
