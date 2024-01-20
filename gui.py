from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from api_requests import api_operations
from api_requests import LST_OF_STATS
from api_requests import LST_OF_ACTIVE_PLAYERS


WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
WINDOW_Y_PADDING = 10
WINDOW_X_PADDING = 50
LABEL_X_PADDING = 20
CANVAS_WIDTH = 300
CANVAS_HEIGHT = 150
LOGO_WIDTH = 300
LOGO_HEIGHT = 150
PLAYERS_LABEL_FONT = ("Courier",25,"normal")
BUTTON_FONT = ("Courier",15,"normal")
STAT_FONT = ("Courier",10,"normal")

player1_stats_labels = []
player2_stats_labels = []


class Gui:

    def __init__(self):
        self.window = Tk()
        self.window.title("Player Comparison Program")
        self.window.config(width=WINDOW_WIDTH,height=WINDOW_HEIGHT,padx=WINDOW_X_PADDING,pady=WINDOW_Y_PADDING)
        self.create_canvas()
        self.create_combobox()
        self.create_buttons()
        self.create_stats_labels()
        self.create_player_labels()
        self.window.mainloop()
    
    def create_canvas(self):
        logo_img = PhotoImage(file="NBA-Logo.png")
        self.canvas = Canvas(width=CANVAS_WIDTH,height=CANVAS_HEIGHT)
        self.canvas.image = logo_img
        self.canvas.create_image(150,70,image=logo_img)
        self.canvas.grid(row=0,column=0,columnspan=2)

    def check_input(self,event,player):
        value = event.widget.get()

        if value == '':
            if player == "player1":
                self.player1_combo_box['values'] = LST_OF_ACTIVE_PLAYERS
            else:
                self.player2_combo_box['values'] = LST_OF_ACTIVE_PLAYERS
        else:
            data = []
            for item in LST_OF_ACTIVE_PLAYERS:
                if value.lower() in item.lower():
                    data.append(item)
            if player == "player1":
                self.player1_combo_box['values'] = data
            else:
                self.player2_combo_box['values'] = data
        
    def create_combobox(self):
        self.player1_combo_box = ttk.Combobox(self.window)
        self.player2_combo_box = ttk.Combobox(self.window)

        self.player1_combo_box["values"] = LST_OF_ACTIVE_PLAYERS
        self.player2_combo_box["values"] = LST_OF_ACTIVE_PLAYERS

        self.player1_combo_box.bind('<KeyRelease>', lambda event,player="player1": self.check_input(event,player))
        self.player2_combo_box.bind('<KeyRelease>', lambda event,player="player2": self.check_input(event,player))

        self.player1_combo_box.grid(row=2,column=0)
        self.player2_combo_box.grid(row=2,column=1)
    

    def create_player_labels(self):
        self.player1_label = Label(text="Player 1:",font=PLAYERS_LABEL_FONT,padx=LABEL_X_PADDING)
        self.player1_label.grid(row=1,column=0)
        self.player2_label = Label(text="Player 2:",font=PLAYERS_LABEL_FONT,pady=LABEL_X_PADDING)
        self.player2_label.grid(row=1,column=1)


    def create_buttons(self):
        self.compare_button = Button(text="Compare",font=BUTTON_FONT,command=self.get_entry_input)
        self.compare_button.grid(row=3,column=0,columnspan=2)

    def create_stats_labels(self):
        for index,stat in enumerate(LST_OF_STATS):
            player1_label = Label(text=f"{stat}",font=STAT_FONT)
            player2_label = Label(text=f"{stat}",font=STAT_FONT)

            player1_label.grid(row=index+4,column=0)
            player2_label.grid(row=index+4,column=1)

            player1_stats_labels.append(player1_label)
            player2_stats_labels.append(player2_label)
 

    def get_entry_input(self):
        player_1_name = self.player1_combo_box.get()
        player_2_name = self.player2_combo_box.get()
        
        player1_stats,player2_stats = api_operations(player_1_name,player_2_name)
        if not player1_stats or not player2_stats:
            messagebox.showerror(message="One of the names is incorrect",title="Error")
        else:
            self.update_stats_labels(player1_stats,player2_stats)

    
    def update_stats_labels(self,player1_stats,player2_stats):
        for label1,label2,stat in zip(player1_stats_labels,player2_stats_labels,LST_OF_STATS):
            label1.config(text=f"{stat}: {player1_stats[stat]}")
            label2.config(text=f"{stat}: {player2_stats[stat]}")
    
