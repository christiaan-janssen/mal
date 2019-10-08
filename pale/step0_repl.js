const readlineSync = require('readline-sync');

function main() {
    while (true) {
        var input = readlineSync.question("user> ");
            rep(input);
    }
}

function READ(input) { return input }
function EVAL(input) { return input }
function PRINT(input) { return input }
function rep(input) {
    console.log(PRINT(EVAL(READ(input))));
}

main();