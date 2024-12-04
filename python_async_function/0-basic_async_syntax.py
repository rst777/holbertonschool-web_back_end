#!/usr/bin/env python3
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Coroutine asynchrone qui attend un délai aléatoire entre 0 et max_delay
    (inclus) et retourne ce délai.

    Arguments :
        max_delay (int) : Le délai maximal (en secondes) pour attendre
        (par défaut 10).

    Retour :
        float : Le délai aléatoire obtenu entre 0 et max_delay.
    """
    delay = random.uniform(0, max_delay)  # Génère un délai aléatoire
    await asyncio.sleep(delay)  # Attend ce délai
    return delay  # Retourne le délai généré
