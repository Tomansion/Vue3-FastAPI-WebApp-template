/**
 * main.js
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Plugins
import { registerPlugins } from "@/plugins";

// Components
import App from "./App.vue";

// Composables
import { createApp } from "vue";

// Services
import { webSocketService } from "./services/websocket.js";

const app = createApp(App);

app.config.globalProperties.$websocket = webSocketService;

registerPlugins(app);

app.mount("#app");
