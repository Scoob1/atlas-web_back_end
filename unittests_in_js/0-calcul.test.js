// 0-calcul.test.js
const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function() {
    it('should return 4 when inputs are 1 and 3', function() {
        assert.strictEqual(calculateNumber(1, 3), 4);
    });

    it('should return 5 when inputs are 1 and 3.7', function() {
        assert.strictEqual(calculateNumber(1, 3.7), 5);
    });

    it('should return 5 when inputs are 1.2 and 3.7', function() {
        assert.strictEqual(calculateNumber(1.2, 3.7), 5);
    });

    it('should return 6 when inputs are 1.5 and 3.7', function() {
        assert.strictEqual(calculateNumber(1.5, 3.7), 6);
    });

    it('should return 0 when inputs are 0 and 0', function() {
        assert.strictEqual(calculateNumber(0, 0), 0);
    });

    it('round the second number', function()  {
        assert.equal(calculateNumber(0, 1.5), 2);
        assert.equal(calculateNumber(0, 1.8), 2);
        assert.equal(calculateNumber(0, 2.3), 2);
    });

    it('round the first number', function()  {
        assert.equal(calculateNumber(2.5, 0), 3);
        assert.equal(calculateNumber(2.8, 0), 3);
        assert.equal(calculateNumber(3.2, 0), 3);
    });

    it('return the correct number', function() {
        assert.equal(calculateNumber(2.7, 0), 3);
        assert.equal(calculateNumber(0, 2.5), 3);
        assert.equal(calculateNumber(2.7, 2.7), 6);
        assert.equal(calculateNumber(3.1, 2.5), 6);
        assert.equal(calculateNumber(2.7, 3.2), 6);
    });
});
