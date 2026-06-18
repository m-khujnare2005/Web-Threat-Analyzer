const form = document.getElementById("scanForm");
const result = document.getElementById("result");

form.addEventListener("submit", async (e) => {

    e.preventDefault();

    const url = document.getElementById("urlInput").value;

    try {

        const response = await fetch(
            "http://127.0.0.1:5000/scan",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    url: url
                })
            }
        );

        const data = await response.json();

        console.log(data);

        if (data.success) {

            result.innerHTML = `

            <div class="result-card">

                <h2>Web Threat Analysis Report</h2>

            <hr>

            <p>
                <strong>Website:</strong>
                ${data.url}
            </p>

            <p>
                <strong>SSL Status:</strong>
                ${data.ssl.status}
            </p>

            <p>
                <strong>Certificate Issuer:</strong>
                ${data.ssl.issuer}
            </p>

            <hr>

            <h3>Security Headers</h3>

            <p>
                <strong>Content-Security-Policy:</strong>
                ${data.headers["Content-Security-Policy"]}
            </p>

            <p>
                <strong>Strict-Transport-Security:</strong>
                ${data.headers["Strict-Transport-Security"]}
            </p>

            <p>
                <strong>X-Frame-Options:</strong>
                ${data.headers["X-Frame-Options"]}
            </p>

            <p>
                <strong>X-Content-Type-Options:</strong>
                ${data.headers["X-Content-Type-Options"]}
            </p>

            <hr>

            <p style="color:green;">
                Scan Completed Successfully
            </p>
            <hr>

            <h3>Domain Information</h3>

            <p>
                <strong>Domain:</strong>
                ${data.whois.domain_name}
            </p>

            <p>
                <strong>Registrar:</strong>
                ${data.whois.registrar}
            </p>

            <p>
                <strong>Creation Date:</strong>
                ${data.whois.creation_date}
            </p>

            <p>
                <strong>Expiration Date:</strong>
                ${data.whois.expiration_date}
            </p>
            <hr>

            <h3>Threat Assessment</h3>

            <p>
                <strong>Threat Score:</strong>
                ${data.risk ? data.risk.score : "N/A"}/100
            </p>

            <p>
                <strong>Risk Level:</strong>
                ${data.risk ? data.risk.risk_level: "N/A"}
            </p>

        </div>
        `;
    }

    } catch (error) {

        console.error(error);

        result.innerHTML = `
            <h3>${data.message}</h3>

        <p>
            <strong>URL:</strong>
            ${data.url}
        </p>

        <p>
            <strong>SSL Status:</strong>
            ${data.ssl.status}
        </p>

        <p>
            <strong>Issuer:</strong>
            ${data.ssl.issuer || "Unknown"}
        </p>
    `;
    }
});