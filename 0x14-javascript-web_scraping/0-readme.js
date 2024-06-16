#!/usr/bin/node
const fs = require("fs");
fs.readFile(process.argv[2], "utf-8", (error, body) => {
    if (error){
        console.log(error);
    }
    else {
        console.log(body.toString());
    }
})