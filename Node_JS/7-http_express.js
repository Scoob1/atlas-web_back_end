const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
app.get('/', (req, res) => {
    res.status(200).send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
    const filepath = './database.csv';
    const studentsList = await countStudents(filepath);
    res.status(200).send(`This is the list of our students\n${studentsList}`);
});

app.listen(1245, () => {
    console.log('...');
});

module.exports = app;
