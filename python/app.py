from tkinter import *
from chatbot import Botler

BG_COLOR = "#272727"
TEXT_COLOR = "#FAFAFA"
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"


class ChatApplication:
    """Runs application """

    def __init__(self):
        """Generates window GUI an initializes Chatbot"""
        self._init_window()
        self.chat = Botler()

    def _init_window(self):
        """Initializes window with corresponding settings"""
        self.window = Tk()

        # Add title to window
        self.window.title("Botler the Butler")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=420, height=720, bg=BG_COLOR)

        # text widget
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.9, relwidth=1)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)

        # bottom label
        label = Label(self.window, bg=BG_COLOR, height=80)
        label.place(relwidth=1, rely=0.9)

        # message entry box
        self.msg_entry = Entry(label, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.04, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # send button
        send_button = Button(label, text="Send", font=FONT_BOLD, width=20, bg=BG_COLOR, command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.04, relwidth=0.22)

    def run(self):
        """Runs main loop for window"""
        self.window.mainloop()

    def _on_enter_pressed(self, event):
        """If user submits its message, it processes the input to generate a response"""
        msg = self.msg_entry.get()

        if not msg:
            return

        self._insert_message(msg, "You")
        response = self.chat.generate_response(msg.lower())
        self._insert_message(response, self.chat.name)

    def _insert_message(self, msg, sender):
        """Inserts a message to the screen"""
        if not msg:
            return

        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)