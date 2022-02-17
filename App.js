import './App.css';
import Header from "./Header";
import {
    LineChart,
    ResponsiveContainer,
    Legend, Tooltip,
    Line,
    XAxis,
    YAxis,
    CartesianGrid
} from 'recharts';
  
// Sample chart data
const pdata = [
    {
        name: 'Mahindra Group',
        market_share: 38.83,
        domestic_sale: 3.43833
    },
    {
        name: 'Tafe Group',
        market_share: 18.43,
        domestic_sale: 1.65832
    },
    {
        name: 'Sonalika',
        market_share: 13.06,
        domestic_sale: 1.17503
    },
    {
        name: 'Escorts',
        market_share: 11.32,
        domestic_sale: 1.01849
    },
    {
        name: 'John Deere',
        market_share: 9.52,
        domestic_sale: 0.83610
    },
    {
        name: 'New Holland',
        market_share: 3.98,
        domestic_sale: 0.35828
    },
];
  
function App() {
    return (
      
        <>
           <Header/>
            <h1 className="text-heading">
                Line Chart Using Rechart
            </h1>
            <ResponsiveContainer width="100%" aspect={5}>
                <LineChart data={pdata} margin={{ right: 100 }}>
                    <CartesianGrid />
                    <XAxis dataKey="name" 
                        interval={'preserveStartEnd'} />
                    <YAxis></YAxis>
                    <Legend />
                    <Tooltip />
                    <Line dataKey="market_share"
                        stroke="blue" activeDot={{ r: 8 }} />
                    <Line dataKey="domestic_sale"
                        stroke="green" activeDot={{ r: 8 }} />
                </LineChart>
            </ResponsiveContainer>
        </>
    );
}
  
export default App;
