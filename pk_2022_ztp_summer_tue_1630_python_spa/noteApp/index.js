import {AppView} from "./app-view.js";
import {AppController} from "./app-controller.js";


axios.defaults.baseURL = 'http://localhost:5000';

const app = new AppController(new AppView());
