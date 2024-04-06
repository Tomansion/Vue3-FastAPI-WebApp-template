<!-- HomePage, Notes list -->
<template>
  <v-container style="max-width: 1000px">
    <!-- Add Note modal -->
    <v-btn
      prepend-icon="mdi-plus"
      color="primary"
      @click="addNoteModal = true"
      class="mb-4"
    >
      Add Note
    </v-btn>

    <!-- Notes display -->
    <v-fade-transition leave-absolute>
      <div
        v-if="!loading"
        style="display: flex; flex-direction: column; gap: 10px"
      >
        <v-fade-transition group leave-absolute>
          <NoteOverview
            v-for="note in notes"
            :key="note.id"
            :note="note"
            @selected="goToNote(note.id)"
            @delete="deleteNote(note.id)"
          />
        </v-fade-transition>
      </div>
    </v-fade-transition>

    <!-- Notes loading skeleton -->
    <v-fade-transition hide-on-leave>
      <div
        v-if="loading"
        style="display: flex; flex-direction: column; gap: 10px"
      >
        <NoteOverviewSkeleton v-for="i in 3" :key="i" />
      </div>
    </v-fade-transition>

    <!-- No notes message -->
    <v-fade-transition leave-absolute>
      <v-alert type="info" dense v-if="notes.length == 0 && !loading">
        No notes found. Click the "Add Note" button to create a new note.
      </v-alert>
    </v-fade-transition>

    <!-- Add Note modal -->
    <v-dialog v-model="addNoteModal" max-width="500px">
      <NoteCreationForm @noteAdded="noteAdded" @close="addNoteModal = false" />
    </v-dialog>
  </v-container>
</template>

<script>
import axios from "axios";

const noteCreationUpdateEventName = "noteCreationUpdate";
const noteDeletionUpdateEventName = "noteDeletionUpdate";

export default {
  name: "HomePage",
  data() {
    return {
      loading: true,
      addNoteModal: false,
      notes: [],

      newTaskTitle: "",
    };
  },
  mounted() {
    // Get the notes from the API
    this.getNotes();

    // Listen for websocket updates
    this.$websocket.onMessage(noteCreationUpdateEventName, (newNote) => {
      // Check if the note already exists
      const existingNote = this.notes.find((note) => note.id === newNote.id);
      if (existingNote) return; // The note already exists

      // Add the new note to the list
      this.notes.unshift(newNote);
    });
    this.$websocket.onMessage(noteDeletionUpdateEventName, (noteId) => {
      // Remove the note from the list
      this.notes = this.notes.filter((note) => note.id !== noteId);
    });
  },
  methods: {
    getNotes() {
      this.loading = true;
      axios
        .get("/api/notes")
        .then((response) => {
          this.notes = response.data;

          // Reverse the order of the notes to show the latest note first
          this.notes.reverse();

          setTimeout(() => {
            // Simulate loading time
            this.loading = false;
          }, 300);
        })
        .catch((error) => {
          console.error(error);
        });
    },
    goToNote(id) {
      this.$router.push({ path: `/notes/${id}` });
    },
    noteAdded(newNote) {
      // Check if the note already exists
      const existingNote = this.notes.find((note) => note.id === newNote.id);
      if (existingNote) return; // The note already exists

      // Add the new note to the start of the list
      this.notes.unshift(newNote);
    },
    deleteNote(id) {
      axios
        .delete(`/api/notes/${id}`)
        .then(() => {
          // Remove the note from the list
          this.notes = this.notes.filter((note) => note.id !== id);
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  beforeUnmount() {
    // Remove the all websocket listeners
    this.$websocket.offMessage(noteCreationUpdateEventName);
    this.$websocket.offMessage(noteDeletionUpdateEventName);
  },
};
</script>
