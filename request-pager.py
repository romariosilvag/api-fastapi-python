import requests
from typing import Dict

def send_to_pagerduty(dedup_key: str, routing_key: str, summary: str, source: str, severity: str, event_action: str, alerta_dict: dict, client: str,client_url: str,component: str) -> bool:
    """
    Envía un evento a PagerDuty utilizando el routing key, el resumen, la fuente y la gravedad especificados.
    
    Args:
        routing_key (str): El routing key del servicio de PagerDuty al que se enviará el evento.
        summary (str): El resumen del evento.
        source (str): La fuente del evento.
        severity (str): La gravedad del evento.
    
    Returns:
        bool: True si la solicitud se envió correctamente, False si no.
    """
    
    # URL del endpoint de PagerDuty
    url = "https://events.pagerduty.com/v2/enqueue"
    
    # Crear el payload de la solicitud POST
    payload = {
        "dedup_key": dedup_key,
        "routing_key": routing_key,
        "event_action": event_action,
        "payload": {
            "summary": summary,
            "source": source,
            "severity": severity,
            "client": client,
            "client_url": client_url,
            "component": component,
            "custom_details": {
        
                "1.1 ID Alerta": alerta_dict["1.1 ID Alerta"], 
                "1.2 Estado": alerta_dict["1.2 Estado"],
                "1.3 Severidad": alerta_dict["1.3 Severidad"],
                "1.4 Dispositivo": alerta_dict["1.4 Dispositivo"],
                "1.5 Mensaje": alerta_dict["1.5 Mensaje"],
                "1.6 Descripcion": alerta_dict["1.6 Descripcion"], 
                "1.7 Escalamiento": alerta_dict["1.7 Escalamiento"],
                "1.8 Propiedades": alerta_dict["1.8 Propiedades"]
            }
        }
    }
    
    # Crear los encabezados de la solicitud POST
    headers = {
        "Content-Type": "application/json"
    }
    
    # Enviar la solicitud POST a PagerDuty
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error al enviar solicitud a PagerDuty: {e}")
        return False


dedup_key = "123"
routing_key = "f2ea8bc1ca934001c01a28b76f149ede"
summary = "test python 3"
source = "python"
severity = "critical"
event_action = "trigger"
client = "webhook-python"
client_url = "url-origen"
component = "nombre-componente"

alerta_dict = {
    "1.1 ID Alerta": "ID",
    "1.2 Estado": "State",
    "1.3 Severidad": "ProblemSeverity",
    "1.4 Dispositivo": "ImpactedEntityNames \nImpactedEntity",
    "1.5 Mensaje": "ProblemID - ProblemTitle",
    "1.6 Descripcion": "ProblemDetailsText", 
    "1.7 Escalamiento": "Tags",
    "1.8 Propiedades": "Impacto: ProblemImpact test rsg"
}


response = send_to_pagerduty(dedup_key,routing_key,summary,source,severity,event_action,alerta_dict,client,client_url,component)

print(response)