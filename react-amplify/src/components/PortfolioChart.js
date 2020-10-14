import * as React from 'react';
import { PieChart } from 'react-minimal-pie-chart';

const colors = ["#0074D9", "#FF4136", "#2ECC40", "#FF851B", "#7FDBFF", "#B10DC9", "#FFDC00", "#001f3f", "#39CCCC", "#01FF70", "#85144b", "#F012BE", "#3D9970", "#111111", "#AAAAAA"];

function PortfolioChart(props) {

    function generateUserProfile() {
        console.log(props);
        const result = [];
        for (const r in props.userProfile) {
            const up = props.userProfile[r];
            result.push({
                title: up.ticker,
                value: parseInt(up.weight, 10),
                color: colors[r]
            });
        }
        console.log(result);
        return result;
    }
    return (

        <div style={{ height: '650px', width: '100%' }}>
            <PieChart
                data={generateUserProfile()}
                label={({ dataEntry }) => dataEntry.title + ' ' + dataEntry.value + '%'}
                labelStyle={(index) => ({
                    fill: colors[index],
                    fontSize: '2px',
                    fontFamily: 'sans-serif',
                })}
                radius={42}
                labelPosition={112}
                lineWidth={15} rounded
            />
        </div>
    );
}

export default PortfolioChart;