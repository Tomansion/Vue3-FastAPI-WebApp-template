<template>
  <v-app>
    <v-main>
      <!-- App bar, will be present on all pages -->
      <v-app-bar :elevation="2">
        <v-app-bar-title
          style="cursor: pointer"
          @click="() => $router.push('/')"
        >
          <v-icon>mdi-note</v-icon>
          Easy notes, a Web APP template
        </v-app-bar-title>
      </v-app-bar>

      <!-- App messenger -->
      <AppMessenger />

      <!-- The router view will be rendered here -->
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
export default {
  beforeUnmount() {
    this.$websocket.close();
  },
};
</script>
