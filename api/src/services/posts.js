module.exports.register = function (app) {
  app.get('/posts', async function (req, res) {
    const posts = await app.db.Post.findAll();
    res.send(JSON.stringify(posts));
  });

  app.get('/post/:id', async function(req, res) {
    try {
      const post = await app.db.Post.getById(req.params.id);
    } catch (e) {
      res.status(404);
    }
  });
};
