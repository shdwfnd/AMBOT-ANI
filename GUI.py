import tkinter as tk

LARGE_FONT_STYLE = ("Cambria", 30, "bold")
SMALL_FONT_STYLE = ("Cambria", 16)
DEFAULT_FONT_STYLE = ("Cambria", 20)


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("370x590")
        self.window.iconbitmap("calc_icon.ico")
        self.window.resizable(0, 0)
        self.window.title("Calculator")

        self.total_expression = ""
        self.current_expression = ""
        self.prev_ans = ""
        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_labels()
        self.digits = {
            7: (3, 1), 8: (3, 2), 9: (3, 3),
            4: (4, 1), 5: (4, 2), 6: (4, 3),
            1: (5, 1), 2: (5, 2), 3: (5, 3),
            ".": (6, 2), 0: (6, 1)
        }
        self.operations1 = {"*": "\u00D7", "+": "+"}
        self.operations2 = {"/": "\u00F7", "-": "-"}
        self.buttons_frame = self.create_buttons_frame()

        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)
        # BASIC BUTTONS
        self.create_digit_buttons()
        self.create_operator1_buttons()
        self.create_operator2_buttons()
        self.create_delete_button()
        self.create_equals_button()
        self.create_clear_button()
        self.create_additional_buttons()

    def create_additional_buttons(self):
        self.create_square_button()
        self.create_sqrt_button()
        self.create_cube_button()
        self.create_exp_button()
        self.create_right_parenthesis_button()
        self.create_left_parenthesis_button()
        self.create_ans_button()
        self.create_tan_button()
        self.create_sin_button()
        self.create_cos_button()
        self.create_pi_button()
        self.create_log_button()
        self.create_ln_button()
        self.create_abs_button()
        self.create_e_button()
        self.create_permutation_button()
        self.create_combination_button()

    # row 0
    def create_pi_button(self):
        button = tk.Button(self.buttons_frame, text="π", bg="gray10", fg="ghost white", font=DEFAULT_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def create_log_button(self):
        button = tk.Button(self.buttons_frame, text="log", bg="gray10", fg="ghost white", font=DEFAULT_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def create_ln_button(self):
        button = tk.Button(self.buttons_frame, text="ln", bg="gray10", fg="ghost white", font=DEFAULT_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    def create_abs_button(self):
        button = tk.Button(self.buttons_frame, text="abs", bg="gray10", fg="ghost white", font=DEFAULT_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=0, column=4, sticky=tk.NSEW)

    def create_e_button(self):
        button = tk.Button(self.buttons_frame, text="e", bg="gray10", fg="ghost white", font=DEFAULT_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=0, column=5, sticky=tk.NSEW)

    # row 1
    def create_sin_button(self):
        button = tk.Button(self.buttons_frame, text="sin", bg="gray10", fg="ghost white", font=DEFAULT_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=1, column=1, sticky=tk.NSEW)

    def create_cos_button(self):
        button = tk.Button(self.buttons_frame, text="cos", bg="gray10", fg="ghost white", font=DEFAULT_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=1, column=2, sticky=tk.NSEW)

    def create_tan_button(self):
        button = tk.Button(self.buttons_frame, text="tan", bg="gray10", fg="ghost white", font=DEFAULT_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=1, column=3, sticky=tk.NSEW)

    def create_left_parenthesis_button(self):
        button = tk.Button(self.buttons_frame, text="(", bg="gray10", fg="ghost white",
                           font=DEFAULT_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=1, column=4, sticky=tk.NSEW)

    def create_right_parenthesis_button(self):
        button = tk.Button(self.buttons_frame, text=")", bg="gray10", fg="ghost white",
                           font=DEFAULT_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=1, column=5, sticky=tk.NSEW)

    # row 2
    def create_square_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00b2", bg="gray10", fg="ghost white", font=DEFAULT_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=2, column=1, sticky=tk.NSEW)

    def create_sqrt_button(self):
        button = tk.Button(self.buttons_frame, text="\u221ax", bg="gray10", fg="ghost white", font=DEFAULT_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=2, column=2, sticky=tk.NSEW)

    def create_cube_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00b3", bg="gray10", fg="ghost white", font=DEFAULT_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=2, column=3, sticky=tk.NSEW)

    def create_permutation_button(self):
        button = tk.Button(self.buttons_frame, text="nPr", bg="gray10", fg="ghost white", font=DEFAULT_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=2, column=4, sticky=tk.NSEW)

    def create_combination_button(self):
        button = tk.Button(self.buttons_frame, text="nCr", bg="gray10", fg="ghost white", font=DEFAULT_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=2, column=5, sticky=tk.NSEW)

    # row 3
    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg="gray6", fg="ghost white", font=SMALL_FONT_STYLE,
                               borderwidth=0)
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="AC", bg="firebrick3", fg="ghost white", font=DEFAULT_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=3, column=4, sticky=tk.NSEW)

    def create_delete_button(self):
        button = tk.Button(self.buttons_frame, text="del", bg="firebrick3", fg="ghost white", font=DEFAULT_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=3, column=5, sticky=tk.NSEW)

    # row 4 and 5
    def create_operator1_buttons(self):
        i = 4
        for operator, symbol in self.operations1.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg="gray10", fg="ghost white", font=DEFAULT_FONT_STYLE,
                               borderwidth=0)
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def create_operator2_buttons(self):
        i = 4
        for operator, symbol in self.operations2.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg="gray10", fg="ghost white", font=DEFAULT_FONT_STYLE,
                               borderwidth=0)
            button.grid(row=i, column=5, sticky=tk.NSEW)
            i += 1

    # row 6
    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg="chocolate1", fg="ghost white", font=DEFAULT_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=6, column=5, sticky=tk.NSEW)

    def create_ans_button(self):
        button = tk.Button(self.buttons_frame, text="Ans", bg="gray6", fg="ghost white", font=DEFAULT_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=6, column=4, sticky=tk.NSEW)

    def create_exp_button(self):
        button = tk.Button(self.buttons_frame, text="EXP", bg="gray6", fg="ghost white", font=DEFAULT_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=6, column=3, sticky=tk.NSEW)

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg="gray37",
                               fg="lavender", padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill='both')

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg="gray37",
                         fg="lavender", padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill='both')

        return total_label, label

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, )
        frame.pack(expand=True, fill="both")
        return frame

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
