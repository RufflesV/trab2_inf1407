onload = () => {
    const id_number = localStorage.getItem('ID_USER');
    fetch('http://127.0.0.1:8000/user/' + id_number, {
      method: 'DELETE',
      headers: { 'Content-Type': 'application/json' }
    })
      .then(response => {
        if (response.ok) {
          return response.json()
        }
      })

  }