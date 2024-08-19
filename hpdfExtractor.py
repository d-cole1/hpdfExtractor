import PySimpleGUI as sg
from functions import extract_func

# Define a custom theme for the GUI
my_new_theme = {'BACKGROUND': "#31363b",
                'TEXT': "#f9f1ee",
                'INPUT': "#232629",
                'TEXT_INPUT': "#f9f1ee",
                'SCROLL': "#333a41",
                'BUTTON': ('#31363b', '#0dd1fc'),
                'PROGRESS': ('#f9f1ee', '#31363b'),
                'BORDER': 1,
                'SLIDER_DEPTH': 0,
                'PROGRESS_DEPTH': 0}

# Add and set the custom theme
sg.theme_add_new("MyNewTheme", my_new_theme)
sg.theme("MyNewTheme")
sg.set_options(font=("Segoe UI Variable", 11))

logo = r"C:\Users\dominick.cole\Python\hpdfExtractor\logos\applogo.ico"
e_logo = r"C:\Users\dominick.cole\Python\hpdfExtractor\logos\error.ico"
s_logo = r"C:\Users\dominick.cole\Python\hpdfExtractor\logos\success.ico"

layout = [
    [sg.Text("Select directory:"), sg.Input(), sg.FolderBrowse("Browse", key='source')],
    [sg.Button("Extract")]
]

window = sg.Window("HPDF Extractor", layout, icon=logo)

while True:
    event, values = window.read()

    match event:

        case sg.WIN_CLOSED:
            break

        case "Extract":
            extract_func(window, values)

        case "Done":
            sg.popup("SUCCESS!\n\n"
                     "The .hpdf has been extracted into a new folder within your original"
                     " folder selection.\n",
                     custom_text="Exit", icon=s_logo)
            break

        case "Error":
            error_message = values[event]

            if error_message == "no_files_found":
                sg.popup("No .hpdf files found.",
                         custom_text="Exit", icon=e_logo)
                break

            else:
                sg.popup(f"An unknown error has occurred.\n"
                         f"{error_message}",
                         custom_text="Exit", icon=e_logo)
                break

window.close()
