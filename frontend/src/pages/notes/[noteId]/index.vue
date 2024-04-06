<template>
  <v-container style="max-width: 1000px">
    <!-- Back to home -->
    <previous-page-btn @back="backToHome" />

    <!-- Note info -->
    <v-slide-y-transition>
      <v-card :loading="loading">
        <!-- Note title -->
        <v-card-title
          style="display: flex"
          class="text-wrap"
          v-if="title !== null"
        >
          {{ title }}
        </v-card-title>
        <v-skeleton-loader type="heading" width="300px" height="40px" v-else />

        <!-- Note subtitle -->
        <v-card-subtitle style="display: flex" class="text-wrap" v-if="id">
          {{ id }}
        </v-card-subtitle>
        <v-skeleton-loader type="subtitle" width="200px" height="40px" v-else />

        <!-- Note content -->
        <v-card-text style="text-align: justify" v-if="content !== null">
          {{ content }}
        </v-card-text>
        <v-skeleton-loader type="paragraph" height="40px" v-else />

        <!-- Action buttons -->
        <v-card-actions>
          <v-spacer />
          <v-btn text @click="deleteNote">Delete the note</v-btn>
        </v-card-actions>
      </v-card>
    </v-slide-y-transition>
  </v-container>
</template>

<script>
import axios from "axios";
import messagesStore from "@/store/messages";
import { mapStores } from "pinia";

const websocketDeletionUpdateEvent = "noteDeletionUpdate";

export default {
  name: "NotePage",
  data() {
    return {
      loading: true,

      id: null,
      title: null,
      content: null,
    };
  },
  mounted() {
    // Get the note id from the route
    this.noteId = this.$route.params.noteId;

    if (!this.noteId) {
      console.log("No note given in route");
      this.$router.push({ path: `/` });
      return;
    }

    // Get the note from the server
    this.getNote();

    // Listen for websocket updates
    this.$websocket.onMessage(websocketDeletionUpdateEvent, (noteId) => {
      // Check if the update is for this note and redirect to home if it is
      if (noteId === this.id) {
        // Warn the user
        this.messagesStore.addMessage({
          type: "info",
          message: "The note has been deleted",
        });
        this.$router.push({ path: `/` });
      }
    });
  },
  methods: {
    getNote() {
      const url = "/api/notes/" + this.noteId;

      axios
        .get(url)
        .then((response) => {
          // Simulate loading time
          setTimeout(() => {
            this.loading = false;
            this.id = response.data.id;
            this.title = response.data.title;
            this.content = response.data.content;
          }, 500);
        })
        .catch((error) => {
          if (error.response?.status === 404) {
            console.log("Note not found");
            this.$router.push({ path: `/` });
            return;
          } else {
            console.log("Error loading note");
            console.log(error);
          }
        });
    },
    backToHome() {
      this.$router.push({
        path: "/",
      });
    },
    updateNote(update) {
      // Update the data
      if (update.title) this.title = update.title;
      if (update.synopsis) this.synopsis = update.synopsis;
      if (update.event) this.event = update.event;
      if (update.characters) this.characters = update.characters;
      if (update.completed) this.completed = update.completed;
      if (update.estimatedPrice) this.estimatedPrice = update.estimatedPrice;
      if (update.error) this.errorMessage = update.errorDetails;
    },
    deleteNote() {
      const url = "/api/notes/" + this.noteId;

      axios
        .delete(url)
        .then(() => {
          this.$router.push({ path: `/` });
        })
        .catch((error) => {
          console.log("Error deleting note");
          console.log(error);
        });
    },
  },
  computed: {
    ...mapStores(messagesStore),
  },
  beforeUnmount() {
    this.$websocket.offMessage(websocketDeletionUpdateEvent);
  },
};
</script>
