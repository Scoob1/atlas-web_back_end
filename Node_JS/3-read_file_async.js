const fs = require('fs').promises;

const countStudents = (path) => {
    return new Promise(async (resolve, reject) => {
        try {
            const data = await fs.readFile(path, 'utf8');
            const lines = data.trim().split('\n').filter(line => line);

            if (lines.length === 0) {
                console.log('Number of students: 0');
                resolve();
                return;
            }

            const students = lines.slice(1).map(line => line.split(','));
            const fields = {};

            students.forEach(student => {
                const [firstname, , , field] = student;
                if (!fields[field]) {
                    fields[field] = [];
                }
                fields[field].push(firstname);
            });

            console.log(`Number of students: ${students.length}`);
            for (const [field, names] of Object.entries(fields)) {
                console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
            }

            resolve();
        } catch (error) {
            reject(new Error('Cannot load the database'));
        }
    });
};

module.exports = countStudents;
