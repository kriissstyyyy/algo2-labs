import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from lab9 import Trie, TrieNode, build_trie

RED = "\033[91m"
RESET = "\033[0m"


def find_autocomplete_suggestions(trie: Trie, prefix: str, limit: int = 3) -> list[str]:
    node = trie.root
    for char in prefix:
        if char not in node.children:
            return []
        node = node.children[char]

    suggestions = []

    def dfs(current_node: TrieNode, current_word: str):
        if len(suggestions) >= limit:
            return

        if current_node.is_end_of_word:
            suggestions.append(current_word)

        for symbol in sorted(current_node.children.keys()):
            dfs(current_node.children[symbol], current_word + symbol)

    dfs(node, prefix)
    return suggestions


def load_words(filename: str) -> list[str]:
    # Шукаємо файл відносно папки, де лежить цей скрипт
    base_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(base_dir, filename)

    if not os.path.exists(full_path):
        print(f"{RED}Помилка: Файл '{filename}' не знайдено.{RESET}")
        return []

    with open(full_path, "r", encoding="utf-8") as f:
        return [line.strip().lower() for line in f if line.strip()]


def main():
    filename = "words.txt"
    words = load_words(filename)

    if not words:
        return

    print(f"{RED}Завантажено слів: {len(words)}{RESET}")
    print(f"{RED}Префіксне дерево успішно побудовано.{RESET}")

    trie = build_trie(words)

    while True:
        try:
            user_input = input(f"\n{RED}Введіть префікс (або 'exit' для виходу): {RESET}").strip().lower()
            if user_input == "exit":
                break

            if not user_input:
                continue

            hints = find_autocomplete_suggestions(trie, user_input, limit=3)
            print(f"{RED}Підказки: {hints}{RESET}")

        except (KeyboardInterrupt, EOFError):
            break


if __name__ == "__main__":
    main()
    