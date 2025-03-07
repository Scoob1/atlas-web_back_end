const fs = require('fs').promises;

async function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    try {
      const data = fs.readFile(filePath, 'utf8');
      resolve(data);
    } catch (error) {
      reject(new Error(error));
    }
  });
}

module.exports = readDatabase;
