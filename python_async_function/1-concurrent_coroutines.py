#!/usr/bin/env python3
import asyncio
import importlib

# Importation dynamique du module 0-basic_async_syntax
basic_async_syntax = importlib.import_module('0-basic_async_syntax')

# Utilisation de la fonction wait_random depuis le module importé
wait_random = basic_async_syntax.wait_random

async def wait_n(n: int, max_delay: int) -> list:
    """
    Lance n fois la fonction wait_random avec un délai max_delay et retourne
    les délais sous forme de liste triée de manière ascendante.

    Arguments :
        n (int) : Le nombre de fois où la fonction wait_random doit être appelée.
        max_delay (int) : Le délai maximum à passer à wait_random.

    Retour :
        list : Liste des délais sous forme de flottants, triée de manière ascendante.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]  # Crée une liste de tâches wait_random
    delays = await asyncio.gather(*tasks)  # Exécute toutes les tâches en parallèle
    return delays  # La liste des délais est renvoyée telle quelle
