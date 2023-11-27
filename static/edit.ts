function handleChange(checkbox: HTMLInputElement):boolean {
  if (checkbox.checked){
    return true
  }
  else{
    return false
  }

}
onload = () => {
    (document.getElementById('edit') as HTMLButtonElement).addEventListener('click', evento => {evento.preventDefault();

    const input1 = ((document.getElementById('nome'))as HTMLInputElement).value;
    const input2 = ((document.getElementById('administrator'))as HTMLInputElement);
    const input3 = ((document.getElementById('age'))as HTMLInputElement).value;
    const input4 = ((document.getElementById('password'))as HTMLInputElement).value;
    const input5 = ((document.getElementById('civil_state'))as HTMLInputElement).value;

    var adm_bool: boolean = handleChange(input2);
    var age_var: number = Number(input3);
    const requestData = {
      "id": id_number,
      "name": input1,
      "administrator": adm_bool,
      "age": age_var,
      "password": input4,
      "civil_state": input5,
      "games": ["example"]
    };
    console.log(requestData)
    fetch('http://127.0.0.1:8000/edit/' + id_number, {
      method: 'PUT',
      body: JSON.stringify(requestData),
      headers: { 'Content-Type': 'application/json' }
    })
      .then(response => {
        if (response.ok) {
          return response.json()
        }
      })
      .then(data => {
          console.log(data);
          localStorage.setItem('ID_USER', data[0]);
          localStorage.setItem('USERNAME', data[1]);
          localStorage.setItem('AGE_DATA', data[2]);
          localStorage.setItem('PASSWORD_USER', data[3]);
      })

  });
  const input1 = localStorage.getItem('USERNAME');
  const input2 = localStorage.getItem('AGE_DATA');
  const elemen1 = ((document.getElementById('nome'))as HTMLInputElement)
  const elemen2 = ((document.getElementById('age'))as HTMLInputElement);

  const id_number = localStorage.getItem('ID_USER');
  if (elemen1) {
      elemen1.value = input1 || '';
  }

  if (elemen2) {
      elemen2.value = input2 || '';
  }
};
