const express = require('express');
const sequelize = require('sequelize');

const models = require('./models');
const services = require('./services');

function initializeDatabase() {
  return new Sequelize('sqlite:nikolaus.db');
}

function main() {
  const app = express();
  app.db = initializeDatabase();

  models.register(app);
  services.register(app);

  app.listen(3000, () => console.log('Listening on port 3000'));
}

main();
