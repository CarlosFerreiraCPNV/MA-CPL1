# tokenizer.py – Version avec vocabulaire (mot → id)

import re
import sys


# -----------------------------------------------------------
# 1) MODE 1 : découpe naïve par espaces
# -----------------------------------------------------------

def tokenize_whitespace(text):
    """
    Retourne une liste de tokens découpés par espaces.
    """
    return text.split()


# -----------------------------------------------------------
# 2) MODE 2 : découpe avec regex
# -----------------------------------------------------------

TOKEN_RE = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿ]+|\d+|[.,;:!?/(\\)\"]")


def tokenize_regex(text):
    """
    Retourne une liste de tokens basés sur la regex.
    """
    return TOKEN_RE.findall(text)


# -----------------------------------------------------------
# 3) Construction du vocabulaire
# -----------------------------------------------------------

def build_vocab(tokens):
    """
    Crée un vocabulaire : token -> id unique
    """
    vocab = {}
    next_id = 0

    for x in tokens:
        if x not in vocab:
            vocab[x] = next_id
            next_id += 1

    return vocab


# -----------------------------------------------------------
# 4) Interface en ligne de commande (CLI)
# -----------------------------------------------------------

# Usage :
# python tokenizer.py whitespace "le chat et le chat"
# python tokenizer.py regex "Bonjour le monde ! Bonjour !"

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(1)

    mode = sys.argv[1]
    text = " ".join(sys.argv[2:])

    # Tokenisation
    if mode == "whitespace":
        tokens = tokenize_whitespace(text)
    elif mode == "regex":
        tokens = tokenize_regex(text)
    else:
        print("Mode inconnu.")
        sys.exit(1)

    # Vocabulaire
    vocab = build_vocab(tokens)

    token_result = []

    # Affichage
    print(F"ID      mot\n")
    for x in tokens:
        print(f"{vocab[x]}\t{x}")
        token_result.append(vocab[x])

    print("\nALL TOKENS")
    print(token_result)
