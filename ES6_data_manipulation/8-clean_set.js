export default function cleanSet(set, startString) {
  // Vérifie si startString est vide ou non valide
  if (!startString || typeof startString !== 'string') {
    return '';
  }

  // Filtre et transforme les valeurs du set qui commencent par startString
  const result = Array.from(set)
    .filter((value) => typeof value === 'string' && value.startsWith(startString))
    .map((value) => value.slice(startString.length)) // Retire startString
    .join('-'); // Joint les valeurs par un tiret

  return result;
}
