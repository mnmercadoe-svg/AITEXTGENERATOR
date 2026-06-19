def save_text(text, filename="output.txt"):
    with open(f"exports/{filename}", "w", encoding="utf-8") as f:
        f.write(text)

