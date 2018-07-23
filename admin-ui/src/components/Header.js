import React from 'react';
import { Link } from 'react-router-dom'; 

import './Header.scss';

export default function (props) {
  return (
    <header className="Header">
      <div className="container">
	<div className="row align-center">
	  <Link className="Header__link col col-auto" to="/">Dashboard</Link>
	  <Link className="Header__link col col-auto" to="/posts">Posts</Link>
	  <Link className="Header__link col col-auto" to="/users">Users</Link>
	  <Link className="Header__link col col-auto" to="/settings">Settings</Link>
	  <div className="col">
	    <div className="Header__user row">
	      <div className="Header__blogName">
		Cakes by Rebecca
		<span className="icon ion-ios-arrow-down" />
	      </div>
	      <a className="Header__createPost" href="/">Create Post</a>
	      <div
		className="Header__profilePicture"
		style={{backgroundImage: 'url("/img/profile.jpg")'}}
	      />
	    </div>
	  </div>
	</div>
      </div>
    </header>
  );
}
