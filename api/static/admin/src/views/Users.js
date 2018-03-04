import React from 'react';
import { Link } from 'react-router-dom';

import Table, { IconColumn } from 'react-css-grid-table';

export default function(props) {
  const headers = [
    {
      value: 'check',
      width: '0.3fr',
    },
    {
      label: 'User',
      value: 'user',
      width: '2fr',
    },
    {
      label: '# Published',
      value: 'numberPublished',
      width: '1fr'
    },
    {
      label: 'Email',
      value: 'email',
      width: '2fr'
    },
    {
      label: 'Permissions',
      value: 'permissions',
      width: '1fr'
    },
    {
      label: 'Actions',
      value: 'actions',
      width: '0.7fr'
    }
  ];

  const data = [
    {
      id: 1,
      user: 'Rebecca Park',
      numberPublished: 42,
      email: 'burugirl93@gmail.com',
      permissions: 'Admin, Writer',
      actions: ['Edit', 'More']
    },
    {
      id: 2,
      user: 'Effie Eaton',
      numberPublished: 3,
      email: 'effie@gmail.com',
      permissions: 'Writer',
      actions: ['Edit', 'More'],
    }
  ];

  const customColumns = {
    check: {
      format: (data) => <IconColumn icon="icon ion-md-checkmark" data={data} />,
      className: 'justify-content-center'
    },
    user: {
      format: (data) => <Link to="/users:id" data={data} />,
      className: 'Table__user'
    },
    actions: {
      format: (multipleData) => multipleData.map(
	data => <span className="Table__action pr-2">{data}</span>)
    }
  }

  return (
    <div className="Users">
      <h1>Users</h1>
      <Table
	headers={headers}
	data={data}
	customColumns={customColumns}
      />
    </div>
  )
}
