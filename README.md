# UNIT-1_PROJECT


## Based on what you’ve learned until now , create a project of your choosing (impress us with your imagination) . This project must at least satisfy the following minimum requirements :

- Must be interactive on CLI.
- Use data structures. 
- Use loops & conditionals.
- Use functions that return an output . 
- Use a Lambda function.
- Use at least 1 Class.
- Use some form of Error Handling .
- Organize Your Code into modules & (or packages)

## Example Project :  An online Grocery Store :

#### Overview : An online store that sells fruits to customers. This online store has 2 main users. The customer and the manager of the store . Each one of them should be able to do the following tasks for the store to function properly . 

#### As a customer I should be able to do the following :
- Browse  Products . 
- View the product info (summary, specs, price, quantity , etc.)
- Search for Products.
- Get recommendations for my next purchase based on my purchase history.
- Add Products to the shopping cart .
- Remove a product from the shopping cart.
- List the products in my shopping cart. 
- Continue to checkout . 
- Fill in my address for delivery.
- Get receipt of my purchases.
- Check delivery status . 



#### Usage :
 Explain to the user how to use your project . 
 for example:
 - type in search product_name to search for a product.
 - type in list_products to show all the products in the grocery.
 - type in show product_name to get information about this product.
 - type in buy product_name to buy the product . 
 - and so on...


### For your project. Edit this README.md file to include your own project name,  overview, user stories, and usage. 

### Project name:
Guessing Word Game.

### Overview: 
The Guessing Word Game challenges players to guess a word.This game has only one main user(player). The player should be able to do the following stucture for the game to function properly. 

### As a player: 
- player must be able to start the play by enter his name.
- Player should be able to start a game.
- Player should be able to view all game categories(Hobbies, Jobs, Food).
- player should be able to choose category.
- Player must be able to insert letter or word to guess.
- Player should be able to choose play again.
- Player should be able to view LEADERBORD.
- Player must be able to gain scores by guessing correctly.
- Player must be able to  scores by guessing incorrectly.
- Player should be able to exit the game.

### game rules
- Each player starts by registering a nickname and selects a category to play.
- Players have three rounds to guess words within the chosen category.
- In each round, players have 5 attempts to guess either a letter or the entire word.
- Points are awarded based on correct guesses:
    - Guessing a letter correctly earns 2 points.
    - Guessing the entire word earns 2 points for each letter in the word.
- Points are deducted for incorrect guesses:
    - Incorrectly guessing a letter results in a deduction of 1 point.
    - Incorrectly guessing the entire word results in a deduction of 1 points for each letter in the word.

### usage
- Register a nickname and select a category to play
- Each round starts with a simple description of the word and placeholders for each letter
- Guess letters or the entire word, with a maximum of 5 attempts per round
- Receive feedback on each guess:
    - Correct guesses are acknowledged
    - Incorrect guesses are noted, and points may be deducted
    - Duplicate guesses are flagged to prevent redundancy
- Complete all three rounds to accumulate points
- Track your points throughout the game