# trab2_inf1407

-REQUIREMENTS:
Tudo presente dentro do requirements.txt :)

FUNCIONA:
  -CRUD no front-end
  -CRUD no back-end
  -Consulta e documentação via swagger, foi utilizado drf-spectacular em conjunto ao Django REST-framework, para documentar as APIs]
  -Foi publicado em um provedor Web
  -Ao tentar criar um novo usuário, será necessário informar name/id de Games válidos, já que existe uma relação entre os modelos User e Game

NÃO FUNCIONA:
  -Foi solicitado "imagens", não tivemos certeza se quer dizer .png's ou apenas htmls
  - Não foi implementado o token de autorização, logo não há endpoint protegido
  -Vale a pena apontar que no POST do modelo 'User' o argumento "id_arg" da URL não será usado.
  -Por algum motivo, não foi possível criar um css para initial_user.html que funcionasse da maneira esperada
  -Ao hospedar o site e tentar deixar o frontend disponível, nos deparamos com o problema que o css não era carregado. o erro: Refused to apply style from 'https://jpraffo.pythonanywhere.com/base_style' because its MIME type ('text/html') is not a supported stylesheet MIME type, and strict MIME checking is enabled

Manual do usuário:

Acessar 'start_page.html' e decidir se irá para login ou cadastro, ao selecionar qualquer uma das opções será direcionado aos htmls necessários.
Não acessar initial_user.html ou edit.html sem passar pelo login.
Para acessar o swagger: https://jpraffo.pythonanywhere.com/api/swagger
