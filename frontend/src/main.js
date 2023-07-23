//importar boostrap para que pueda verse en el codigo
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap';

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

createApp(App).use(router).mount('#app')
