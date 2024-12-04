#!/usr/bin/env python3
import asyncio
import importlib

# Importation dynamique du module 3-tasks
tasks_module = importlib.import_module('3-tasks')

# Accès à la fonction task_wait_random depuis le module importé
task_wait_random = tasks_module.task_wait_random

async def task_wait_n(n: int, max_delay: int):
    """
    Crée et attend n tâches asyncio, chacune exécutant la fonction task_wait_random avec max_delay.

    Arguments :
        n (int) : Le nombre de tâches à exécuter.
        max_delay (int) : Le délai maximal pour wait_random.

    Retour :
        list : Une liste contenant les délais obtenus, triés dans l'ordre d'exécution.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]  # Créer n tâches
    delays = await asyncio.gather(*tasks)  # Attendre que toutes les tâches se terminent
    return delays  # Retourner la liste des délais obtenus
