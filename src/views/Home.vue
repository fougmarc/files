<template>
    <div>
      <div class="container">
      <div class="py-5 text-center">
        <h2>Send Files</h2>
      </div>

      <div id="big" class="row">
    
        <div class="col-md order-md-1">
         
          <form @submit.prevent="Add">

            

            
            <div class="mb-3">
              <label for="address2">fichier <span> *</span></label>
              <input  class="form-control" v-on:change="FileUpload()" ref="file" id="file"  type="file">
            </div>
           

            
            <hr class="mb-4">
            <button class="btn btn-primary btn-lg btn-block" type="submit">Envoyer</button>
          </form>
         
        </div>
      </div>

      
    </div>
     
    </div>
</template>

<script>


import {Conn} from '../Repository';
require('./bootstrap.min.css');



export default {
  name: 'App',
  data() {
    return {
      file:''
    }
    },
  
  
  methods: {
    FileUpload(){
      this.file = this.$refs.file.files[0];
    },
   
     Add(){   
        let formData = new FormData();
      
        formData.append('file', this.file);    
         Conn.post('apifile/', FormData);
    },
  }
}
</script>

<style>

    .container {
        margin-bottom: 30px;
        text-align: left;
  max-width: 960px;
}

.border-top { border-top: 1px solid #e5e5e5; }
.border-bottom { border-bottom: 1px solid #e5e5e5; }
.border-top-gray { border-top-color: #adb5bd; }

.box-shadow { box-shadow: 0 .25rem .75rem rgba(0, 0, 0, .05); }

.lh-condensed { line-height: 1.25; }



</style>