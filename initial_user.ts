function checkOddOrEven(number: number): string {
  if (number % 2 === 0) {
    return 'Even';
  } else {
    return 'Odd';
  }
}


onload = () => {
  const input1 = localStorage.getItem('ID_USER');
  const input2 = localStorage.getItem('USERNAME');
  const input3 = localStorage.getItem('AGE_DATA');

  const name = (document.getElementById('username') as HTMLDivElement);
  name.innerHTML = "Name:" + input2 + "   Age:" + input3;

  const listContainer = document.getElementById('user_list');
  const listContainer2 = document.getElementById('all_games');
  const url: string = 'http://127.0.0.1:8000/user/list/' + input1;
  fetch(url, {
      method: 'GET',
      headers: { 'Content-Type': 'application/json' }
    })
        .then(response => {
            if (response.ok) {
                return response.json()

            }
        })
        .then(data => {
             for (let i = 0; i < data.length; i += 2) {
                 const listItem = document.createElement('li');
                 const listItem2 = document.createElement('li');
                 listItem.textContent = 'Jogo: ' + data[i];
                 listItem.setAttribute('id', 'blue');
                 listContainer.appendChild(listItem);
                 if (i + 1 < data.length) {
                     listItem2.textContent = 'Developer: ' + data[i + 1];
                     listItem2.setAttribute('id', 'blue');
                     listContainer.appendChild(listItem2);
                 }
                 const lineBreak = document.createElement('br');
                 listContainer.appendChild(lineBreak);
             }
             const url2: string = 'http://127.0.0.1:8000/list_games/' + input1;
             fetch(url2, {
                 method: 'GET',
                headers: { 'Content-Type': 'application/json' }
              })
                 .then(response => {
                    if (response.ok) {
                        return response.json()
                    }
                  })
                  .then(data2 => {
                    for (let i = 0; i < data2.length; i++) {
                        const listItem = document.createElement('li');
                        listItem.textContent = 'Jogo: ' + data2[i];
                        if (checkOddOrEven(i) === 'Odd') {
                            listItem.setAttribute('id', 'odd');
                        } else {
                            listItem.setAttribute('id', 'even');
                        }
                        listContainer2.appendChild(listItem);
                        const lineBreak = document.createElement('br');
                        listContainer2.appendChild(lineBreak);
                    }

                  })

        })



}