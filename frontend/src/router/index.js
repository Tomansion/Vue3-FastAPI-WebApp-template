/**
 * router/index.ts
 *
 * Automatic routes for `./src/pages/*.vue`
 * Doc ? https://github.com/hannoeru/vite-plugin-pages
 */

// Composable
import { createRouter, createWebHistory } from "vue-router/auto";

const router = createRouter({
  history: createWebHistory(),
});

// Logs created routes
// console.log(router.getRoutes());

export default router;
