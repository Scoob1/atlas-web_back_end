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
 * Sets values in a Redis hash
 * @param {string} hashName - The name of the hash
 * @param {Object} values - An object containing key-value pairs to store in the hash
 */
function setHashValues(hashName, values) {
    for (const [key, value] of Object.entries(values)) {
        client.hset(hashName, key, value, print);
    }
}

/**
 * Displays the values of a Redis hash
 * @param {string} hashName - The name of the hash
 */
function displayHashValues(hashName) {
    client.hgetall(hashName, (err, reply) => {
        if (err) {
            console.error(err);
        } else {
            console.log(reply);
        }
    });
}

// Values to store in the HolbertonSchools hash
const holbertonSchoolsValues = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2,
};

// Set the hash values and display the hash
setHashValues('HolbertonSchools', holbertonSchoolsValues);
displayHashValues('HolbertonSchools');

