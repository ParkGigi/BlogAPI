module.exports.register = function (db, datatypes) {
  db.define('post', {
    id: {
      type: datatypes.INTEGER,
      autoIncrement: true,
      primaryKey: true,
      allowNull: false,
    },
    title: {
      type: datatypes.BLOB,
    },
    content: {
      type: datatypes.BLOB,
    },
  });
};
