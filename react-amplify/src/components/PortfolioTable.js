import * as React from 'react';

import { DataGrid } from '@material-ui/data-grid';

const currencyFormatter = new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
});

const columns = [
    { field: 'id', headerName: 'Ticker' },
    { field: 'name', headerName: 'Name', width: 300 },
    // { field: 'issuer', headerName: 'Issuer' },
    {
        field: 'mer', headerName: 'MER%',
        type: 'number',
    },
    {
        field: 'weight', headerName: 'Weight',
        type: 'number',
    },
    {
        field: 'return', headerName: 'Return%',
        type: 'number',
    },
    { field: 'quantity', headerName: 'Quantity' },
    {
        type: 'number',
        field: 'purchasedPrice', headerName: 'Purchased Market Value',
        valueFormatter: ({ value }) => currencyFormatter.format(Number(value)),
    },
    {
        type: 'number',
        field: 'currentValue', headerName: 'Current Market Value',
        valueFormatter: ({ value }) => currencyFormatter.format(Number(value)),
    }
];


function PorfolioTable(props) {

    function generateUserProfile() {

        return props.userProfile;
    }
    return (
        <div style={{ height: '650px', width: '100%' }}>
            <DataGrid rows={generateUserProfile()} columns={columns} pageSize={10} />
        </div>
    );
}

export default PorfolioTable;