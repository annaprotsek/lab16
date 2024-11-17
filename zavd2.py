from collections import Counter
import matplotlib.pyplot as plt

text_content = """
Once upon a time in a small village, there lived a wise old man. He spent his days reading books, helping others, and telling fascinating stories to the children. The villagers admired him for his kindness and wisdom. One day, a traveler visited the village and asked the old man about the secret to happiness. The old man smiled and said, "Happiness lies in helping others and appreciating the simple joys of life." The traveler thanked him and left the village with a heart full of gratitude.
"""

with open('protsek.txt', 'w', encoding='utf-8') as file:
    file.write(text_content)

with open('protsek.txt', 'r', encoding='utf-8') as file:
    text = file.read().lower()

filtered_text = ''.join(filter(str.isalpha, text))

letter_counts = Counter(filtered_text)

letters = sorted(letter_counts.keys())
frequencies = [letter_counts[letter] for letter in letters]

plt.bar(letters, frequencies, color='skyblue')
plt.title('Частота англійських літер у тексті (protsek.txt)')
plt.xlabel('Літери')
plt.ylabel('Частота')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
