<template>
  <v-card outlined tile>
    <v-card-title>{{ note.title }}</v-card-title>
    <v-card-text>{{ note.content }}</v-card-text>

    <v-card-actions>
      <v-spacer />
      <v-btn text @click="deleteNote">Delete</v-btn>
      <v-btn text @click="selectNote">Open</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  props: {
    note: {
      type: Object,
      required: true,
    },
  },
  emits: ["selected", "delete"],
  methods: {
    selectNote() {
      this.$emit("selected");
    },
    deleteNote() {
      this.$emit("delete");
    },
  },
};
</script>
