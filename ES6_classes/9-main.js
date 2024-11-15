import list from './9-hoisting';

console.log(list);

const listPrinted = list.map((student) => (
  student.fullStudentDescription
));

console.log(listPrinted);
