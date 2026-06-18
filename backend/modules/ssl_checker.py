import ssl
import socket
from urllib.parse import urlparse

def check_ssl(url):

    try:

        hostname = urlparse(url).netloc

        context = ssl.create_default_context()

        with socket.create_connection((hostname, 443), timeout=5) as sock:

            with context.wrap_socket(
                sock,
                server_hostname=hostname
            ) as secure_sock:

                cert = secure_sock.getpeercert()

                return {
                    "status": "Valid",
                    "issuer": str(cert.get("issuer"))
                }

    except Exception as e:

        return {
            "status": "Invalid",
            "error": str(e)
        }