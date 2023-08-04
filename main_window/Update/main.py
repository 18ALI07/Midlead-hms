from pathlib import Path

from tkinter import Frame, Canvas, Entry, Text, Button, PhotoImage, messagebox
from controller import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")
import os
import sys
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


def update():
    Update()


class Update(Frame):
    def loginFunc(self):

        if updatePassword(self.username.get().lower(), self.password.get()):
            messagebox.showinfo("Success", "Password Updated successfully")
            self.username.delete(0,'end')
            self.password.delete(0,'end')

        else:
            messagebox.showerror(
                title="Invalid Credentials",
                message="The Security Answer Not match",
            )
    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.configure(bg="#FFFFFF")


        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=432,
            width=797,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )

        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(
            469.0, 0.0, 1012.0, 506.0, fill="#FFFFFF", outline=""
        )

        self.entry_image_1 = PhotoImage(file=resource_path(relative_to_assets("entry_1.png")))
        entry_bg_1 = self.canvas.create_image(128.0, 194.0, image=self.entry_image_1, anchor="nw",)

        entry_1 = Entry(self.canvas, bd=0, bg="#EFEFEF", highlightthickness=0)
        entry_1.place(x=128.0, y=194.0, width=336.0, height=0)

        self.entry_image_2 = PhotoImage(file=resource_path(relative_to_assets("entry_2.png")))
        entry_bg_2 = self.canvas.create_image(128.0, 92.0, image=self.entry_image_2, anchor="nw")
        entry_2 = Entry(self.canvas, bd=0, bg="#EFEFEF", highlightthickness=0)
        entry_2.place(x=128.0, y=92.0, width=336.0, height=0)

        self.canvas.create_text(
            153.0,
            206.0,
            anchor="nw",
            text="New Password",
            fill="black",
            font=("Montserrat Bold", 18 * -1),

        )
        # self.canvas.create_text(
        #     153.0,
        #     46.0,
        #     anchor="nw",
        #     text="Update Password",
        #     fill="black",
        #     font=("Montserrat Bold", 18 * -1),
        #
        # )

        self.canvas.create_text(
            153.0,
            104.0,
            anchor="nw",
            text="Security Answer",
            fill="black",
            font=("Montserrat Bold", 18 * -1),

        )
        self.button_image_1 = PhotoImage(file=resource_path(relative_to_assets("button_u.png")))
        self.button_1 = Button(
            self.canvas,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginFunc,
            relief="flat",

        )
        self.button_1.place(x=135.0, y=315.0, width=200.0, height=51.0)
        entry_image_3 = PhotoImage(file=resource_path(relative_to_assets("entry_3.png")))
        entry_bg_3 = self.canvas.create_image(736.0, 241.0, image=entry_image_3)
        self.username = Entry(
            self.canvas,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            font=("Montserrat Bold", 16 * -1),
            foreground="#120919",
        )
        self.username.place(x=153.0, y=129.0, width=326.0, height=22.0)

        entry_image_4 = PhotoImage(file=resource_path(relative_to_assets("entry_4.png")))
        entry_bg_4 = self.canvas.create_image(736.0, 342.0, image=entry_image_4)
        self.password = Entry(
            self.canvas,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            font=("Montserrat Bold", 16 * -1),
            foreground="#120919",
            show="•",
        )
        self.password.place(x=153.0, y=230.0, width=326.0, height=22.0)
        # Bind enter to form submit
        self.username.bind("<Return>", lambda x: self.loginFunc())
        self.password.bind("<Return>", lambda x: self.loginFunc())
        # self.canvas.create_text(
        #     36.0,
        #     43.0,
        #     anchor="nw",
        #     text="Staff Details",
        #     fill="#0B1011",
        #     font=("Montserrat Bold", 26 * -1),
        # )
        #
        # self.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        # image_1 = self.canvas.create_image(191.0, 26.0, image=self.image_image_1)
        #
        # self.image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        # image_2 = self.canvas.create_image(203.0, 205.0, image=self.image_image_2)
        #
        # self.image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
        # image_3 = self.canvas.create_image(565.0, 205.0, image=self.image_image_3)
        #
        # self.canvas.create_text(
        #     56.0,
        #     121.0,
        #     anchor="nw",
        #     text="Tinkerer",
        #     fill="#777777",
        #     font=("Montserrat Medium", 15 * -1),
        # )
        #
        # self.canvas.create_text(
        #     418.0,
        #     121.0,
        #     anchor="nw",
        #     text="SW-Fan",
        #     fill="#777777",
        #     font=("Montserrat Medium", 15 * -1),
        # )
        #
        # self.canvas.create_text(
        #     56.0,
        #     138.0,
        #     anchor="nw",
        #     text="Mohit",
        #     fill="#0B1011",
        #     font=("Montserrat Bold", 26 * -1),
        # )
        #
        # self.canvas.create_text(
        #     418.0,
        #     138.0,
        #     anchor="nw",
        #     text="Anirudh",
        #     fill="#0B1011",
        #     font=("Montserrat Bold", 26 * -1),
        # )
        #
        # self.canvas.create_text(
        #     56.0,
        #     170.0,
        #     anchor="nw",
        #     text="Yadav",
        #     fill="#0B1011",
        #     font=("Montserrat Bold", 18 * -1),
        # )
        #
        # self.canvas.create_text(
        #     418.0,
        #     170.0,
        #     anchor="nw",
        #     text="Agarwal",
        #     fill="#0B1011",
        #     font=("Montserrat Bold", 18 * -1),
        # )
        #
        # self.image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
        # image_4 = self.canvas.create_image(308.0, 150.0, image=self.image_image_4)
        #
        # self.canvas.create_rectangle(
        #     56.0, 197.0, 169.0, 199.0, fill="#FFFFFF", outline=""
        # )
        #
        # self.canvas.create_rectangle(
        #     418.0, 197.0, 531.0, 199.0, fill="#FFFFFF", outline=""
        # )
        #
        # self.image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
        # image_5 = self.canvas.create_image(669.0, 151.0, image=self.image_image_5)
        #
        # self.canvas.create_text(
        #     197.0,
        #     352.0,
        #     anchor="nw",
        #     text="© 2023 Designed and developed by Midlead, All rights reserved",
        #     fill="#0B1011",
        #     font=("Montserrat Bold", 16 * -1),
        # )
        # #
        # # self.canvas.create_text(
        # #     246.0,
        # #     372.0,
        # #     anchor="nw",
        # #     text="Open sourced under the MIT license",
        # #     fill="#0B1011",
        # #     font=("Montserrat Bold", 16 * -1),
        # # )
        #
        # self.canvas.create_text(
        #     418.0,
        #     207.0,
        #     anchor="nw",
        #     text="A tech-nerd and a freelance programmer,",
        #     fill="#777777",
        #     font=("Montserrat Medium", 13 * -1),
        # )
        #
        # self.canvas.create_text(
        #     418.0,
        #     223.0,
        #     anchor="nw",
        #     text="Anirudh likes to kill his time in a world of",
        #     fill="#777777",
        #     font=("Montserrat Medium", 13 * -1),
        # )
        #
        # self.canvas.create_text(
        #     418.0,
        #     239.0,
        #     anchor="nw",
        #     text="computer. He sometimes can be found in",
        #     fill="#777777",
        #     font=("Montserrat Medium", 13 * -1),
        # )
        #
        # self.canvas.create_text(
        #     418.0,
        #     255.0,
        #     anchor="nw",
        #     text="the reality, walking his dog or watching",
        #     fill="#777777",
        #     font=("Montserrat Medium", 13 * -1),
        # )
        #
        # self.canvas.create_text(
        #     418.0,
        #     271.0,
        #     anchor="nw",
        #     text="Star Wars.",
        #     fill="#777777",
        #     font=("Montserrat Medium", 13 * -1),
        # )
        #
        # self.canvas.create_text(
        #     56.0,
        #     207.0,
        #     anchor="nw",
        #     text="A coding-addict, entusiastic creator, and a",
        #     fill="#777777",
        #     font=("Montserrat Medium", 13 * -1),
        # )
        #
        # self.canvas.create_text(
        #     56.0,
        #     223.0,
        #     anchor="nw",
        #     text="passionate learner, Mohit likes to bring",
        #     fill="#777777",
        #     font=("Montserrat Medium", 13 * -1),
        # )
        #
        # self.canvas.create_text(
        #     56.0,
        #     239.0,
        #     anchor="nw",
        #     text="perfection to anything he’s doing. He’s",
        #     fill="#777777",
        #     font=("Montserrat Medium", 13 * -1),
        # )
        #
        # self.canvas.create_text(
        #     56.0,
        #     255.0,
        #     anchor="nw",
        #     text="also a passionate designer and a die-hard",
        #     fill="#777777",
        #     font=("Montserrat Medium", 13 * -1),
        # )
        #
        # self.canvas.create_text(
        #     56.0,
        #     271.0,
        #     anchor="nw",
        #     text="Avengers fan.",
        #     fill="#777777",
        #     font=("Montserrat Medium", 13 * -1),
        # )
