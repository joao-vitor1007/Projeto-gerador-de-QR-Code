# 🔳 Gerador de QR Code com Flask

Olá! Eu sou o João Vitor, e este é um projeto simples, porém bem estilizado, de **gerador de QR Code** feito com **Python (Flask)**. Nele, o usuário pode inserir um link e obter automaticamente a imagem de um QR Code correspondente.

Além da funcionalidade, me preocupei também com o visual da aplicação: usei **CSS personalizado**, **animações com JavaScript** e até **efeitos de partículas de fundo** para deixar tudo mais bonito e moderno.

---

## 🚀 Tecnologias Utilizadas

- **Python 3**
- **Flask** – Para o backend e renderização de páginas
- **qrcode** – Para gerar os códigos QR
- **HTML5 + CSS3** – Interface da aplicação
- **JavaScript** – Animações e interatividade
- **particles.js** – Efeito visual com partículas no fundo da página

---

## 💻 Como executar o projeto

### ✅ Pré-requisitos

- Python 3 instalado
- Pip (gerenciador de pacotes do Python)

### 🔧 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/qr-code-generator-flask.git
   cd qr-code-generator-flask


   Crie um ambiente virtual (opcional, mas recomendado):

bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
Instale as dependências:

bash
Copiar
Editar
pip install flask qrcode
Execute a aplicação:

bash
Copiar
Editar
python app.py
Acesse no navegador:

arduino
Copiar
Editar
http://localhost:5000
🖼️ Estrutura de Pastas
csharp
Copiar
Editar
qr-code-generator/
│
├── app.py               # Código principal em Flask
├── qrcodes/             # Pasta onde os QR Codes gerados são salvos
├── templates/
│   └── index.html       # Interface da aplicação
├── static/
│   └── style.css        # Estilos personalizados
├── README.md            # Este arquivo
🎨 Funcionalidades e Estilo
Entrada de link com botão customizado

Geração dinâmica de QR Code

Estilo com gradiente e sombras roxas/neon

Efeitos de transição ao carregar a página

Animação ao clicar no botão

Animação de entrada suave para o QR gerado

Partículas animadas no fundo (via particles.js)

📷 Preview



📦 To-Do (Melhorias futuras)
Adicionar histórico de QR Codes gerados

Permitir escolha do tipo de dado (texto, link, telefone etc.)

Download automático do QR

Deploy online com Render ou Vercel

📄 Licença
Este projeto é de uso livre para fins educacionais e demonstrações. Sinta-se à vontade para modificá-lo ou aprimorá-lo!

Se tiver dúvidas ou sugestões, entre em contato! 
