function printLeftTriangle(n) {
    /**
    * Prints a left-aligned triangle with n rows.
    *
    * @param {number} n - The number of rows in the triangle
    * @returns {void}
    */
    
    for (let i = 0; i <= n; i++) {
        let text = '';
        for (let j = 0; j < i; j++) {
            text += '*'
        }
        console.log(text);
    }

}

function printCenteredTriangle(n) {
    /**
    * Prints a centered triangle with n rows.
    *
    * @param {number} n - The number of rows in the triangle
    * @returns {void}
    */
    
    for (let i = 0; i <= n; i++) {
        let text = '';
        for (let j = 0; j < n-i; j++) {
            text += ' '
        }

        for (let j = 0; j < 2*i-1; j++) {
            text += '*'
        }

        console.log(text);
    }
}

// Example usage:
function main() {
    // You can replace this with your own input method
    const n = 5;
    console.log("Left-aligned triangle:");
    printLeftTriangle(n);
    console.log("\nCentered triangle:");
    printCenteredTriangle(n);
}
main();
