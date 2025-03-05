<template>
  <div>
    <h2>Telnet Scan</h2>
    <input type="text" v-model="ipAddress" placeholder="Enter IP address" />
    <button @click="scanIp">Scan</button>

    <!-- Display loading message or error if necessary -->
    <div v-if="telnetStore.isLoading">
      <p>Loading scan results...</p>
    </div>
    <!-- Display scan results once available -->
    <div v-if="telnetStore.scanResult !== null && !telnetStore.isLoading">
      <h3>Scan Results for {{ ipAddress }}</h3>
      <p><strong>Status:</strong> {{ telnetStore.scanResult.host_status }}</p>
      
      <h4>Open Ports:</h4>
      <ul>
        <li v-for="(port, index) in telnetStore.scanResult.ports" :key="index">
          <p><strong>Port:</strong> {{ port.port }}</p>
          <p><strong>State:</strong> {{ port.state }}</p>
          <p v-if="port.service"><strong>Service:</strong> {{ port.service }}</p>
        </li>
      </ul>
    </div>
  </div>
</template>


<script setup lang="ts">
import { ref } from 'vue';
import { useTelnetStore } from '../stores/telnetStore';

const ipAddress = ref('');
const telnetStore = useTelnetStore();

function scanIp() {
  telnetStore.scanIp(ipAddress.value);
}
</script>

<style scoped>
/* Add any styles you need here */
</style>