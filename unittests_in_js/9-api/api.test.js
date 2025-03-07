const request = require('request');
const { expect } = require('chai');

describe('Payment system', () => {
    describe('GET /', () => {
        it('Returns "Welcome to the payment system"', (done) => {
            request('http://localhost:7865/', (error, response, body) => {
                expect(response.statusCode).to.equal(200);
                expect(body).to.equal('Welcome to the payment system');
                done();
            });
        });
    });
    describe('GET /cart/:id', () => {
        it('Returns Payment methods for cart number', (done) => {
            const id = 12;
            request(`http://localhost:7865/cart/${id}`, (error, response, body) => {
                expect(response.statusCode).to.equal(200);
                expect(body).to.equal(`Payment methods for cart ${id}`);
                done();
            });
        });
        it('Returns 404 when :id is NOT a number', (done) => {
            request('http://localhost:7865/cart/hello', (error, response, body) => {
                expect(response.statusCode).to.equal(404);
                done();
            });
        });
    });
});
