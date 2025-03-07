import { createClient, print } from 'redis';

const client = createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.error('Redis client not connected to the server:', err.message);
});

client.connect().catch((err) => {
    console.error('Redis client not connected to the server:', err.message);
});

/**
 * Sets a new school in Redis
 * @param {string} schoolName
 * @param {string} value
 */
function setNewSchool(schoolName, value) {
    client.set(schoolName, value, print);
}

/**
 * Displays the value of a school from Redis
 * @param {string} schoolName
 */
function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, reply) => {
        if (err) {
            console.error(err);
        } else {
            console.log(reply);
        }
    });
}

// Calling the functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

