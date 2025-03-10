import { defineStore } from 'pinia';
import axios from 'axios';
import { API_BASE_URL } from '../config';

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
    isLoading: false,
  }),
  actions: {
    async scanIp(ipAddress: string) {
      try {
        this.isLoading = true;
        console.log('Scanning IP:', ipAddress);
        const response = await axios.post(`${API_BASE_URL}/telnet-scan/${ipAddress}`);
        console.log('Scan result:', response.data);
        this.scanResult = response.data as ScanResult;
      } catch (error) {
        console.error('Error scanning IP:', error);
      } finally {
        this.isLoading = false;
      }
    },
  },
});
