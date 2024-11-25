export default function hasValuesFromArray(set, array) {
  // Vérifie si tous les éléments de l'array sont dans le set
  return array.every((value) => set.has(value));
}
