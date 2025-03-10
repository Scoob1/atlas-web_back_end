import { createClient } from 'redis';

const subscriber = createClient();

subscriber.on('connect', () => {
    console.log('Redis client connected to the server');
});

subscriber.on('error', (err) => {
    console.error('Redis client not connected to the server:', err.message);
});

subscriber.connect().catch((err) => {
    console.error('Redis client not connected to the server:', err.message);
});

subscriber.subscribe('holberton school channel', (message) => {
    console.log(message);
    if (message === 'KILL_SERVER') {
        subscriber.unsubscribe('holberton school channel');
        subscriber.quit();
    }
});

