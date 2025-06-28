#!/usr/bin/env python3

"""Hello World Multi Languages

This script displays a message in the language configured on your system.

Usage:

Make sure the system variable LANG is set. Example:

    export LANG=pt_BR

Execution:

    python3 hello.py
    or
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Romulo Alcantara"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "en_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour, Monde!"

# Programa inicial
print(msg)
