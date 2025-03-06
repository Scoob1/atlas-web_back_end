function getPaymentTokenFromAPI(success) {
  return new Promise((resolve, reject) => {
      if (success) {
          resolve({ data: 'Successful response from the API' });
      } else {
          reject(new Error('Failed response from the API'));
      }
  });
}

module.exports = getPaymentTokenFromAPI;
