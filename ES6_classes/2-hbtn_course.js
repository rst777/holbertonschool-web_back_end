export default class HolbertonCourse {
  constructor(name, length, students) {
    // Vérification des types des attributs
    if (typeof name !== 'string') {
      throw new TypeError('Name must be a string');
    }
    if (typeof length !== 'number') {
      throw new TypeError('Length must be a number');
    }
    if (!Array.isArray(students) || !students.every(student => typeof student === 'string')) {
      throw new TypeError('Students must be an array of strings');
    }

    // Assignation des attributs avec un underscore
    this._name = name;
    this._length = length;
    this._students = students;
  }

  // Getter pour name
  get name() {
    return this._name;
  }

  // Setter pour name
  set name(value) {
    if (typeof value !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = value;
  }

  // Getter pour length
  get length() {
    return this._length;
  }

  // Setter pour length
  set length(value) {
    if (typeof value !== 'number') {
      throw new TypeError('Length must be a number');
    }
    this._length = value;
  }

  // Getter pour students
  get students() {
    return this._students;
  }

  // Setter pour students
  set students(value) {
    if (!Array.isArray(value) || !value.every(student => typeof student === 'string')) {
      throw new TypeError('Students must be an array of strings');
    }
    this._students = value;
  }
}
