<template>
  <div>
    <h1>Home Router Test Lab</h1>
    <p>API Base URL: {{ API_BASE_URL }}</p>
    <TelnetScan />
  </div>
</template>

<script setup lang="ts">
import TelnetScan from './components/TelnetScan.vue';
import { API_BASE_URL } from './config';
</script>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
