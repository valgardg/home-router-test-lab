from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import subprocess
import re
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your frontend's URL for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

class IPAddress(BaseModel):
    ip: str

# Define a Pydantic model to represent the scan result
class ScanResult(BaseModel):
    ip: str
    host_status: str
    ports: list

class PortDetail(BaseModel):
    port: int
    state: str
    service: str

@app.post("/telnet-scan/{ip_address}")
async def telnet_scan(ip_address: str):
    try:
        result = subprocess.run(
            ["nmap", "-p", "23", "--open", ip_address],
            capture_output=True, 
            text=True
        )

        # Parse the Nmap output to extract relevant information
        output = result.stdout
        print(output)
        
        # Extract host status (whether the host is up or down)
        host_status_match = re.search(r"Host (is (up|down)|seems down)", output)
        host_status = host_status_match.group(0) if host_status_match else "unknown"
        
        # Extract the port status and service information
        port_details = []
        port_lines = re.findall(r"(\d+/tcp)\s+(\w+)\s+(\w+)", output)
        for port_line in port_lines:
            port_number = int(port_line[0].split("/")[0])
            state = port_line[1]
            service = port_line[2]
            port_details.append(PortDetail(port=port_number, state=state, service=service))

        # Return the result in a structured format
        return ScanResult(
            ip=ip_address, 
            host_status=host_status, 
            ports=port_details
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))