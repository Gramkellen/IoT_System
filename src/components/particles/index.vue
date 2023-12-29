<template>
    <div class="particles-js-box">
      <div id="particles-js"></div>
    </div>
  </template>
  <script>
  /* eslint-disable */
  import particlesJs from "./particles.js";
  import particlesConfig from "./particles.json";
  export default {
    data() {
      return {};
    },
    mounted() {
      this.init();
    },
    methods: {
      init() {
        particlesJS("particles-js", particlesConfig);
        document.body.style.overflow = "hidden";
      },
    },
  };
  </script>
  <style scoped>
  .particles-js-box {
    position: fixed;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    z-index: 1;
  }
  #particles-js {
    background: linear-gradient(270deg, #28006A 16.67%, #4878B0 48.48%, #395381 75%, #33446F 85.42%, #545C64 100%);
    /* background-color: #6b8ebb; */
    width: 100%;
    height: 100%;
  }
  </style>