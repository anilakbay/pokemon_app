from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from data import *

co0 = "#444466"  # black
co1 = "#feffff"  # white
co2 = "#6f9fbd"  # blue
co3 = "#403d3d"  # ash

window = Tk()
window.title("")
window.geometry('550x510')
window.configure(bg=co1)
window.resizable(width=FALSE, height=FALSE)

ttk.Separator(window, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

main_frame = Frame(window, width=540, height=305, bg=co1)
main_frame.grid(row=0, column=0, padx=1, pady=1)

def choose_pokemon(i):
    global i_icon_1, pokemon_image
    main_frame['bg'] = pokemon[i]['others'][1]

    pok_name['text'] = i
    pok_name['bg'] = pokemon[i]['others'][1]
    pok_type['text'] = pokemon[i]['others'][1]
    pok_type['bg'] = co3
    pok_number['text'] = pokemon[i]['others'][0]
    pok_number['bg'] = pokemon[i]['others'][1]

    image = pokemon[i]['others'][0]
    pokemon_image = Image.open(image)
    pokemon_image = pokemon_image.resize((250, 250))
    pokemon_image = ImageTk.PhotoImage(pokemon_image)

    l_icon_1 = Label(main_frame, image=pokemon_image, bg=pokemon[i]['others'][1])
    l_icon_1.place(x=60, y=50)

    if i == 'Pikachu':
        pok_name['fg'] = co0
    else:
        pok_name['fg'] = co1

    pok_hp['text'] = pokemon[i]['status'][0]
    pok_attack['text'] = pokemon[i]['status'][1]
    pok_defence['text'] = pokemon[i]['status'][2]
    pok_speed['text'] = pokemon[i]['status'][3]
    pok_total['text'] = pokemon[i]['status'][4]

    pok_hb_1['text'] = pokemon[i]['skills'][0]
    pok_hb_1['text'] = pokemon[i]['skills'][1]

    pok_type.lift()
    pok_number.lift()

pok_name = Label(main_frame, text="Pokemon name", anchor="center", font="Ivy 20 bold", fg=co1)
pok_name.place(x=15, y=15)

pok_type = Label(main_frame, text="Pokemon type", anchor="center", font="Verdana 10 bold", fg=co1)
pok_type.place(x=20, y=50)

pok_number = Label(main_frame, text="Pokemon number", anchor="center", font="Verdana 13 bold", fg=co0)
pok_number.place(x=20, y=75)

pok_type.lift()
pok_number.lift()

pok_status = Label(window, text="Status", font="Verdana 20", bg=co1, fg=co0)
pok_status.place(x=15, y=310)

pok_hp = Label(window, text="HP:100", font="Verdana 10", bg=co1, fg=co0)
pok_hp.place(x=20, y=360)

pok_attack = Label(window, text="Attack:300", font="Verdana 10", bg=co1, fg=co0)
pok_attack.place(x=20, y=385)

pok_defence = Label(window, text="Defence:500", font="Verdana 10", bg=co1, fg=co0)
pok_defence.place(x=20, y=410)

pok_speed = Label(window, text="Speed:100", font="Verdana 10", bg=co1, fg=co0)
pok_speed.place(x=20, y=435)

pok_total = Label(window, text="Total", font="Verdana 10 bold", bg=co1, fg=co0)
pok_total.place(x=20, y=460)

pok_skill = Label(window, text="Skill", font="Verdana 20", bg=co1, fg=co0)
pok_skill.place(x=180, y=310)

pok_hb_1 = Label(window, text="Thunder", font="Verdana 10", bg=co1, fg=co0)
pok_hb_1.place(x=195, y=360)

pok_hb_2 = Label(window, text="Hydro Pump", font="Verdana 10", bg=co1, fg=co0)
pok_hb_2.place(x=195, y=385)

img_pok_1 = Image.open('images/pikachu-head.png')
img_pok_1 = img_pok_1.resize((40, 40))
img_pok_1 = ImageTk.PhotoImage(img_pok_1)

icon_1 = Button(window, text='Pikachu', command=lambda:choose_pokemon('Pikachu'), width=150, image=img_pok_1, padx=5, compound=LEFT, overrelief=RIDGE, anchor=NW, font='Verdana 12', bg=co1, fg=co0)
icon_1.place(x=375, y=10)

img_pok_2 = Image.open('images/bulbasaur-head.png')
img_pok_2 = img_pok_2.resize((40, 40))
img_pok_2 = ImageTk.PhotoImage(img_pok_2)

icon_2 = Button(window, text='Bulbasaur', command=lambda:choose_pokemon('Bulbasaur'), width=150, image=img_pok_2, padx=5, compound=LEFT, overrelief=RIDGE, anchor=NW, font='Verdana 12', bg=co1, fg=co0)
icon_2.place(x=375, y=65)

img_pok_3 = Image.open('images/charmander-head.png')
img_pok_3 = img_pok_3.resize((40, 40))
img_pok_3 = ImageTk.PhotoImage(img_pok_3)

icon_3 = Button(window, text='Charmander', command=lambda:choose_pokemon('Charmander'), width=150,  image=img_pok_3, padx=5, compound=LEFT, overrelief=RIDGE, anchor=NW, font='Verdana 12', bg=co1, fg=co0)
icon_3.place(x=375, y=120)

img_pok_4 = Image.open('images/gyarados-head.png')
img_pok_4 = img_pok_4.resize((40, 40))
img_pok_4 = ImageTk.PhotoImage(img_pok_4)

icon_4 = Button(window, text='Gyarados', command=lambda:choose_pokemon('Gyarados'), width=150, image=img_pok_4, padx=5, compound=LEFT, overrelief=RIDGE, anchor=NW, font='Verdana 12', bg=co1, fg=co0)
icon_4.place(x=375, y=175)

img_pok_5 = Image.open('images/gengar-head.jpg')
img_pok_5 = img_pok_5.resize((40, 40))
img_pok_5 = ImageTk.PhotoImage(img_pok_5)

icon_5 = Button(window, text='Gengar', command=lambda:choose_pokemon('Gengar'), width=150, image=img_pok_5, padx=5, compound=LEFT, overrelief=RIDGE, anchor=NW, font='Verdana 12', bg=co1, fg=co0)
icon_5.place(x=375, y=230)

img_pok_6 = Image.open('images/dragonite-head.png')
img_pok_6 = img_pok_6.resize((40, 40))
img_pok_6 = ImageTk.PhotoImage(img_pok_6)

icon_6 = Button(window, text='Dragonite', command=lambda:choose_pokemon('Dragonite'), width=150, image=img_pok_6, padx=5, compound=LEFT, overrelief=RIDGE, anchor=NW, font='Verdana 12', bg=co1, fg=co0)
icon_6.place(x=375, y=285)

choose_pokemon('Pikachu')

window.mainloop()