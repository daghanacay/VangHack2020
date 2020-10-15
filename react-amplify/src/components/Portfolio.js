import * as React from 'react';
import profile from '../data/profile';
import efts from '../data/asx';
import closePrice from '../data/closePrice';
import Grid from '@material-ui/core/Grid';
import Card from '@material-ui/core/Card';
import CardHeader from '@material-ui/core/CardHeader';
import CardActions from '@material-ui/core/CardActions';

import PortfolioTable from './PortfolioTable';
import PortfolioChart from './PortfolioChart';
import Team from './Team';
import { Button, Link } from '@material-ui/core';

const currencyFormatter = new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
});
const percentageFormatter = new Intl.NumberFormat('en-US', {
    style: 'percent',
    minimumFractionDigits: 2,
    maximumFractionDigits: 2
});


function Porfolio(props) {
    function getUserProfile() {
        console.log(props);
        const userProfile = profile[props.username] || profile.other;
        return userProfile;
    }

    function generateUserPortfolio() {
        console.log(props);
        const result = [];
        console.log(closePrice['2020-10-12']);
        const userProfile = getUserProfile();
        for (const r in userProfile) {
            const up = userProfile[r];
            console.log(up.price);
            console.log(up.ticker);
            console.log(closePrice['2020-10-12'][up.ticker]);
            const purchasedPrice = up.quantity * up.price;
            const currentValue = up.quantity * (closePrice['2020-10-12'][up.ticker] || up.price);
            result.push({
                ...efts[up.ticker],
                ...up,
                purchasedPrice,
                currentValue,
                return: (currentValue - purchasedPrice) * 100 / purchasedPrice
            });
        }
        console.log(result);
        return result;

    }

    function getTotalValue() {
        var totPurchasedValue = 0, totCurrentValue = 0;
        const userProfile = generateUserPortfolio();
        for (var up in userProfile) {
            totPurchasedValue += userProfile[up].purchasedPrice;
            totCurrentValue += userProfile[up].currentValue;
        }

        return {
            totPurchasedValue,
            totCurrentValue,
            netGrowth: (totCurrentValue - totPurchasedValue) / totPurchasedValue / 100,
            cash: 10000 - totPurchasedValue
        }
    }
    return (

        <Grid container spacing={3}>
            <Grid item xs={12} sm={4} md={3}>

                <Card style={{ backgroundColor: '#bbcf9c' }}>
                    <CardHeader
                        title={currencyFormatter.format(Number(getTotalValue().totPurchasedValue))}
                        subheader="Total Investment"
                    />
                </Card>
            </Grid>
            <Grid item xs={12} sm={4} md={3}>

                <Card style={{ backgroundColor: '#f2f2f2' }}>
                    <CardHeader
                        title={currencyFormatter.format(Number(getTotalValue().totCurrentValue))}
                        subheader="Current Value"
                    />
                </Card>
            </Grid>
            <Grid item xs={12} sm={4} md={3}>


                <Link href="http://52.63.91.203:8080/comparison" target="_blank" color="primary" rel="noreferrer" underline='none' >
                    <Card style={{ backgroundColor: '#f6f8f1' }}>
                        <CardHeader
                            title={percentageFormatter.format(Number(getTotalValue().netGrowth))}
                            subheader="Return"
                        />
                    </Card>
                </Link>
            </Grid>
            <Grid item xs={12} sm={4} md={3}>

                <Card style={{ backgroundColor: 'rgba(227, 114, 34, 0.4)' }}>
                    <CardHeader
                        title={generateUserPortfolio().length}
                        subheader="Investments"
                    />
                </Card>
            </Grid>
            <Grid item xs={12} md={8}>
                <PortfolioTable userProfile={generateUserPortfolio()} ></PortfolioTable>
            </Grid>
            <Grid item xs={12} md={4}>
                <PortfolioChart userProfile={getUserProfile()} ></PortfolioChart>
            </Grid>
            <Grid item xs={12} md={6}>


                <Card>
                    <CardHeader
                        title="My teams"
                    />
                    <Button color='primary' variant="contained" style={{ float: "right", marginTop: "-3rem", marginRight: "1rem" }} >Join team</Button>
                    <Team></Team>
                </Card>
            </Grid>
            <Grid item xs={12} md={6}>
                <Grid container spacing={5}>
                    <Grid item xs={12} sm={6}>

                        <Card style={{ backgroundColor: 'rgba(227, 114, 34, 0.4)' }}>
                            <CardHeader
                                title={7}
                                subheader="Buddies"
                            />
                        </Card>
                    </Grid>
                    <Grid item xs={12} sm={6}>

                        <Card style={{ backgroundColor: '#f6f8f1' }}>
                            <CardHeader
                                title={'$4,500'}
                                subheader="Avg Investment"
                            />
                        </Card>
                    </Grid>
                    <Grid item xs={12} sm={6}>

                        <Link href="http://54.206.87.115:8080/leadership" target="_blank" color="primary" rel="noreferrer" underline='none' >
                            <Card style={{ backgroundColor: '#f2f2f2' }}>
                                <CardHeader
                                    title={'#275'}
                                    subheader="Overall rank"
                                />
                            </Card>
                        </Link>
                    </Grid>
                    <Grid item xs={12} sm={6}>

                        <Card style={{ backgroundColor: '#bbcf9c' }}>
                            <CardHeader
                                title={currencyFormatter.format(Number(getTotalValue().cash))}
                                subheader="Cash"
                            />
                        </Card>
                    </Grid>
                </Grid>

            </Grid>
        </Grid >)
}

export default Porfolio;