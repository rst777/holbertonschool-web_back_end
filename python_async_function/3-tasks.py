#!/usr/bin/env python3
import asyncio
import importlib

# Importation dynamique du module 0-basic_async_syntax
basic_async_syntax = importlib.import_module('0-basic_async_syntax')

# Utilisation de la fonction wait_random depuis le module importé
wait_random = basic_async_syntax.wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Crée et retourne une tâche asyncio exécutant la coroutine wait_random.

    Arguments :
        max_delay (int) : Le délai maximal pour wait_random.

    Retour :
        asyncio.Task : Un objet Task représentant l'exécution de wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
