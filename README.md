# NBA Comparison App

A Python desktop application that allows users to compare NBA players' statistics side by side. This tool enables basketball fans, analysts, and enthusiasts to easily visualize and contrast player performance data.

## 🏀 Features

- **Player Comparison**: Select and compare statistics for any two NBA players side by side
- **Comprehensive Stats**: View key player statistics including:
  - Games Played (GP)
  - Minutes Played (MIN)
  - Field Goal Percentage (FG_PCT)
  - 3-Point Field Goal Percentage (FG3_PCT)
  - Free Throw Percentage (FT_PCT)
  - Rebounds (REB)
  - Assists (AST)
  - Steals (STL)
  - Blocks (BLK)
  - Turnovers (TOV)
  - Points (PTS)
- **Simple Interface**: User-friendly GUI built with Tkinter

## 💻 Technologies Used

- **Language**: Python
- **GUI Framework**: Tkinter
- **Data Source**: NBA Statistics API

## 📋 Prerequisites

- Python 3.x
- Required Python packages (see requirements.txt)

## ⚙️ Installation and Setup

1. Clone the repository
   ```bash
   git clone https://github.com/orati1111/Nba-Comparison-App.git
   cd Nba-Comparison-App
   ```

2. Install required dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application
   ```bash
   python main.py
   ```

## 📊 Usage

1. Launch the application
2. Select the first player from the dropdown menu
3. Select the second player for comparison
4. The application will fetch the players' statistics and display them side by side
5. Compare the statistics across various metrics (GP, MIN, FG_PCT, etc.)

## 🔍 How It Works

The application makes API calls to retrieve NBA player statistics, processes the data, and presents it through a Tkinter GUI interface. Users can select different players to compare their performance across key basketball metrics.
