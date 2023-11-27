function generateUniqueId(): number {
  return new Date().getTime(); // Returns the current timestamp in milliseconds
}
function handleChange(checkbox: HTMLInputElement):boolean {
  if (checkbox.checked){
    return true
  }
  else{
    return false
  }

}

onload = () => {
  (document.getElementById('create') as HTMLButtonElement).addEventListener('click', evento => {evento.preventDefault();

    const input1 = ((document.getElementById('nome'))as HTMLInputElement).value;
    const input2 = ((document.getElementById('administrator'))as HTMLInputElement);
    const input3 = ((document.getElementById('age'))as HTMLInputElement).value;
    const input4 = ((document.getElementById('password'))as HTMLInputElement).value;
    const input5 = ((document.getElementById('civil_state'))as HTMLInputElement).value;
    const generatedId: number = generateUniqueId();
    var adm_bool: boolean = handleChange(input2);
    var age_var: number = Number(input3);
    const requestData = {
      "id": generatedId,
      "name": input1,
      "administrator": adm_bool,
      "age": age_var,
      "password": input4,
      "civil_state": input5,
      "games": ["example"]
    };
    console.log(requestData)
    fetch('http://127.0.0.1:8000/user/' + generatedId, {
      method: 'POST',
      body: JSON.stringify(requestData),
      headers: { 'Content-Type': 'application/json' }
    })
      .then(response => {
        if (response.ok) {
          (document.getElementById('mensagem') as HTMLDivElement).innerHTML = 'Dados inseridos com sucesso';
        } else {
          (document.getElementById('mensagem') as HTMLDivElement).innerHTML = 'Dados inseridos com erro';
        }
      })
      .catch(error => {
        console.log(error);
      });
  });
};
