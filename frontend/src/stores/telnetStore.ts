import { defineStore } from 'pinia';
import axios from 'axios';

interface ScanResult {
  ip: string;
  host_status: string;
  ports: Array<{
    port: number;
    state: string;
    service?: string;
  }>;
}

export const useTelnetStore = defineStore('telnet', {
  state: () => ({
    scanResult: null as ScanResult | null,
  }),
  actions: {
    async scanIp(ipAddress: string) {
      try {
        console.log('Scanning IP:', ipAddress);
        const response = await axios.post(`http://localhost:8000/telnet-scan/${ipAddress}`);
        console.log('Scan result:', response.data);
        this.scanResult = response.data as ScanResult;
      } catch (error) {
        console.error('Error scanning IP:', error);
      }
    },
  },
});
