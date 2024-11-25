export default function createInt8TypedArray(length, position, value) {
  // Crée un ArrayBuffer de la longueur spécifiée
  const buffer = new ArrayBuffer(length);
  const view = new DataView(buffer);

  // Vérifie si la position est valide
  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }

  // Écrit la valeur Int8 à la position spécifiée
  view.setInt8(position, value);

  return view;
}
