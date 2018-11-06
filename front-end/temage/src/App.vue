<template>
  <div id="app">
    <img src="./assets/logo.png">
    <router-view/>
    <new_compo></new_compo>
  </div>
</template>

<script>
import new_compo from './components/new_compo.vue'
export default {
  name: 'App',
  components:{
    new_compo
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
