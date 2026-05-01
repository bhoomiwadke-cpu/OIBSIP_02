# OIBSIP_02
BMI_ CALCULATOR<BR>
AUTHOR-BHOOMI SANJAY WADKE
# 🏋️ BMI Calculator — Advanced GUI

A desktop BMI (Body Mass Index) calculator built with Python, featuring a clean Tkinter GUI and a matplotlib-powered trend chart to track your BMI over time.

![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![GUI](https://img.shields.io/badge/GUI-Tkinter-orange)

---

## ✨ Features

- **Instant BMI calculation** from weight (kg) and height (m)
- **WHO category classification** — Underweight, Normal weight, Overweight, Obese
- **Session history tracking** — logs every calculation in memory
- **BMI trend chart** — visualises your history with a matplotlib line graph
- **Input validation** — friendly error dialogs for invalid entries

---

## 📋 Requirements

- Python 3.7 or higher
- [matplotlib](https://matplotlib.org/)

Tkinter ships with the standard Python installer on Windows and macOS. Linux users may need to install it separately (see [Installation](#installation)).

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/bmi-calculator.git
cd bmi-calculator
```

### 2. Install dependencies

```bash
pip install matplotlib
```

**Linux only** — install Tkinter if it is missing:

```bash
# Debian / Ubuntu
sudo apt-get install python3-tk

# Fedora
sudo dnf install python3-tkinter
```

### 3. Run the app

```bash
python bmi_gui.py
```

---

## 🖥️ Usage

1. Enter your **weight in kilograms** in the first field.
2. Enter your **height in metres** in the second field (e.g. `1.75`).
3. Click **Calculate BMI** — your result and category appear instantly.
4. Repeat for additional entries; each result is saved to your session history.
5. Click **Show History** to open a line chart of all BMI values recorded this session.

---

## 📊 BMI Categories

| BMI Range | Category |
|-----------|----------|
| Below 18.5 | Underweight |
| 18.5 – 24.9 | Normal weight |
| 25.0 – 29.9 | Overweight |
| 30.0 and above | Obese |

*Based on World Health Organization (WHO) classifications.*

---

## 📁 Project Structure

```
bmi-calculator/
└── bmi_gui.py   # Main application — GUI, logic, and history chart
```

---

## 🔮 Potential Improvements

- [ ] Persist history to a CSV or SQLite database between sessions
- [ ] Add imperial units (lbs / inches) with automatic conversion
- [ ] Support multiple named user profiles
- [ ] Export the trend chart as a PNG
- [ ] Package as a standalone executable with PyInstaller

---

## ⚠️ Disclaimer

This tool is intended for general informational purposes only and does not constitute medical advice. Consult a qualified healthcare professional for personalised guidance.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
