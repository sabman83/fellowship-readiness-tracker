# Workshop Setup Instructions

Complete all of the steps below **before** the workshop. If you run into any issues, reach out early so we can help.

This guide covers setup for **Mac**, **Windows**, and **Linux**.

---

## Step 1: Open Your Terminal

You will use the terminal (also called the command line) throughout this workshop. Here is how to open it on your platform:

### Mac

1. Press `Cmd + Space` to open Spotlight Search
2. Type **Terminal** and press Enter

You should see a window with a command prompt — something like `yourusername@MacBook ~ %`.

### Windows

1. Press the **Windows key** on your keyboard (or click the Start menu)
2. Type **Command Prompt** and press Enter

You should see a window with a command prompt — something like `C:\Users\YourName>`.

> **Tip:** If you later install Git for Windows (Step 3), you will also get **Git Bash**, which is another terminal option. Either Command Prompt or Git Bash will work for this workshop.

### Linux

1. Press `Ctrl + Alt + T` to open a terminal window

If that shortcut does not work, look for **Terminal** in your applications menu.

---

## Step 2: Install Python 3

Python is the programming language used by the backend of this app.

### Check if you already have Python installed

Open your terminal and run:

```bash
python3 --version
```

If you see a version number like `Python 3.10.x` or higher, you are good to go — skip ahead to Step 3.

If you get an error like "command not found", follow the instructions below for your platform.

> **Windows note:** On Windows, the command might be `python` instead of `python3`. Try both. If `python --version` shows Python 3.x, you are fine.

### Mac

**Option A — Using the installer:**

1. Go to [python.org/downloads](https://www.python.org/downloads/)
2. Download the latest Python 3 installer for macOS
3. Open the downloaded file and follow the installation steps

**Option B — Using Homebrew (if you have it):**

```bash
brew install python
```

### Windows

1. Go to [python.org/downloads](https://www.python.org/downloads/)
2. Download the latest Python 3 installer for Windows
3. **Important:** On the first screen of the installer, check the box that says **"Add python.exe to PATH"**. This is critical — if you miss this, Python will not work from the command line
4. Click **Install Now** and follow the remaining steps

After installation, **close and reopen** your Command Prompt, then verify:

```bash
python --version
```

You should see `Python 3.x.x`.

### Linux

Most Linux distributions come with Python 3 pre-installed. If not:

**Ubuntu / Debian:**

```bash
sudo apt update
sudo apt install python3 python3-pip
```

**Fedora:**

```bash
sudo dnf install python3 python3-pip
```

After installation, verify:

```bash
python3 --version
```

---

## Step 3: Install Git

Git is a version control tool that lets you download (clone) the project code.

### Check if you already have Git installed

Open your terminal and run:

```bash
git --version
```

If you see a version number, you are good to go — skip ahead to Step 4.

### Mac

When you run `git --version` for the first time, macOS may prompt you to install the **Xcode Command Line Tools**. If it does:

1. Click **Install** in the dialog that appears
2. Wait for the installation to finish (this can take a few minutes)
3. Run `git --version` again to confirm it worked

If you do not get that prompt, you can install Git manually:

```bash
xcode-select --install
```

### Windows

1. Go to [git-scm.com/downloads](https://git-scm.com/downloads/win)
2. Download the installer for Windows
3. Run the installer — the default settings are fine for everything. Just keep clicking **Next** until it finishes

After installation, **close and reopen** your Command Prompt, then verify:

```bash
git --version
```

> **Note:** The Git installer also installs **Git Bash**, which gives you a Unix-like terminal on Windows. You can use either Git Bash or Command Prompt for the rest of these instructions.

### Linux

**Ubuntu / Debian:**

```bash
sudo apt update
sudo apt install git
```

**Fedora:**

```bash
sudo dnf install git
```

After installation, verify:

```bash
git --version
```

---

## Step 4: Install VS Code

VS Code is the code editor we will use in the workshop.

1. Go to [code.visualstudio.com](https://code.visualstudio.com/)
2. Download the installer for your platform (Mac, Windows, or Linux)
3. Install it using the default settings

### Install required extensions

Once VS Code is open:

1. Click the **Extensions** icon in the left sidebar (it looks like four small squares)
2. Search for and install these two extensions:
   - **Python** (by Microsoft)
   - **Pylance** (by Microsoft)

These extensions give you syntax highlighting, error detection, and debugging support for Python code.

---

## Step 5: Clone the Repository

Cloning downloads a copy of the project code to your computer.

Open your terminal and run:

```bash
git clone https://github.com/sabman83/fellowship-readiness-tracker.git
```

Then navigate into the project folder:

```bash
cd fellowship-readiness-tracker
```

> **Tip:** You can choose where to clone the project. By default it will be created in whatever folder your terminal is currently in. If you want it on your Desktop, first run:
>
> - **Mac / Linux:** `cd ~/Desktop`
> - **Windows:** `cd %USERPROFILE%\Desktop`
>
> Then run the `git clone` command above.

### Open the project in VS Code

Now open the project folder in VS Code so you can browse and edit the code:

**Option A — From the terminal:**

```bash
code .
```

This opens VS Code with the current folder. If this command does not work, see the troubleshooting note below.

**Option B — From VS Code:**

1. Open VS Code
2. Go to **File > Open Folder** (on Mac: **File > Open...**)
3. Navigate to the `fellowship-readiness-tracker` folder you just cloned and select it

> **Troubleshooting the `code` command:**
>
> If you get "command not found" when running `code .`:
>
> - **Mac:** Open VS Code, press `Cmd + Shift + P`, type **"Shell Command: Install 'code' command in PATH"**, and select it. Then restart your terminal and try again.
> - **Windows:** The `code` command is usually set up automatically during installation. If it is not working, try closing and reopening your Command Prompt. If it still does not work, use Option B above.
> - **Linux:** The `code` command is usually available after installing VS Code via your package manager. If not, use Option B above.

---

## Step 6: Install the Python Dependencies

The app uses Flask, a lightweight web framework for Python. Install it by running:

**Mac / Linux:**

```bash
pip3 install flask
```

**Windows:**

```bash
pip install flask
```

> **Troubleshooting:** If you get a "pip not found" error:
>
> - **Mac / Linux:** Try `python3 -m pip install flask`
> - **Windows:** Try `python -m pip install flask`
>
> If that still does not work, Python may not have been added to your PATH. Go back to Step 2 and reinstall Python, making sure to check the "Add to PATH" box.

---

## Step 7: Run the App

Make sure you are inside the project folder (`fellowship-readiness-tracker`), then run:

**Mac / Linux:**

```bash
python3 app.py
```

**Windows:**

```bash
python app.py
```

You should see output like:

```
 * Running on http://127.0.0.1:5001
```

Open your web browser (Chrome or Firefox recommended) and go to:

**[http://127.0.0.1:5001](http://127.0.0.1:5001)**

You should see the **Fellowship Readiness Tracker** dashboard with a list of students and their scores.

> **Troubleshooting:**
>
> - If you see **"Address already in use"**, another program is using that port. Let your coach know.
> - If the page does not load, make sure the terminal is still running (do not close it) and double-check the URL.
> - To stop the app, go back to the terminal and press `Ctrl + C`.

---

## Step 8: Check Your Browser Developer Tools

We will use browser Developer Tools during the workshop for debugging. Let us make sure they work.

> **Important:** Please use **Chrome** or **Firefox** for the workshop. Their developer tools are more intuitive and easier to follow along with. Safari or other browsers may work differently.

1. Open **Chrome** or **Firefox** (either is fine)
2. Go to any webpage
3. Open Developer Tools:
   - **Mac:** `Cmd + Option + I`
   - **Windows / Linux:** `F12` or `Ctrl + Shift + I`

You should see a panel appear at the bottom or side of your browser. Click through these three tabs so they feel familiar:

- **Console** — shows errors and log messages
- **Network** — shows web requests the page makes
- **Sources** (Chrome) or **Debugger** (Firefox) — shows the page's code

You do not need to understand what everything does yet — we will cover it in the workshop.

---

## Before the Workshop — Pull the Latest Code

The project may be updated between now and the workshop. On the day of (or the night before), open your terminal, navigate to the project folder, and run:

```bash
cd fellowship-readiness-tracker
git pull
```

This makes sure you have the latest version of the code.

---

## You Are All Set!

If you completed all the steps above and the app loads in your browser, you are ready for the workshop. If anything did not work, reach out before the workshop so we can help.
