import pandas as pd

# Load dataset
df = pd.read_csv("dataset.csv")

# Clean text (important if you edited values)
df = df.apply(lambda col: col.str.strip().str.lower() if col.dtype == "object" else col)

print("Dataset loaded successfully!")
df.head()

print("Available moods:", df['mood'].unique())
print("Available energy levels:", df['energy_level'].unique())
print("Available sleep qualities:", df['sleep_quality'].unique())

mood = input("Enter your mood: ").strip().lower()
energy = input("Enter your energy level: ").strip().lower()
sleep = input("Enter your sleep quality: ").strip().lower()

filtered = df[
    (df['mood'] == mood) &
    (df['energy_level'] == energy) &
    (df['sleep_quality'] == sleep)
]

if filtered.empty:
    print("\nNo exact match found. Showing closest suggestions based on mood.\n")
    filtered = df[df['mood'] == mood]

sample = filtered.sample(1).iloc[0]

print("\n✨ YOUR PERSONALIZED RECOMMENDATIONS ✨\n")
print("🎵 Song:", sample['recommended_song'].title())
print("🎬 Movie:", sample['recommended_movie'].title())
print("📚 Book:", sample['recommended_book'].title())
print("🎨 Hobby:", sample['suggested_hobby'].title())
