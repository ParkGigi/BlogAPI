class Posts extends React.Component {
  render() {
    
    return(
      <div>
        <h2>Posts</h2>
        <div></div>
        <div className="Table">
          <div className="d-flex flex-row">
            <div className="col">Select</div>
            <div className="col">Title</div>
            <div className="col">Published Date</div>
            <div className="col">Published By</div>
          </div>
          <div className="d-flex flex-row">
            <div className="col"><input type="checkbox"/></div>
            <div className="col">Welcome to my blog!</div>
            <div className="col">Feb.29, 2017</div>
            <div className="col">burugirl93</div>
          </div>
        </div>
      </div>
    )
  }
}

class Admin extends React.Component {
  render() {
    return (
      <div>
        <h1>Admin</h1>
        <Posts/>
      </div>
    )
  }
};

ReactDOM.render(
  <Admin/>,
  document.getElementById('root')
);
