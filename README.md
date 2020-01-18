# Python-Space-Invaders

This program is a recreation of the popular computer game Space Invaders with Python using the library Pygame.

The basic aim of the game is to shoot down as many aliens as possible before one of them touches your spaceship or reaches the ground. As soon as a wave is defeated the next one will spawn, moving faster. The spaceship is controlled with the arrow keys and spacebar. The player can also only have 3 active bullets flying over the screen at any time in order to prevent spamming the spacebar.

The program is divided into different python files. Each contains a specific set of functions such as everything related to the ship, the aliens or the game statistics. These functions are then imported into the main file alien_invasion. alien_invasion is also the one which has to be executed in order to play the game. The game was seperated in this way in order to make the code easier to understand and easier to change. 
Important: All files have to be in the same folder, otherwise the import function will encounter problems. The picture files (alien, ship, star) however have to be moved into a seperate folder called "images" in the game folder itself.

The player has three lives shown in the top left corner. In the top right corner the current score and current wave are shown. In the top center the local highscore. This highscore is saved in a text file in the game folder and updated in case the player is able to beat his/her previous highscore.

For question/critique/tips&tricks feel free to write me a message. Thanks a lot for reading.
