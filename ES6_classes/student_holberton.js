// student_holberton.js

export class StudentHolberton {
  constructor(firstName, lastName, holbertonClass) {
    this._firstName = firstName; // Assignation de l'attribut _firstName
    this._lastName = lastName; // Assignation de l'attribut _lastName
    this._holbertonClass = holbertonClass; // Assignation de l'attribut _holbertonClass
  }

  get fullName() {
    return `${this._firstName} ${this._lastName}`; // Getter pour le nom complet
  }

  get holbertonClass() {
    return this._holbertonClass; // Renvoie l'objet _holbertonClass
  }

  get fullStudentDescription() {
    return `${this.fullName} - ${this.holbertonClass.year} - ${this.holbertonClass.location}`; // Description complète de l'étudiant
  }
}
