import pandas as pd
from bs4 import BeautifulSoup
import os

def html_to_markdown(html):
    """
    Convert HTML content to Markdown format.
    """
    soup = BeautifulSoup(html, 'html.parser')
    return soup.get_text(" ", strip=True)

def update_markdown(csv_file_path, markdown_file_path):
    """
    Update the Markdown file with new words from the CSV file.
    If a word already exists, update the notes section only.
    """
    # Read the CSV file
    df = pd.read_csv(csv_file_path)
    df['单词'] = df['单词'].apply(lambda x: f'[[{x}]]')
    df['解释'] = df['解释'].apply(html_to_markdown)

    # Check if the Markdown file exists and read its content
    existing_content = ""
    if os.path.exists(markdown_file_path):
        with open(markdown_file_path, 'r', encoding='utf-8') as file:
            existing_content = file.read()

    # Update or append content
    with open(markdown_file_path, 'w', encoding='utf-8') as file:
        for index, row in df.iterrows():
            word_section = f"### {row['单词']}\n"
            if word_section not in existing_content:
                file.write(word_section)
                file.write(f"**音标:** {row['音标']}\n\n")
                file.write(f"**解释:** {row['解释']}\n\n")
                if pd.notna(row['笔记']):
                    file.write(f"**笔记:** {row['笔记']}\n\n")
                file.write("---\n\n")
            else:
                # If the word exists, update the notes section only
                note_section = f"**笔记:** {row['笔记']}\n\n" if pd.notna(row['笔记']) else ""
                existing_content = existing_content.replace(word_section, word_section + note_section)
        if existing_content:
            file.write(existing_content)

# Example usage
csv_file_path = '生词本CSV导出/2024-01-22_生词本.csv'  # Replace with your new CSV file path
markdown_file_path = 'your_markdown_file.md'  # Replace with your existing Markdown file path
update_markdown(csv_file_path, markdown_file_path)
