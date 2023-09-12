
const API_URL = 'http://127.0.0.1:5000';

export const getTickets = async () => {
  //const response = await axios.get(`${API_URL}/tickets`);
  //return response.data;
  const response = await fetch(`${API_URL}/tickets`).catch((error) => console.log(error));
  return await response.json();
};

