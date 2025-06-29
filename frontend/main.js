function loadDevices() {
  fetch('http://127.0.0.1:5000/api/status')
    .then(res => res.json())
    .then(data => {
      const container = document.getElementById("devices");
      container.innerHTML = "";
      data.forEach(dev => {
        const statusClass = dev.status ? 'online' : 'offline';
        container.innerHTML += `
          <div class="col-md-4">
            <div class="card ${statusClass}">
              <div class="card-body">
                <h5 class="card-title">${dev.name}</h5>
                <p class="card-text">IP: ${dev.ip}</p>
                <p class="card-text fw-bold text-${dev.status ? 'success' : 'danger'}">
                  ${dev.status ? 'Online' : 'Offline'}
                </p>
                <p class="card-text">Latency: ${dev.latency !== null ? dev.latency + ' ms' : 'N/A'}</p>
                <p class="card-text">Last Seen: ${dev.last_seen}</p>
              </div>
            </div>
          </div>
        `;
      });
    });
}

document.getElementById('device-form').addEventListener('submit', function(e) {
  e.preventDefault();
  const name = document.getElementById('name').value;
  const ip = document.getElementById('ip').value;
  fetch('http://127.0.0.1:5000/api/add-device', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ name, ip })
  })
  .then(res => res.json())
  .then(data => {
    alert(data.message);
    setTimeout(loadDevices, 500);  // Slight delay for smoother update
    document.getElementById('device-form').reset();
  });
});

// Load devices on page load
loadDevices();
