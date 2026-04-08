# 🛡️ Digital Detox Tracker
A lightweight, Python-based CLI tool designed to help you break the habit of scrolling through Instagram Reels and Youtube Shorts. This tool focuses on reclaiming your mental focus and physical health through daily discipline and motivational reinforcement.

## 🌟 Features
### Streak Tracking: 
Automatically calculates your daily progress.

### No-Install Design: 
Runs directly via Python without needing complex packages or pip.

### Randomized Motivation: 
Provides a different encouraging sentence every day to keep you inspired.

### Health-Focused: 
Includes specific reminders to stay away from provocative content and preserve your physical energy.

## 🚀 Installation & Setup
### 1. Download the Tool
Open your terminal and clone this folder:
```
git clone https://github.com/rhitamcoder/detox-tracker.git
```
```
cd detox-tracker
```
*(Alternatively, click the green **Code** button on Github and select **Download ZIP**.)*

### 2. Make it a Global Command
To run the tracker by typing 'detox' from a terminal:
```
sudo ln -s $(pwd)/tracker.py /usr/local/bin/detox && chmod +x tracker.py
```
### 🎮 How to Use
Simply open your terminal and type:
```
detox
```
*If you didn't do the "Global Command" above, you can run it manually inside the folder using:*
```
python3 tracker.py
```
### The Logic
**1. Input:** The tool will ask if you successfully avoided Reels/Shorts today.

**2. Reward:** If you enter **'y'**, you get a motivational quote and your streak increases.

**3. Reset:** If you miss a day or enter **'n'**, the streak resets to 0. Discipline is key!

### 🛠️ Requirements
**Python 3.x:** (Installed by default on almost every Linux system).

**Linux/Unix:** Works perfectly on Arch, Ubuntu, Fedora, Mint, (Any Ubuntu-based distros) & MacOS.

## 🧠 Why I Built This
This tool was created to fight the "infinite scroll" addiction that affects out dopamine levels and physical health. By forcing a manual clock check-in every day, we build mindfulness and take back control of our time.

"Your Attention is your most valuable asset. Don't trade your long-term goals for a 30-second distraction."

## 📈 Why use this?
By using a manual tracker, you are:

**1. Building Mindfulness:** Forcing yourself to consciously acknowledge your progress.

**2. Reclaiming Physical Health:** Turning away from provocative content that drains your energy.

**3. Mastering Discipline:** Proving that you are the master of your machine, not the other way around.

### Contributing:
Since this is a community-focused tool, feel free to **Fork** this repo and add your own motivational sentences to the code of mine.

