import tkinter as tk
from PIL import Image, ImageTk
import random

from tkinter import Tk, Label

class Lietcelv:
    def __init__(self):
        self.root = Tk()
        self.root.title("Lietotāja ceļvedis")
        self.root.minsize(500, 500) 
        self.root.geometry("300x300+50+50")

        # Prevent the window from resizing to fit its content
        self.root.pack_propagate(True)

        # Create Label in our window
        # Spēles apraksts
        self.text = tk.Label(self.root, text="Spēles apraksts: Spēlētājam tiks parādīta bilde, un viņam būs jāizvēlas pareizais burts no dotajām izvēlēm.", font=("Helvetica", 10, "bold"), justify="left", wraplength=280)
        self.text.pack(anchor="w", padx=10, fill="both", expand=False)

        # Interfeiss
        self.text = tk.Label(self.root, text="Uz ekrāna tiks parādīta bilde. Zem bildes būs divas pogas ar burtiem. Viena poga būs ar pareizo burtu, kas attiecas uz bildē redzamo objektu", font=("Helvetica", 10, "bold"), justify="left", wraplength=280)
        self.text.pack(anchor="w", padx=10, fill="both", expand=True)

        # Spēles gaita
        self.text = tk.Label(self.root, text="Spēles gaita: Spēles sākumā parādīsies pirmā bilde un divas pogas ar burtiem. Ja spēlētājs izvēlas pareizo burtu, tas turpina spēli, ja nē, tad mēģina vēlreiz", font=("Helvetica", 10, "bold"), justify="left", wraplength=280)
        self.text.pack(anchor="w", padx=10, fill="both", expand=True)

        # Bildes un burtu izvēle
        self.text = tk.Label(self.root, text="Bildes un burtu izvēle: Bildes ir sagatavotas iepriekš, un tās tiks mainītas, kad spēlētājs izvēlas pareizo pogu. Katram burtam ir pievienota attiecīgā bilde, un spēles gaitā tas tiks mainīts.", font=("Helvetica", 10, "bold"), justify="left", wraplength=280)
        self.text.pack(anchor="w", padx=10, fill="both", expand=True)

        # Svari un cipari
        self.text = tk.Label(self.root, text="Puntku sistēma: Spēles laikā tiks reģistrēts cik bieži spēlētājs ir izvēlējies pareizo pogu.", font=("Helvetica", 10, "bold"), justify="left", wraplength=280)
        self.text.pack(anchor="w", padx=10, fill="both", expand=True)

        # Create a button to close the window
        self.close_button = tk.Button(self.root, text="Sapratu!", command=self.close_window)
        self.close_button.pack(anchor="e", padx=10, pady=10)  # Anchor to the east (right) side of the window with some padding
    
    def close_window(self):
        self.root.destroy()
        
    def run(self):
        self.root.mainloop()

# Instantiate and run the application
liet_celv = Lietcelv()
liet_celv.run()


class ButtonHandler:
    def __init__(self, root):
        self.root = root
        self.latvian_letters = ["A", "Ā", "B", "C", "Č", "D", "E", "Ē", "F", "G", "Ģ", "H", "I", "Ī", "J", "K", "Ķ", "L", "Ļ", "M", "N", "Ņ", "O", "P", "R", "S", "Š", "T", "U", "Ū", "V", "Z", "Ž"]
        self.current_index = 0  # Index of the current correct letter
        self.cipars = 0
        self.create_correct_button()
        self.create_incorrect_button()
    
    def create_correct_button(self):
        self.correct_btn = tk.Button(self.root, text=self.latvian_letters[self.current_index], command=self.correct_button_pressed)
        self.correct_btn.pack()

    def create_incorrect_button(self):
        incorrect_options = self.latvian_letters[:]
        incorrect_options.remove(self.latvian_letters[self.current_index])
        self.incorrect_btn = tk.Button(self.root, text=random.choice(incorrect_options), command=self.incorrect_button_pressed)
        self.incorrect_btn.pack()

    def correct_button_pressed(self):
        self.correct_btn.destroy()
        self.incorrect_btn.destroy()
        self.current_index = (self.current_index + 1) % len(self.latvian_letters)
        
        self.cipars += 1
        print(self.cipars)
        
        # Select the next image path from the list
        image_path = images_paths[self.cipars % len(images_paths)]
        # Load the new image
        image = load_image(image_path, image_width, image_height)
        # Update the image displayed in the label
        label_image.config(image=image)
        label_image.image = image  # Keep a reference to the image to prevent garbage collection
        
        # Create new buttons for both correct and incorrect options
        press = True
        if press==True:
            changes = random.choice([True, False])
            print(changes)
            if changes==True:
                self.create_incorrect_button()
                self.create_correct_button()
            else:
                self.create_correct_button()
                self.create_incorrect_button()
        
        return self.cipars

    def incorrect_button_pressed(self):
        self.correct_btn.config(state="disabled")
        self.incorrect_btn.config(state="disabled")
        self.incorrect_btn.config(bg="red")
        self.try_again_button = tk.Button(self.root, text="Try Again", command=self.try_again)
        self.try_again_button.pack()

    def try_again(self):
        self.try_again_button.destroy()
        self.correct_btn.config(state="active")
        self.incorrect_btn.config(state="active")
        self.incorrect_btn.config(bg="SystemButtonFace")
        
    def get_cipars(self):
        return self.cipars


root = tk.Tk()
root.title("Alfabēta spēle")
# Define a function to load an image
def load_image(path, width, height):
    img = Image.open(path)
    img = img.resize((width, height))
    return ImageTk.PhotoImage(img)

# Load your image
images_paths =["arbuzs.png","apple.png","banans.png","citrons.png","cuska.png","dinazaurs.png",
               "engelis.png","ezelis.png","flamingo.png","galds.png","gitara.png","heli.png","iesnas.png", "iis.png","jura.png","kakis.png",
               "kirbis.png","lacis.png","launs.png","masina.png","nauda.png","nau.png","ozols.png","pele.png","riepa.png","suns.png",
               "sokolode.png","tilts.png","uguns.png","udens.png","vavere.png","zabaks.png","zogs.png"]
image_path = images_paths[0]  # Select the first image initially
image_width = 500
image_height = 500
image = load_image(image_path, image_width, image_height)

# Create a label to display the image
label_image = tk.Label(root, image=image)
label_image.pack()

# Create a label to display text
label_text = tk.Label(root, text="Hello, Tkinter!")
label_text.pack()

button_handler = ButtonHandler(root)

root.geometry("700x700")
# Start the Tkinter event loop
root.mainloop()
