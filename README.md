# Wordlist Wizard 🧙‍♂️

Welcome to **Wordlist Wizard** – the ultimate tool for creating customized wordlists, testing passwords against them, and even generating fake profiles. This project is as magical as it sounds, but remember, with great power comes great responsibility. 🪄✨

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Creating a Wordlist](#creating-a-wordlist)
  - [Testing a Password](#testing-a-password)
  - [Generating a Fake Profile](#generating-a-fake-profile)
  - [Help Menu](#help-menu)
- [Disclaimer](#disclaimer)

## Introduction

Wordlist Wizard is your trusty companion for generating custom wordlists, checking if your passwords are up to snuff, and even creating fake profiles for testing purposes. Whether you want to create a list of potential passwords or test your security against a dictionary attack, this tool has got you covered.

## Features

- **Custom Wordlist Generation**: Mix and match words to create a unique wordlist.
- **Password Testing**: Check if a password is in your custom dictionary.
- **Fake Profile Generator**: Generate fake English or French profiles for testing purposes.
- **Interactive and User-Friendly**: Easy-to-use menu with fun loading animations.

## Installation

Before you can summon the powers of the Wordlist Wizard, you need to install the required dependencies. Open your terminal and cast the following spell:

```bash
pip install termcolor unidecode
```

## Usage

Once your environment is set up, run the `main.py` script to access the magical menu:

```bash
python main.py
```

### Creating a Wordlist

1. Choose option `1` in the menu.
2. Follow the prompts to input words you want to include in the wordlist.
3. Optionally, add basic characters (like `1,2,3,...,9,!,_,-`).
4. Name your output file (don't forget to add `.txt` at the end).

### Testing a Password

1. Choose option `2` in the menu.
2. Provide the password you want to test.
3. Specify the dictionary file you want to use.
4. The wizard will let you know if your password was found.

### Generating a Fake Profile

1. Choose option `4` in the menu.
2. A random English or French profile will be generated.

### Help Menu

1. Choose option `0` in the menu.
2. Get useful information about the tool and how to switch between English and French datasets.

## Dumper: The Profile Generator

The `dumper` module is an integral part of Wordlist Wizard, providing the ability to generate random profiles. Here's how it works:

### How It Works

- **Dataset Loading**: Loads a dataset (either in English or French) to gather names, professions, hobbies, etc.
- **Random Profile Generation**: Creates a profile with randomly selected attributes such as name, date of birth, profession, hobbies, and even pets.
- **Password Generation**: Constructs a password based on the generated profile attributes.

### Sample Output

A generated profile might look like this:

```
PROFIL:
PRENOM: John
NOM: DOE
DATE DE NAISSANCE: 15/07/1985
NOMBRE DE FRÈRES ET SŒURS: 2
FRÈRES ET SŒURS:
  - Nom: Jane
    Date de naissance: 12/03/1990
  - Nom: Jack
    Date de naissance: 20/05/1992
PARENTS:
  - Nom: Michael
    Date de naissance: 04/04/1960
  - Nom: Sarah
    Date de naissance: 10/10/1962
MÉTIER: engineer
HOBBY: reading
ANIMAL DE COMPAGNIE: dog
SURNOM DE L'ANIMAL: buddy
```

The `dumper` module not only generates these profiles but also creates a sample password based on them, ensuring it's a fun and informative tool for security testing.

## Disclaimer

⚠️ **DISCLAIMER** ⚠️

This tool is intended for educational purposes and to help improve security by demonstrating the importance of strong passwords. **Do not use this tool for any malicious activities.** The author is not responsible for any misuse of this tool. Always use your powers for good!

---

Dive into the world of Wordlist Wizardry and may your passwords be ever strong! 🧙‍♂️🔒
