from tkinter import Tk, Label, Button, Canvas, Entry
from PIL import Image, ImageTk
import requests
from io import BytesIO
from logic import RNG, stoneTracker, stonesSpent

# Initialize global variables
stoneCount = 0
stoneUse = 0

def summon():
    global stoneCount, stoneUse
    
    # Get values from the input fields
    try:
        summon_value = int(summon_value_entry.get())
        rate_value = float(rate_entry.get())
        banner_value = banner_entry.get()

        multi = summon_value >= 10

        result = RNG(summon_value, multi, rate_value, False, banner_value)
        
        # Update stone count based on the input field
        stoneCount = int(stone_count_entry.get())
        stoneUse = stonesSpent(stoneUse=50)  # Example, subtract 50 stones
        stoneCount = stoneTracker(stoneCount, stoneUse)  # Update stoneCount after each summon
        
        result_label.config(text=f"Result: {result}\nStones Left: {stoneCount}")  # Update the label with the summon result
    
    except ValueError:
        result_label.config(text="Please enter valid numbers for stones and summon value.")
    except Exception as e:
        result_label.config(text=f"An error occurred: {e}")

# Create the main window
root = Tk()
root.title("Summon Simulator")  # Set the window title

# Load the image from the URL
response = requests.get('https://jpn.dokkan.wiki/assets/japan/character/card/1029090/card_1029090_effect.png')
img_data = response.content
bg_image = Image.open(BytesIO(img_data))
tk_image = ImageTk.PhotoImage(bg_image)

# Create a canvas and set the image as the background
canvas = Canvas(root, width=bg_image.width, height=bg_image.height)
canvas.create_image(0, 0, anchor="nw", image=tk_image)
canvas.pack(fill='both', expand=True)  # Fill the window and allow expansion

# Add input fields
stone_count_label = Label(root, text="Initial Stones:", bg='white')
canvas.create_window(100, 350, window=stone_count_label)
stone_count_entry = Entry(root)
canvas.create_window(250, 350, window=stone_count_entry)

summon_value_label = Label(root, text="Summon Value:", bg='white')
canvas.create_window(100, 400, window=summon_value_label)
summon_value_entry = Entry(root)
canvas.create_window(250, 400, window=summon_value_entry)

rate_label = Label(root, text="Rate:", bg='white')
canvas.create_window(100, 450, window=rate_label)
rate_entry = Entry(root)
canvas.create_window(250, 450, window=rate_entry)

banner_label = Label(root, text="Banner:", bg='white')
canvas.create_window(100, 500, window=banner_label)
banner_entry = Entry(root)
canvas.create_window(250, 500, window=banner_entry)

# Add the summon button
summon_button = Button(root, text="Summon", command=summon)
canvas.create_window(100, 550, window=summon_button)  # Adjust button position

# Create a label to display the result
result_label = Label(root, text="Welcome to the Summon Simulator!", bg='white')
canvas.create_window(800, 550, window=result_label)  # Adjust label position

# Update the window size to fit the content
root.update_idletasks()
root.geometry(f"{bg_image.width}x{bg_image.height}")

# Start the main loop
root.mainloop()
