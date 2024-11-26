export default function guardrail(mathFunction) {
  const queue = [];

  try {
    // Exécuter la fonction mathFunction et ajouter le résultat à la queue
    const result = mathFunction();
    queue.push(result);
  } catch (error) {
    // En cas d'erreur, ajouter le message d'erreur à la queue
    queue.push(error.toString());
  } finally {
    // Ajouter le message final 'Guardrail was processed' à la queue
    queue.push('Guardrail was processed');
  }

  return queue;
}
