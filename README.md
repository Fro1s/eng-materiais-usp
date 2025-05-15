Projeto Conheça os Materiais - Engenharia de Materiais
Este é um site educacional desenvolvido por alunos do curso de Engenharia de Materiais da EEL-USP como parte da disciplina de Python. O projeto apresenta diferentes materiais de engenharia, suas microestruturas, propriedades e aplicações de forma interativa e visualmente atraente.

Descrição
O site "Conheça os Materiais" permite aos usuários explorar cinco diferentes materiais de engenharia:

Concreto Refratário
Aço Inoxidável
Ferro Fundido
Aço Liga F22
Folha de Cana de Açúcar
Cada material possui uma página dedicada com informações detalhadas sobre suas características microestruturais, propriedades, aplicações e curiosidades.

Tecnologias Utilizadas
Backend: Python com framework Flask
Frontend: HTML, CSS, JavaScript
Design: Design responsivo para funcionar em dispositivos móveis e desktop
Estrutura do Projeto
projeto/
│
├── app.py                 # Aplicação Flask principal
├── static/                # Arquivos estáticos
│   ├── style.css          # Estilos CSS
│   └── img/               # Imagens dos materiais
│       ├── concreto.jpg
│       ├── aco_inox.jpg
│       ├── ferro_fundido.jpg
│       ├── ferro_f22.jpg
│       └── folha_cana.jpg
│
├── templates/             # Templates HTML
│   ├── index.html         # Página inicial
│   ├── about.html         # Página sobre o projeto
│   └── materiais/         # Páginas de cada material
│       ├── concreto.html
│       ├── aco_inox.html
│       ├── ferro_fundido.html
│       ├── ferro_f22.html
│       └── folha_cana.html
│
├── requirements.txt       # Dependências do projeto
└── README.md              # Este arquivo
Instalação e Execução
Clone o repositório:
git clone https://github.com/seu-usuario/conheca-os-materiais.git
cd conheca-os-materiais
Crie um ambiente virtual (opcional, mas recomendado):
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
Instale as dependências:
pip install -r requirements.txt
Execute a aplicação:
python app.py
Acesse o site no navegador:
http://127.0.0.1:5000
Equipe de Desenvolvimento
Este projeto foi desenvolvido pelos alunos:

Ana Lívia Sampaio
Francisco Rangel (Chico)
Ighor de Oliveira
Katharine Souza
Laís Monteiro (Polegada)
Henrique Holanda (Mike)
Victoria Santos
Orientação
Projeto desenvolvido sob a orientação do Professor Luiz Eleno, como parte da disciplina de Python do curso de Engenharia de Materiais da EEL-USP.

Licença
Este projeto é para fins educacionais e não possui uma licença específica. Todos os direitos pertencem aos desenvolvedores e à EEL-USP.

Agradecimentos
Agradecemos ao Professor Luiz Eleno pela orientação e oportunidade de desenvolver este projeto, que nos permitiu aplicar conhecimentos de programação em um contexto relevante para nossa área de estudo.

© 2025 Engenharia de Materiais - EEL-USP