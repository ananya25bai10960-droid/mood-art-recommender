# Mood-Based Wellness Recommendation System

## Overview
This project is a Mood-Based Wellness Recommendation System that suggests music, movies, books, and hobbies based on a user's emotional state, energy level, sleep quality, and personal preferences.

The goal of this project is to explore how basic AI and ML concepts such as data-driven decision making, filtering, and rule-based recommendation systems can be applied to mental wellness and everyday life.

This project was developed as part of the **Bring Your Own Project (BYOP)** component for the course *Fundamentals of AI and ML*.

---

## Problem Statement
Mental health and emotional well-being are often overlooked in daily routines. People may feel sad, anxious, numb, or overwhelmed but are unsure what kind of content or activity would help them feel better.

This project aims to solve that problem by providing gentle, personalized recommendations that align with the user's mood and preferences.

---

## Solution Approach
- A custom dataset was created that maps moods, energy levels, sleep quality, and preferences to suitable recommendations.
- User inputs are collected through an interactive interface.
- The system filters the dataset to find the closest matching recommendation.
- If an exact match is not found, a fallback strategy ensures the user still receives meaningful suggestions.

---

## Features
- Mood-based personalization
- Energy and sleep-aware recommendations
- Suggestions for:
  - Music
  - Movies
  - Books
  - Hobbies
- Friendly interface built using Streamlit
- Graceful handling of partial matches

---

## Technologies Used
- Python
- Pandas
- Streamlit

---

## Project Structure
mood_music_recommender/
│
├── app_ui.py
├── dataset.csv
├── requirements.txt
├── README.md
└── report.pdf


---

## How to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/mood_music_recommender.git
cd mood_music_recommender
2. Install Dependencies
pip install -r requirements.txt
3. Run the Application
streamlit run app_ui.py
4. Open in Browser

The app will open automatically at:

http://localhost:8501
Learning Outcomes
Understood how datasets influence recommendation systems
Applied basic AI logic without complex models
Improved debugging and error-handling skills
Learned how to structure and document a real-world project
Author

Developed by a BTech CSE student as part of the Fundamentals of AI and ML course. 
