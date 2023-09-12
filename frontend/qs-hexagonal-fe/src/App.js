import { useEffect, useState } from 'react';
import { getTickets } from './api';

function App() {
  const [tickets, setTickets] = useState([]);

  useEffect(() => {
    const fetchTickets = async () => {
      const data = await getTickets();
      console.log(data);
      setTickets(JSON.parse(data.value));
    };
    fetchTickets();
  }, []);

  return (
    <div>
      <h1>Tickets</h1>
      <ul>
        {tickets && tickets.map((ticket) => (
          <li key={ticket.id}>
            [ {ticket.status} ] {ticket.priority} - {ticket.description}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;