import { defineStore } from "pinia";
import { v4 } from "uuid";

const store = defineStore("messages", {
  state: () => {
    return {
      messages: [],
    };
  },
  actions: {
    addMessage({ type, text }) {
      // Generate a new message id and add it to the messages array
      const newMessageId = v4();
      this.messages.push({
        id: newMessageId,
        text,
        type,
      });

      // Remove the message after 5 seconds
      setTimeout(() => {
        this.removeMessage(newMessageId);
      }, 5000);
    },
    removeMessage(id) {
      this.messages = this.messages.filter((message) => message.id !== id);
    },
  },
});

export default store;
