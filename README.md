# Alphabet Game

## Description
The Alphabet Game is designed to help Latvian children expand their knowledge of the Latvian alphabet in a fun way! The game features images and buttons where the child must press a button corresponding to the letter represented by the image.

## Features
- **Interactive Gameplay**: Children are shown images, and they must select the correct letter from two options.
- **Scoring System**: It tracks how many times the child selects the correct button.
- **Dynamic Image and Letter Selection**: When the child selects the correct letter, the image and buttons are updated.

## Installation
To run the game, you need Python and the following libraries:
- `tkinter`
- `PIL` (Pillow)

### Requirements
You can install Pillow using pip:

```bash
pip install pillow
```

### Running the Game
To run the game, execute the following command in your terminal:
```bash
python alphabet_game.py
```
Make sure to have your images (e.g., arbuzs.png, apple.png, etc.) in the same directory as the script or update the image paths in the code accordingly.

### Code Structure
- **Lietcelv**: The main class that creates the game window and handles the user interface.
- **ButtonHandler**: The class that manages the buttons and game logic, including the scoring system.
- **Image Loading Function**: A function that loads and displays images within the game.
  
## Example Code
Here’s a brief example of how to initialize and run the game:
```python
liet_celv = Lietcelv()
liet_celv.run()
```
### Images
The game uses images of various objects, such as fruits and animals, to help children learn the letters associated with the images. Below is a sample list of image files used in the game:
- `arbuzs.png`
- `apple.png`
- `banans.png`
- `citrons.png`
- `cuska.png`
- `dinazaurs.png`
  
### Author
Developed by yours truly - Jana Ozolniece - aka. Janchuks

  
