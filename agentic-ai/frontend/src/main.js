import { createApp } from 'vue';
import App from './App.js';
import './styles/main.css';

const app = createApp(App);
app.mount('#app');


import React from 'react';
import { createRoot } from 'react-dom/client';
import App from './App';
import './styles/main.css';

const rootEl = document.getElementById('app');
const root = createRoot(rootEl);
root.render(<App />);