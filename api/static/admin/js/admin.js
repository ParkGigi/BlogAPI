function request(method, url, body, callback) {
  const request = new XMLHttpRequest();
  request.open(method, url, true);
  request.setRequestHeader('Content-Type', 'application/json');

  request.onreadystatechange = function () {
    const response = request.responseText;
    if (request.readyState === XMLHttpRequest.DONE && callback) {
      callback(response ? JSON.parse(response) : undefined);
    }
  };

  request.send(body ? JSON.stringify(body) : undefined);
}

class Table extends React.Component {
  renderHeaderColumn(column) {
    return (
      <div className="col" key={column}>
        <div className="Table-cell">{column}</div>
      </div>
    );
  }

  render() {
    return (
      <div className="Table">
        {!this.props.header ? null : (
          <div className="Table-header">
            <div className="row">
              {this.props.header.map(this.renderHeaderColumn)}
            </div>
          </div>
        )}
        {this.props.children}
      </div>
    )
  }
}

class TableRow extends React.Component {
  render() {
    return (
      <div className="Table-row">
        <div className="row">
          {this.props.children}
        </div>
      </div>
    );
  }
}

class TableCell extends React.Component {
  render() {
    const { size } = this.props;

    return (
      <div className={`col ${size ? `col-${size}` : ''}`}>
        <div className="Table-cell">
          {this.props.children}
        </div>
      </div>
    );
  }
}

class Posts extends React.Component {
  render() {
    const { posts } = this.props;
    const table_rows = [];

    for (let i=0; i < (posts || []).length; i++) {
      //table_rows == null ? table_rows = [] : null;
      table_rows.push(
        <TableRow>
          <TableCell><input type="checkbox"/></TableCell>
          <TableCell>{posts[i].title}</TableCell>
          <TableCell>{posts[i].created}</TableCell>
          <TableCell>{posts[i].author_id}</TableCell>
        </TableRow>
      );
    }
    
    return(
      <div>
        <h2>Posts</h2>
        <Table header={['Select', 'Title', 'Published Date', 'Published By']} >
            {table_rows}
        </Table>
      </div>
    )
  }
}

class Users extends React.Component {
  render() {
    const { users } = this.props
    const user_rows = [];

    for (let i=0; i < (users || []).length; i++ ) {
      console.log(users);
      user_rows.push(
        <TableRow>
          <TableCell><input type="checkbox" /></TableCell>
          <TableCell>{users[i].username}</TableCell>
          <TableCell>7</TableCell>
          <TableCell>{users[i].user_level}</TableCell>
        </TableRow>
      )
    }
    
    return(
      <div>
        <h2>Users</h2>
        <Table header={['Select', 'Username', '#Published', 'Permissino level']}>
          {user_rows}
        </Table>
      </div>
    )
  }
}

class Admin extends React.Component {
  constructor() {
    super();

    this.state = {
      posts : null,
    }
  }
  
  componentWillMount() {
    this.getPosts();
    this.getUsers();
  }

  getPosts() {
    request('GET', 'http://localhost:5000/posts', null, (response) => {
      this.setState({ posts: response });
    });
  }

  getUsers() {
    request('GET', 'http://localhost:5000/users', null, (response) => {
      this.setState({ users: response });
    });
  }

  render() {
    const { posts, users } = this.state;
    
    return (
      <div className="container">
        <h1>Admin</h1>
        <div className="row">
          <div className="col-lg-7">
            <Posts posts={posts}/>
          </div>
          <div className="col-lg-5">
            <Users users={users}/>
          </div>
        </div>
      </div>
    )
  }
};

ReactDOM.render(
  <Admin/>,
  document.getElementById('root')
);
