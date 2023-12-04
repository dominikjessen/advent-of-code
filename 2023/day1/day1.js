import fs from 'fs';

// Find first and last number, concat, total sum.
function partOne(filePath) {
  const inp = fs.readFileSync(filePath, { encoding: 'utf-8' });

  const words = inp.split('\n');

  let sum = 0;

  for (const word of words) {
    const numbers = word.replace(/\D/g, '');
    sum += parseInt(`${numbers[0]}${numbers[numbers.length - 1]}`);
  }

  console.log('Sum 1 is:', sum);
}

// Numbers can be written out (e.g. 1 as 'one'). Still look for first and last as concat and total sum.
function partTwo(filePath) {
  let map = new Map([
    ['one', 1],
    ['two', 2],
    ['three', 3],
    ['four', 4],
    ['five', 5],
    ['six', 6],
    ['seven', 7],
    ['eight', 8],
    ['nine', 9]
  ]);

  const inp = fs.readFileSync(filePath, { encoding: 'utf-8' });

  let sum = 0;
  const words = inp.split('\n');

  for (const word of words) {
    // Get all numbers or 'numbers' for words and handle cases like 'eighthree' -> 'eight', 'three'
    let matches = [];
    for (const opt of [...map.keys(), ...map.values(), 0]) {
      // Handle multiple occurrence of same word with regex matchAll
      [...word.matchAll(opt)].forEach((matchArray) => {
        matches[matchArray.index] = matchArray[0];
      });
    }

    // Remove empty array elements due to index insertion
    const numbers = matches.filter((n) => n);

    if (numbers) {
      // Convert first and last to actual number
      const num1 = numbers[0].length === 1 ? `${numbers[0]}` : `${map.get(numbers[0])}`;
      const num2 = numbers[numbers.length - 1].length === 1 ? `${numbers[numbers.length - 1]}` : `${map.get(numbers[numbers.length - 1])}`;
      sum += parseInt(`${num1}${num2}`);
    }
  }

  console.log('Sum 2 is:', sum);
}

partOne('./input.txt');
partTwo('./input.txt');
