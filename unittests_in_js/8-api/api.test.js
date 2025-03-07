const request = require('request');
const expect = require('chai').expect;

describe('Index page', function() {
    it('Correct status code?', function(done) {
        request('http://localhost:7865/', function (error, response) {
            if (error) return done(error);
            expect(response.statusCode).to.equal(200);
            done();
        });
    });

    it('Correct result?', function(done) {
        request('http://localhost:7865/', function (error, response, body) {
            if (error) return done(error);
            expect(body).to.equal('Welcome to the payment system');
            done();
        });
    });

    it('Other?', function(done) {

        done();
    });
});
