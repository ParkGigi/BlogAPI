const datatypes = require('sequelize');

const post = require('./post');

module.exports.register = function (app) {
  post.register(app.db, datatypes);
};
