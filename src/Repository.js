import axios from 'axios';
//connexion à l'api
export const Conn = axios.create({
  baseURL: `http://127.0.0.1:8000/`,
  headers: {
    'Accept': 'application/json',
     'Content-Type': 'application/json' 
  }
})