import customtkinter as ctk

app = ctk.CTk()
app.title("Inicio de Sesión")

#Función para centrar las ventanas ref: https://github.com/TomSchimansky/CustomTkinter/discussions/1820
def centerwindow(Screen: ctk, width: int, height: int, scale_factor: float = 1.0):
    screen_width = Screen.winfo_screenwidth()
    screen_height = Screen.winfo_screenheight()
    x = int(((screen_width/2) - (width/2)) * scale_factor)
    y = int(((screen_height/2) - (height/1.5)) * scale_factor)
    return f"{width}x{height}+{x}+{y}"

def login():
    user = entry_user.get()
    password = entry_password.get()
    print("Iniciar sesión como:",user,"\ncon contraseña:", password)

entry_user = ctk.CTkEntry(app, justify="center", placeholder_text="USUARIO")
entry_user.grid(row=0, column=0, padx=10, pady=10)

entry_password = ctk.CTkEntry(app, justify="center", placeholder_text="CONTRASEÑA", show="•")
entry_password.grid(row=1, column=0, padx=10, pady=10)

boton = ctk.CTkButton(app, text="Iniciar Sesión", command=login)
boton.grid(row=2, column=0, padx=10, pady=10)

app.grid_columnconfigure(0, weight=1)

app.geometry(centerwindow(app, 300, 150, app._get_window_scaling()))

app.mainloop()
