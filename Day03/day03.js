const fs = require("fs");
const path = require("path");

// Function to check if a cell is adjacent to a symbol
function isAdjacentToSymbol(row, col) {
    const rowOffsets = [-1, 0, 1];
    const colOffsets = [-1, 0, 1];
    const symbols = ['%', '#', '*', '/', '@', '$', '&', '=', '+', '-'];

    for (const rowOffset of rowOffsets) {
        for (const colOffset of colOffsets) {
            // Check if the neighboring cell is within bounds
            if (
                !(row + rowOffset < 0 || row + rowOffset >= inputRows.length ||
                col + colOffset < 0 || col + colOffset >= inputRows[0].length)
            ) {
                // Check if the neighboring cell contains a symbol
                if (symbols.includes(inputRows[row + rowOffset][col + colOffset])) {
                    return true;
                }
            }
        }
    }
    return false;
}

const inputFilePath = path.join(__dirname, "schema.txt");
const inputRows = String(fs.readFileSync(inputFilePath)).trim().split("\n");

const numbersInParts = [];
let tempNumber = '';
let isPartOfPart = false;

// Iterate through each row in the input data
for (let row = 0; row < inputRows.length; row++) {
    for (let col = 0; col < inputRows[row].length; col++) {
        const currentCharacter = inputRows[row][col];
        
        // Check if the current character is an integer (part of a number)
        if (Number.isInteger(+currentCharacter)) {
            tempNumber += currentCharacter;
            // Check if the current number is part of a larger part
            isPartOfPart = (isPartOfPart || isAdjacentToSymbol(row, col));
        }

        // Check if the current character is not an integer or if it's the end of the row
        if (!Number.isInteger(+currentCharacter) || col === inputRows[row].length - 1) {
            if (tempNumber.length > 0) {
                // If the number is part of a larger part, add it to the list
                if (isPartOfPart) {
                    numbersInParts.push(+tempNumber);
                }
                tempNumber = '';
                isPartOfPart = false;
            }
        }
    }
}

// Print the sum of all numbers in parts
console.log(numbersInParts.reduce((accumulator, currentValue) => accumulator + currentValue));
