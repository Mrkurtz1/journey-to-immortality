# Experience Time Tracker

A Python application to calculate and visualize progression time in game leveling systems.

## Overview

This tool helps players calculate the time required to progress through different title/rank levels in two different event systems: "Journey" and "Feast of Nature". It accounts for stamina usage to provide accurate time estimates and visualizes progression with a line chart.

## Features

- Calculate remaining time to reach different title levels
- Account for stamina efficiency in time calculations
- Visualize progression path with Matplotlib charts
- Support for two different ranking systems:
  - Journey (Q1-Q3, B1-B3, C1-C3, N1-N6)
  - Feast of Nature (C3-C1, S3-S1, B3-B1, E6-E1)
- Simple GUI interface built with Tkinter

## Requirements

- Python 3.x
- Tkinter (included in standard Python installation)
- Matplotlib (`pip install matplotlib`)

## Installation

1. Clone this repository:
   ```
   git clone https://gitlab.com/your-username/experience-time-tracker.git
   cd experience-time-tracker
   ```

2. Install required dependencies:
   ```
   pip install matplotlib
   ```

3. Run the application:
   ```
   python exp_tracker.py
   ```

## Usage

1. Select an event type from the dropdown (Journey or Feast of Nature)
2. Enter your current title/rank (e.g., "C3" for Feast of Nature or "Q1" for Journey)
3. Enter your current experience points
4. Click "Compute Time" to calculate and visualize progression

The application will display:
- Total hours remaining to max level
- A chart showing progression through each tier over time

## How It Works

The application uses the following game mechanics:
- Each stamina point takes 15 minutes to regenerate
- Experience rate is calculated based on knowledge gain
- Different title levels have different knowledge gain values
- The application optimizes stamina usage in time calculations

## Formulas

- Experience per second: `(knowledge_gain * 1.3) / 8`
- Time calculation with stamina optimization: The application calculates the optimal number of stamina uses to minimize progression time

## License

MIT Licence

## Contributing

Rivera from Discord
