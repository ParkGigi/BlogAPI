const posts = require('./posts');

module.exports.register = function (app) {
  posts.register(app);
};
