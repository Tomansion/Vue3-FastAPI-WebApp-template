import { defineStore } from "pinia";

export const useAppStore = defineStore("app", {
  state: () => ({
    session: null,
  }),
  actions: {
    setSession(data) {
      this.session = data;
    },
  },
});
