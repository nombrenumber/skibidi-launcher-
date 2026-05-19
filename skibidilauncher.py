######################
#  Original Made by yanis_truc #
#  Copy made by Fripouilleuh 
# ohhh zedcuatro cuatro cuatro#
######################

import platform
import subprocess
import sys
def ilib(package_name):
    """Install a package from pip."""
    try: subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
    except subprocess.CalledProcessError: sys.exit(1)
for i in ["distro", "requests", "portablemc"]:
    ilib(i)
import distro
import requests

def check_python():
    try:
        python_version = subprocess.check_output([sys.executable, "--version"], universal_newlines=True).strip()
        return python_version
    except FileNotFoundError:
        return "Python is not installed"

def install_tkinter():
    system_name = platform.system()
    if system_name == "Linux":
        distro_name = distro.id().lower()
        if distro_name in ["debian", "ubuntu"]:
            subprocess.check_call(["sudo", "apt", "update"])
            subprocess.check_call(["sudo", "apt", "install", "-y", "python3-tk"])
        elif distro_name == "fedora":
            subprocess.check_call(["sudo", "dnf", "install", "-y", "python3-tkinter"])
        elif distro_name == "arch":
            subprocess.check_call(["sudo", "pacman", "-S", "--noconfirm", "tk"])

try:
    import tkinter as tk
    from tkinter import simpledialog
except ImportError:
    install_tkinter()

def check_tkinter():
    try:
        import tkinter as tk
        from tkinter import simpledialog
    except ImportError:
        install_tkinter()

def fetch_minecraft_versions():
    url = "https://launchermeta.mojang.com/mc/game/version_manifest.json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        versions = [version["id"] for version in data['versions'] if version['type'] == 'release']
        return versions
    except requests.RequestException as e:
        return []
def get_pseudo():
    getp = tk.Tk()
    getp.withdraw()
    return(simpledialog.askstring("Username", "Enter your username brooochacho !"))

def on_play_button_click(app_listbox, root):
    root.quit()
    selected_version = app_listbox.get(app_listbox.curselection())
    available_versions = fetch_minecraft_versions()
    if selected_version in available_versions:
        try:
            subprocess.check_call([sys.executable, "-m", "portablemc", "start", selected_version, "-u", get_pseudo()])
        except subprocess.CalledProcessError as e:
            print("Error : {e}")

def main():
    python_version = check_python()
    check_tkinter()
    versions = fetch_minecraft_versions()
    root = tk.Tk()
    root.title("Skibidi Launcher")
    root.geometry("400x400")
    root.config(bg="#f2f2f2")
    label = tk.Label(root, text="Available Versions :", font=("Helvetica", 12), bg="#f2f2f2", fg="#333")
    label.pack(pady=10)
    app_listbox = tk.Listbox(root, height=10, width=40, font=("Helvetica", 12), selectmode=tk.SINGLE)
    for app in versions:
        app_listbox.insert(tk.END, app)
    app_listbox.pack(pady=10)
    play = tk.Button(root, text="Play", command=lambda: on_play_button_click(app_listbox, root), font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", relief="raised", width=20, height=2)
    play.pack(pady=20)
    tk.Label(root, bg="#ffffff").pack(pady=10)
    root.mainloop()

if __name__ == "__main__":
    main()