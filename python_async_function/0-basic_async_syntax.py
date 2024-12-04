#!/usr/bin/env python3
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Attends de manière asynchrone un délai aléatoire compris
    entre 0 et max_delay (inclus).
    La fonction retourne le temps d'attente.

    Arguments :
        max_delay (int) : Le délai maximum en secondes. Par défaut, 10.

    Retour :
        float : Le délai réel en secondes.
    """
    delay = random.uniform(0, max_delay)  # Génère un nombre flottant aléatoire entre 0 et max_delay
    await asyncio.sleep(delay)  # Attend de manière asynchrone le délai généré
    return delay  # Retourne le délai
