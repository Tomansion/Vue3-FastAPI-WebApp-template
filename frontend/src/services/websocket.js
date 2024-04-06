const protocol = window.location.protocol === "https:" ? "wss:" : "ws:";
const host = window.location.host;
const wsUrl = `${protocol}//${host}/ws`;

class WebSocketService {
  constructor() {
    this.socket = new WebSocket(wsUrl);
    this.callbacks = [];
  }

  onMessage(message, callback) {
    this.callbacks.push({ message, callback });

    this.socket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      const keys = Object.keys(data);

      for (const key of keys) {
        const callbacks = this.callbacks.filter((cb) => cb.message === key);
        callbacks.forEach((cb) => cb.callback(data[key]));
      }
    };
  }

  offMessage(message) {
    this.callbacks = this.callbacks.filter((cb) => cb.message !== message);
  }

  close() {
    if (this.socket) this.socket.close();
  }
}

const webSocketService = new WebSocketService();

export { webSocketService };
