#!/usr/bin/env python3
import asyncio
import time
import importlib

# Importation dynamique du module 1-concurrent_coroutines
concurrent_coroutines = importlib.import_module('1-concurrent_coroutines')

# Utilisation de la fonction wait_n depuis le module importé
wait_n = concurrent_coroutines.wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Mesure le temps total d'exécution de wait_n(n, max_delay)
    et retourne le temps moyen par exécution.

    Arguments :
        n (int) : Le nombre de fois où wait_n doit être appelé.
        max_delay (int) : Le délai maximum à passer à wait_n.

    Retour :
        float : Le temps moyen d'exécution en secondes.
    """
    start_time = time.time()  # Note l'heure de début
    asyncio.run(wait_n(n, max_delay))  # Exécute la coroutine wait_n
    end_time = time.time()  # Note l'heure de fin
    total_time = end_time - start_time  # Calcule le temps total d'exécution
    return total_time / n  # Retourne le temps moyen par appel
