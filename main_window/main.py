from pathlib import Path
from tkinter import (
    Toplevel,
    Frame,
    Canvas,
    Button,
    PhotoImage,
    messagebox,
    StringVar,
)
from controller import *
from main_window.dashboard.gui import Dashboard
from main_window.reservations.main import Reservations
from main_window.Update.main import Update
from main_window.rooms.main import Rooms
from main_window.guests.main import Guests
# from main import Login
import sys
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)




class MainWindow(Toplevel):
    global user

    def __init__(self, *args, **kwargs):
        Toplevel.__init__(self, *args, **kwargs)

        self.title("Midlead")
        self.iconbitmap(resource_path(relative_to_assets('logo.ico')))
        self.geometry("1012x506")
        self.configure(bg="#5E95FF")

        self.current_window = None
        self.current_window_label = StringVar()

        self.canvas = Canvas(
            self,
            bg="#5E95FF",
            height=506,
            width=1012,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )

        self.canvas.place(x=0, y=0)

        self.canvas.create_rectangle(
            215, 0.0, 1012.0, 506.0, fill="#FFFFFF", outline=""
        )

        # Add a frame rectangle
        self.sidebar_indicator = Frame(self, background="#FFFFFF")

        self.sidebar_indicator.place(x=0, y=133, height=47, width=7)

        button_image_1 = PhotoImage(file=resource_path(relative_to_assets("button_1.png")))
        self.dashboard_btn = Button(
            self.canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.dashboard_btn, "dash"),
            cursor='hand2', activebackground="#5E95FF",
            relief="flat",
        )
        self.dashboard_btn.place(x=7.0, y=133.0, width=208.0, height=47.0)

        button_image_2 = PhotoImage(file=resource_path(relative_to_assets("button_2.png")))
        self.rooms_btn = Button(
            self.canvas,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.rooms_btn, "roo"),
            cursor='hand2', activebackground="#5E95FF",
            relief="flat",
        )
        self.rooms_btn.place(x=7.0, y=183.0, width=208.0, height=47.0)

        button_image_3 = PhotoImage(file=resource_path(relative_to_assets("button_3.png")))
        self.guests_btn = Button(
            self.canvas,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.guests_btn, "gue"),
            cursor='hand2', activebackground="#5E95FF",
            relief="flat",
        )
        self.guests_btn.place(x=7.0, y=283.0, width=208.0, height=47.0)

        button_image_4 = PhotoImage(file=resource_path(relative_to_assets("update.png")))
        self.about_btn = Button(
            self.canvas,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.about_btn, "abt"),
            cursor='hand2', activebackground="#5E95FF",
            relief="flat",
        )
        self.about_btn.place(x=7.0, y=333.0, width=200.0, height=37.0)

        button_image_5 = PhotoImage(file=resource_path(relative_to_assets("button_5.png")))
        self.logout_btn = Button(
            self.canvas,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.logout,
            relief="flat",
        )
        self.logout_btn.place(x=0.0, y=441.0, width=215.0, height=47.0)
        # button_image_u = PhotoImage(file=relative_to_assets("update.png"))
        # self.update_btn = Button(
        #     self.canvas,
        #     image=button_image_u,
        #     borderwidth=0,
        #     highlightthickness=0,
        #     command=self.update,
        #     relief="flat",
        #     background="#5E95FF"
        # )
        # self.update_btn.place(x=0.0, y=400.0, width=215.0, height=47.0)

        button_image_6 = PhotoImage(file=resource_path(relative_to_assets("button_6.png")))
        self.reservations_btn = Button(
            self.canvas,
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.reservations_btn, "res"),
            cursor='hand2', activebackground="#5E95FF",
            relief="flat",

        )
        self.reservations_btn.place(x=7.0, y=233.0, width=208.0, height=47.0)

        self.heading = self.canvas.create_text(
            255.0,
            33.0,
            anchor="nw",
            text="",
            fill="#5E95FF",
            font=("Montserrat Bold", 26 * -1),
        )

        self.canvas.create_text(
            28.0,
            21.0,
            anchor="nw",
            text="Midlead",
            fill="#FFFFFF",
            font=("Montserrat Bold", 36 * -1),
        )

        self.canvas.create_text(
            844.0,
            43.0,
            anchor="nw",
            text="Administrator",
            fill="#808080",
            font=("Montserrat Bold", 16 * -1),
        )

        # self.canvas.create_text(
        #     341.0,
        #     213.0,
        #     anchor="nw",
        #     text="(The screens below",
        #     fill="#5E95FF",
        #     font=("Montserrat Bold", 48 * -1),
        # )
        #
        # self.canvas.create_text(
        #     420.0,
        #     272.0,
        #     anchor="nw",
        #     text="will come here)",
        #     fill="#5E95FF",
        #     font=("Montserrat Bold", 48 * -1),
        # )

        # Loop through windows and place them
        self.windows = {
            "dash": Dashboard(self),
            "roo": Rooms(self),
            "gue": Guests(self),
            "abt": Update(self),
            "res": Reservations(self),
        }

        self.handle_btn_press(self.dashboard_btn, "dash")
        self.sidebar_indicator.place(x=0, y=133)

        self.current_window.place(x=215, y=72, width=1013.0, height=506.0)

        self.current_window.tkraise()
        self.resizable(False, False)
        # from exit import on_exit
        self.protocol("WM_DELETE_WINDOW", self.logout)
        self.mainloop()

    def place_sidebar_indicator(self):
        pass

    def logout(self):
        confirm = messagebox.askyesno(
            "Confirm log-out", "Do you really want to log out?"
        )
        if confirm == True:
            user = None
            # self.destroy()
            self.master.destroy()
            # Login(root)

    def handle_btn_press(self, caller, name):
        # Place the sidebar on respective button
        self.sidebar_indicator.place(x=0, y=caller.winfo_y())

        # Hide all screens
        for window in self.windows.values():
            window.place_forget()

        # Set ucrrent Window
        self.current_window = self.windows.get(name)

        # Show the screen of the button pressed
        self.windows[name].place(x=215, y=72, width=1013.0, height=506.0)

        # Handle label change
        current_name = self.windows.get(name)._name.split("!")[-1].capitalize()
        self.canvas.itemconfigure(self.heading, text=current_name)

    def handle_dashboard_refresh(self):
        # Recreate the dash window
        self.windows["dash"] = Dashboard(self)
