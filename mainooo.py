from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import json

# ------- PASSWORD GENERATOR ------------- #

import random
def generate_pswd():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    pswd_entry.insert(0, password)


# ----------- SAVE PASSWORD ----------- #

def save():
    
    website_data = web_entry.get()
    email_data = email_entry.get()
    password_data = pswd_entry.get()
    new_data = {
        website_data:{
            "email": email_data,
            "password":password_data
        }

    }
    
    if len(website_data) == 0 or len(password_data) == 0:
        messagebox.showinfo(title="Oops", message = "Please make sure you havent left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title="Website", message=f"Your details entered are: \nEmail: {email_data}"f"\nPassword: {password_data} /\n Is it okay to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    #reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json","w") as data_file:
                    json.dump(new_data,data_file,indent=4)
            else:
                #updata data
                data.update(new_data)
                
                with open("data.json","w") as data_file:
                    json.dump(data,data_file,indent=4)
            finally:
                    web_entry.delete(0, END)
                    pswd_entry.delete(0, END)


# ------------FIND PASSWORD ------------- #   
            
def find_pswd():
    website = web_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data File found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists")    
            
              
# ------------ UI SETUP ------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=40,pady=40)

canvas = Canvas(width = 200, height = 200)
photo = PhotoImage(file = "logo.png")
canvas.create_image(100,100, image = photo)
canvas.grid(column = 0, row = 0,columnspan=3)

website = Label(text = "Website: ")
website.grid(column=0, row=1)

web_entry = Entry(width=21)
web_entry.grid(column=1, row=1)
web_entry.focus()

email = Label(text = "Email/Username: ")
email.grid(column=0, row=2)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2,columnspan=2)
email_entry.insert(0, "example@gmail.com")

pswd = Label(text = "Password: ")
pswd.grid(column=0, row=3)

pswd_entry = Entry(width=21)
pswd_entry.grid(column=1, row=3)

pswd_generate = Button(text = "Generate Password", command = generate_pswd)
pswd_generate.grid(column=2, row=3)

add_button = Button(text = "Add" ,width = 36, command = save)
add_button.grid(column=1, row=4,columnspan=2)

search = Button(text = "Search", width=13, command = find_pswd)
search.grid(column=2, row=1)



mainloop()
