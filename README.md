# Fellowship Readiness Tracker

A web app used in a hands-on debugging workshop. You will learn how to find and fix bugs using real developer tools — both with and without AI assistance.

---

## Before the Workshop — Get This Done First

Please complete the following steps **before** you arrive. If you run into issues, reach out early so we can help.

### 1. Install Python 3

Check if you already have it:
```bash
python3 --version
```

If not installed, download it from [python.org/downloads](https://www.python.org/downloads/) or use Homebrew on Mac:
```bash
brew install python
```

### 2. Install Git

Check if you already have it:
```bash
git --version
```

If not installed: [git-scm.com/downloads](https://git-scm.com/downloads)

### 3. Install VS Code

Download from [code.visualstudio.com](https://code.visualstudio.com/)

Install these two extensions inside VS Code:
- **Python** (by Microsoft)
- **Pylance** (by Microsoft)

### 4. Clone This Repository

```bash
git clone https://github.com/sabman83/fellowship-readiness-tracker.git
cd fellowship-readiness-tracker
```

### 5. Install Dependencies

```bash
pip3 install flask
```

### 6. Run the App

```bash
python3 app.py
```

Then open your browser and go to: [http://127.0.0.1:5001](http://127.0.0.1:5001)

You should see the Fellowship Readiness Tracker dashboard with a list of students.

> **Note for Mac users:** If you get an "Address already in use" error on port 5000, the app is already configured to use port 5001. If 5001 is also taken, let your coach know.

### 7. Make Sure Your Browser DevTools Work

Open Chrome or Firefox, go to any webpage, and press:
- **Mac:** `Cmd + Option + I`
- **Windows:** `F12` or `Ctrl + Shift + I`

You should see the Developer Tools panel open. Click through the **Console**, **Network**, and **Sources** tabs so they feel familiar.

---

## What We'll Cover in the Workshop

- Debugging Python using **print statements** and the **VS Code debugger**
- Debugging JavaScript using **Browser DevTools** (Console, Network tab, Sources breakpoints)
- Using **`git bisect`** to find which commit introduced a bug
- Comparing debugging **with and without AI**

---

## You Do Not Need

- Any prior debugging experience
- Any accounts or logins beyond GitHub
- To read or understand the app code beforehand — we'll walk through it together

---

## Questions?

Reach out before the workshop if anything above isn't working. The setup is quick, but it's important to have it ready so we can spend our time debugging, not installing.
