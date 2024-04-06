<template>
  <div>
    <!-- List all messages -->
    <v-snackbar
      :style="{
        'margin-bottom': calcMargin(i),
      }"
      class="cursor-pointer"
      v-for="(s, i) in messages.slice(0, 10)"
      :key="i"
      v-model="show"
      timeout="-1"
      :color="s.type"
      @click="closeMessage(s.id)"
      :offset="100"
    >
      <!-- Message content -->
      <div style="display: flex; align-items: center; gap: 10px">
        <!-- Message Icons -->
        <v-icon v-if="s.type === 'info'">mdi-information</v-icon>
        <v-icon v-if="s.type === 'success'">mdi-check</v-icon>
        <v-icon v-if="s.type === 'warning'">mdi-alert</v-icon>
        <v-icon v-if="s.type === 'error'">mdi-alert-circle</v-icon>

        <!-- Message Text -->
        <div
          style="
            white-space: nowrap;
            max-width: 500px;
            overflow: hidden;
            text-overflow: ellipsis;
          "
        >
          {{ s.text }}
        </div>
      </div>

      <!-- Actions -->
      <template v-slot:actions>
        <v-btn> Close </v-btn>
      </template>
    </v-snackbar>
  </div>
</template>

<script>
import messagesStore from "@/store/messages";
import { mapStores } from "pinia";

export default {
  name: "AppMessenger",
  data: () => {
    return {
      show: true,
    };
  },
  methods: {
    closeMessage: function (id) {
      this.messagesStore.removeMessage(id);
    },
    calcMargin(i) {
      return 10 + i * 55 + "px";
    },
  },
  computed: {
    messages() {
      // console.log(this);
      console.log(this.messagesStore.messages);
      return this.messagesStore.messages;
    },

    // Import the messages store
    ...mapStores(messagesStore),
  },
};
</script>