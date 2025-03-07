import { createClient, print } from 'redis';
import { promisify } from 'util';

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

// Promisify the client.get method
const getAsync = promisify(client.get).bind(client);

/**
 * Displays the value of a school from Redis using async/await
 * @param {string} schoolName
 */
async function displaySchoolValue(schoolName) {
    try {
        const reply = await getAsync(schoolName);
        console.log(reply);
    } catch (err) {
        console.error(err);
    }
}

// Calling the functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
