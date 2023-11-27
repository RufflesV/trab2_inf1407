onload = () => {
  (document.getElementById('login') as HTMLButtonElement).addEventListener('click', evento => {
      evento.preventDefault();

    const input1 = ((document.getElementById('username'))as HTMLInputElement).value;
    const input2 = ((document.getElementById('password'))as HTMLInputElement).value;
    const requestData = {
      "name": input1,
      "password": input2,
    };
    console.log(JSON.stringify(requestData))
    fetch('http://127.0.0.1:8000/login/', {
      method: 'POST',
      body: JSON.stringify(requestData),
      headers: { 'Content-Type': 'application/json' }
    })
        .then(response => {
            if (response.ok) {
                return response.json()
            }
        })
        .then(data => {
            localStorage.setItem('ID_USER', data[0]);
            localStorage.setItem('USERNAME', data[1]);
            localStorage.setItem('AGE_DATA', data[2]);
            localStorage.setItem('PASSWORD_USER', data[3]);

            const file_url = "http://127.0.0.1:8080/static/initial_user.html";
            window.open(file_url);

        });
  });
};