"""Application to log/report the modem dignostics value of the router
"""

from csclient import EventingCSClient
import datetime

diagnostics_path = "status/wan/devices/mdm-182e2f42/diagnostics"

"""Get timestamp, lat, long, accuracy..."""
def get_diagnostics():
    try:
        
       cp.log('Getting Diagnostics...')
       time = datetime.datetime.now().isoformat()
       SINR = cp.get(f'{diagnostics_path}/SINR')
       SINR_5G = cp.get(f'{diagnostics_path}/SINR_5G')
       ULFRQ = cp.get(f'{diagnostics_path}/ULFRQ')
       DLFRQ = cp.get(f'{diagnostics_path}/DLFRQ')
       ULFRQ_5G = cp.get(f'{diagnostics_path}/ULFRQ_5G')
       DLFRQ_5G = cp.get(f'{diagnostics_path}/DLFRQ_5G')
       RSRQ = cp.get(f'{diagnostics_path}/RSRQ')
       RSRP = cp.get(f'{diagnostics_path}/RSRP')
       RFCHANNEL = cp.get(f'{diagnostics_path}/RFCHANNEL')
       DBM = cp.get(f'{diagnostics_path}/DBM')
       SS = cp.get(f'{diagnostics_path}/SS')
       NETWORK_SUBNET = cp.get(f'{diagnostics_path}/NETWORK_SUBNET')
       RSRQ_5G = cp.get(f'{diagnostics_path}/RSRQ_5G')
       RSRP_5G = cp.get(f'{diagnostics_path}/RSRP_5G')
       RFBANDWIDTH_5G = cp.get(f'{diagnostics_path}/RFBANDWIDTH_5G')
       TXCHANNEL = cp.get(f'{diagnostics_path}/TXCHANNEL')
       LTEBANDWIDTH = cp.get(f'{diagnostics_path}/LTEBANDWIDTH')
       
       metrics = {
            "Time": time,
            "SINR": SINR,
            "SINR_5G": SINR_5G,
            "RSRQ": RSRQ,
            "RSRP": RSRP,
            "DBM": DBM,
            "SS": SS,
            "NETWORK_SUBNET": NETWORK_SUBNET,
            "RSRQ_5G": RSRQ_5G,
            "RSRP_5G": RSRP_5G,
            "RFBANDWIDTH_5G": RFBANDWIDTH_5G,
            "ULFRQ": ULFRQ,
            "DLFRQ": DLFRQ,
            "RFCHANNEL": RFCHANNEL,
            "TXCHANNEL": TXCHANNEL,
            "LTEBANDWIDTH": LTEBANDWIDTH,
            "ULFRQ_5G": ULFRQ_5G,
            "DLFRQ_5G": DLFRQ_5G
            
       }
       return metrics
   
    except Exception as e:
        cp.logger.exception(e)
        
cp = EventingCSClient('modem_diagnostics')
cp.log('Starting...')

while True:
    
    Metrics = get_diagnostics()
    
    cp.log(f'SINR: {Metrics["SINR"]}')
    cp.log(f'SINR_5G: {Metrics["SINR_5G"]}')
    cp.log(f'RSRQ: {Metrics["RSRQ"]}')
    cp.log(f'RSRP: {Metrics["RSRP"]}')
    cp.log(f'DBM: {Metrics["DBM"]}')
    cp.log(f'SS: {Metrics["SS"]}')
    cp.log(f'NETWORK_SUBNET: {Metrics["NETWORK_SUBNET"]}')
    cp.log(f'RSRQ_5G: {Metrics["RSRQ_5G"]}')
    cp.log(f'RSRP_5G: {Metrics["RSRP_5G"]}')
    cp.log(f'RFBANDWIDTH_5G: {Metrics["RFBANDWIDTH_5G"]}')
    