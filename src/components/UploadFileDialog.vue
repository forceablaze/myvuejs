<template>
  <v-dialog v-model="dialog" max-width="500">
    <v-card>
        <v-card-title>
          <span class="headline">CV Log Upload</span>
        </v-card-title>
				<v-flex xs12 class="text-xs-center text-sm-center text-md-center text-lg-center">
					<img :src="fileUrl" height="150" v-if="fileUrl"/>
					<v-text-field label="Select Log" @click='pickFile' v-model='fileName' prepend-icon='attach_file'></v-text-field>
					<input
						type="file"
						style="display: none"
						ref="file"
						accept=".log"
						@change="onFilePicked"
					>
				</v-flex>

       <v-card-actions>
        <v-spacer></v-spacer>
         <v-btn color="green darken-1" flat="flat" @click="upload()">
          Upload
        </v-btn>
        <v-btn color="green darken-1" flat="flat" @click="dialog = false">
          Cancel
        </v-btn>

      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>

export default {
  name: 'uploadfile-dialog',

  data () {
    return {
      dialog: false,
      file: undefined,
			fileName: '',
			fileUrl: '',
    }
  },
  methods: {
    open() {
			this.dialog = true
    },
    upload() {
      this.dialog = false
      this.$emit('uploading', this.fileName)

      let formData = new FormData()
      formData.append('file', this.file)
      formData.append('remark', 'uploadfile-dialog')

      console.log(this.axios)

      this.axios.post('/file/', formData, { headers: {'Content-Type': 'multipart/form-data' }})
        .then(response => {
          console.log(response.data)
          this.$emit('success', response.data)
        })
        .catch(error => {
          this.$emit('failed', error)
        });
    },
    pickFile() {
      this.$refs.file.click()
    },
    onFilePicked(e) {
      const files = e.target.files

      let uploadFile = (file) => {
        this.fileName = file.name
        console.log(this.fileName)

        const reader = new FileReader()
        reader.addEventListener('load', () => {
          this.fileURL = this.result
        })

        reader.readAsDataURL(file)
        this.file = file
      }

      if(files) {
        [].forEach.call(files, uploadFile)
      }
      else {
        this.fileName = ''
        this.fileUrl = ''
      }
    }
  }
}

</script>
