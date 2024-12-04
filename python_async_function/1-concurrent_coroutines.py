#!/usr/bin/env python3
import asyncio
from 0-basic_async_syntax import wait_random  # Importation
# de la fonction wait_random


async def wait_n(n: int, max_delay: int):

    """
    Lance n coroutines wait_random avec le paramètre max_delay,
    et retourne une liste des délais obtenus.
    Les délais sont retournés dans l'ordre d'exécution, sans utiliser sort().

    Arguments :
        n (int) : Le nombre de coroutines à exécuter.
        max_delay (int) : Le délai maximal pour wait_random.

    Retour :
        list : Une liste de n délais (float), dans l'ordre
        d'exécution des tâches.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]  # Créer n tâches
    delays = await asyncio.gather(*tasks)  # Attendre que toutes les tâches
    # se terminent
    return delays  # Retourner la liste des délais obtenus
