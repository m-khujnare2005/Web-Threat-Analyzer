import whois

def get_whois_info(url):

    try:

        domain = (
            url.replace("https://", "")
               .replace("http://", "")
               .split("/")[0]
        )

        w = whois.whois(domain)

        return {
            "domain_name": str(w.domain_name),
            "registrar": str(w.registrar),
            "creation_date": str(w.creation_date),
            "expiration_date": str(w.expiration_date)
        }

    except Exception as e:

        return {
            "error": str(e)
        }