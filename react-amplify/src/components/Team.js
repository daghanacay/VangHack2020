import * as React from 'react';


import { DataGrid } from '@material-ui/data-grid';

const currencyFormatter = new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
});
const columns = [
    { field: 'name', headerName: 'Name', width: 300 },
    { field: 'players', headerName: 'Players' },
    {
        field: 'totalValue', headerName: 'Total Value',
        valueFormatter: ({ value }) => currencyFormatter.format(Number(value)), width: 150
    },
    { field: 'rank', headerName: 'Rank' }
];

const rows = [
    {
        id: '1',
        name: 'S.W.A.T Team',
        players: 11,
        totalValue: 97230,
        rank: 5
    },
    {
        id: '2',
        name: 'Let the dogs out',
        totalValue: 72230,
        players: 9,
        rank: 3
    },
    {
        id: '3',
        name: 'Covfefe',
        totalValue: 17230,
        players: 2,
        rank: 1
    },
    {
        id: '4',
        name: 'We\'re fake',
        totalValue: 127230,
        players: 15,
        rank: 8
    },
    {
        id: '5',
        name: 'Everything Burns!',
        totalValue: 1247230,
        players: 148,
        rank: 21
    }
]

function Team(props) {
    return (
        <div style={{ height: '450px', width: '100%' }}>
            <DataGrid rows={rows} columns={columns} pageSize={10} />
        </div>
    );
}

export default Team;