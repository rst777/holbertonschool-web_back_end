export default function updateUniqueItems(map) {
  // Vérifie si l'argument est un Map
  if (!(map instanceof Map)) {
    throw new Error('Cannot process');
  }

  // Parcourt chaque élément du Map
  map.forEach((value, key) => {
    if (value === 1) {
      map.set(key, 100); // Met à jour les quantités égales à 1
    }
  });

  return map;
}
