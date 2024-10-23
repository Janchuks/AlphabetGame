import tkinter as tk
from PIL import Image, ImageTk
import random

from tkinter import Tk, Label

class Lietcelv:
    def __init__(self):
        self.root = Tk()
        self.root.title("Lietotāja ceļvedis")
        self.root.minsize(200, 200) 
        self.root.geometry("300x300+50+50")

                # Spēles apraksts
        self.text = tk.Label(self.root, text="Spēles apraksts: Spēlētājam tiks parādīta bilde, un viņam būs jāizvēlas pareizais burts no dotajām izvēlēm.",font=("Helvetica", 10, "bold"), justify="left")
        self.text.pack(anchor="w", padx=10)

        # Interfeiss
        self.text = tk.Label(self.root, text="Uz ekrāna tiks parādīta bilde. Zem bildes būs divas pogas ar burtiem. Viena poga būs ar pareizo burtu, kas attiecas uz bildē redzamo objektu",font=("Helvetica", 10, "bold"), justify="left")
        self.text.pack(anchor="w", padx=10)

        # Spēles gaita
        self.text = tk.Label(self.root, text="Spēles gaita: Spēles sākumā parādīsies pirmā bilde un divas pogas ar burtiem. Ja spēlētājs izvēlas pareizo burtu, tas turpina spēli, ja nē, tad mēģina vēlreiz",font=("Helvetica", 10, "bold"), justify="left")
        self.text.pack(anchor="w", padx=10)

        # Bildes un burtu izvēle
        self.text = tk.Label(self.root, text="Bildes un burtu izvēle: Bildes ir sagatavotas iepriekš, un tās tiks mainītas, kad spēlētājs izvēlas pareizo pogu. Katram burtam ir pievienota attiecīgā bilde, un spēles gaitā tas tiks mainīts.", font=("Helvetica", 10, "bold"), justify="left")
        self.text.pack(anchor="w", padx=10)

        # Svari un cipari
        self.text = tk.Label(self.root, text="Puntku sistēma: Spēles laikā tiks reģistrēts cik bieži spēlētājs ir izvēlējies pareizo pogu.", font=("Helvetica", 10, "bold"), justify="left")
        self.text.pack(anchor="w", padx=10)
        
        
    def run(self):
        self.root.mainloop()

liet_celv = Lietcelv()
liet_celv.run()

def close_window():
    root.destroy()


class ButtonHandler:
    def __init__(self, root):
        self.root = root

        self.latvian_letters = ["A", "Ā", "B", "C", "Č", "D", "E", "Ē", "F", "G", "Ģ", "H", "I", "Ī", "J", "K", "Ķ", "L", "Ļ", "M", "N", "Ņ", "O", "P", "R", "S", "Š", "T", "U", "Ū", "V", "Z", "Ž"]

        self.current_index = 0  

        self.cipars = 0

        self.large_font = ("Arial", 12) 

        self.create_correct_button()

        self.create_incorrect_button()

    def create_correct_button(self):

        self.correct_btn = tk.Button(self.root, text=self.latvian_letters[self.current_index], command=self.correct_button_pressed, font=self.large_font)

        self.correct_btn.pack(side=tk.RIGHT, padx=10, pady=10, ipadx=100, ipady=30)

    def create_incorrect_button(self):

        incorrect_options = self.latvian_letters[:]

        incorrect_options.remove(self.latvian_letters[self.current_index])

        self.incorrect_btn = tk.Button(self.root, text=random.choice(incorrect_options), command=self.incorrect_button_pressed, font=self.large_font)

        self.incorrect_btn.pack(side=tk.LEFT, padx=10, pady=10, ipadx=100, ipady=30)

    def switch_buttons(self):

        press = True

        if press==True:

            changes = random.choice([True, False])

            if changes == True:

                self.correct_btn.pack(side=tk.RIGHT)

                self.incorrect_btn.pack(side=tk.LEFT)

            else:

                self.correct_btn.pack(side=tk.LEFT)

                self.incorrect_btn.pack(side=tk.RIGHT)

    def correct_button_pressed(self):

      
        self.correct_btn.destroy()
        self.incorrect_btn.destroy()
        self.current_index = (self.current_index + 1) % len(self.latvian_letters)
        
        self.cipars += 1
        print(self.cipars)
        image_path = images_paths[self.cipars % len(images_paths)]
        # Load the new image
        image = load_image(image_path, image_width, image_height)
        # Update the image displayed in the label
        label_image.config(image=image)
        label_image.image = image 
        

        self.create_incorrect_button()

        self.create_correct_button()

        self.switch_buttons()

    def incorrect_button_pressed(self):

        self.correct_btn.config(state="disabled")

        self.incorrect_btn.config(state="disabled")

        self.incorrect_btn.config(bg="red")

        self.try_again_button = tk.Button(self.root, text="Try Again", command=self.try_again,font=self.large_font)

        self.try_again_button.pack(ipadx=100, ipady=30)

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

images_paths =["arbuzs.png","apple.png","banans.png","citrons.png","cuska.png","dinazaurs.png",
               "engelis.png","ezelis.png","flamingo.png","galds.png","gitara.png","heli.png","iesnas.png", "iis.png","jura.png","kakis.png",
               "kirbis.png","lacis.png","launs.png","masina.png","nauda.png","nau.png","ozols.png","pele.png","riepa.png","suns.png",
               "sokolode.png","tilts.png","uguns.png","udens.png","vavere.png","zabaks.png","zogs.png"]
image_path = images_paths[0]  
image_width = 300
image_height = 200
image = load_image(image_path, image_width, image_height)

# Create a label to display the image
label_image = tk.Label(root, image=image)
label_image.pack()

# Create a label to display text
label_text = tk.Label(root, text="Kurš burtiņš atbilst šai bildei?")
label_text.pack()

button_handler = ButtonHandler(root)

root.geometry("400x400")

root.mainloop()
