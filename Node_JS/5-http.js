const http = require('node:http');
const url = require('url');
const countStudents = require('./3-read_file_async');

const app = http.createServer(async (req, res) => {
    const parsedUrl = url.parse(req.url, true);

    if (parsedUrl.pathname === '/') {
        res.statusCode = 200;
        res.setHeader('Content-Type', 'text/plain');
        res.end('Hello Holberton School!');
    } else if (parsedUrl.pathname === '/students') {
        res.statusCode = 200;
        res.setHeader('Content-Type', 'text/plain');
        try {
            const studentsList = await countStudents(path);
            res.end(`This is the list of our students\n${studentsList}`);
        } catch (error) {
            res.statusCode = 500;
            res.end('Not Found');
        }
    } else {
        res.statusCode = 404;
        res.end('Not Found');
    }
});

app.listen(1245, () => {
    console.log('Server is listening on port 1245');
});
