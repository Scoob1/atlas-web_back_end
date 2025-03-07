import { readDatabase } from '../utils';

class StudentsController {
  static async getAllStudents(req, res) {
    try {
      const fields = await readDatabase(req.app.get('databasePath'));

      let response = 'This is the list of our students\n';
      Object.entries(fields).sort().forEach(([field, names]) => {
        response += `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}\n`;
      });

      res.status(200).send(response);
    } catch (error) {
      res.status(500).send(`Cannot load the database: ${error.message}`);
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const { major } = req.params;

    if (major !== 'CS' && major !== 'SWE') {
      return res.status(500).send('Major parameter must be CS or SWE');
    }

    try {
      const fields = await readDatabase(req.app.get('databasePath'));
      const students = fields[major] || [];

      res.status(200).send(`List: ${students.join(', ')}`);
    } catch (error) {
      res.status(500).send(`Cannot load the database: ${error.message}`);
    }
  }
}

export default StudentsController;
