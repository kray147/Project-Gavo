# Project Gavo

Welcome to Project Gavo! This is an experimental pentesting tool that aims to generate custom wordlists for use in brute force attacks against specific users based on their information.

This application requires `itertools` and `unidecode`. If you don't have them installed, simply run and to get out of this:
pip install itertools
pip install unidecode


**Note:** This script is more of a fun project than something genuinely useful.

## News!

Soon enough, i will make the person generator usable without option 3

## Purpose

In the first place, I was developing a custom wordlist builder in Python. However, I thought it would be amusing to mix it with a random person creator to simulate real attacks against passwords.

**Disclaimer:** I don't consider this tool very dangerous, but it should not be used for malicious purposes such as brute force attacks against real people. I take no responsibility for any harm that could be done. I'm only the developer of a tool built for fun.

## Functionality

### I) The Wordlist Builder

- **Option 1:** Helps you generate a custom wordlist.
- **Option 2:** A test feature to verify the generated wordlist contains a password that should be in it.

### II) The Fake Person Maker

- **Functionalities:** It is only able to generate french persons for now, with french labours etc... but soon I will change the structure to be able to use any csv file as base for the generation database thus ensuring
compatibility with other languages.
- **Option 3:** This is the most comprehensive option. It generates a fake individual and associated life data. You can then choose to create a custom wordlist based on this information and test it out. You'll receive a validation message if it works!

That's all for now! Enjoy using Project Gavo :)

**Author:** QuantumKray
