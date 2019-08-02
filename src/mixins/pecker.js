export default {
  methods: {
    startPeckerTask(logId) {
      this.axios.post('/pecker/', {
        log_id: logId
      })
      .then(response => {
        console.log(response.data)
        this.retrieveTaskStatus(response.data.task_id)
      })
      .catch(error => {
        console.log(error)
      });
    },

    getTaskStatusPromise(task_id) {
      return this.axios.get('/pecker/' +  task_id)
    },

    retrieveTaskStatus(task_id) {
    },

  }
}
