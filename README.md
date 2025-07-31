# 🤖 Echo Bot README

Este é um bot simples, baseado no modelo de **Echo Bot** da Microsoft, que foi modificado para interagir com o usuário e coletar informações para a criação de um chamado de suporte.

---

## ✨ Funcionalidades do Bot

O bot foi projetado para:

- **👋 Saudar o usuário**: Ao ser adicionado a uma conversa, o bot envia uma mensagem de saudação.
- **📝 Iniciar a criação de um chamado**: Ele escuta por frases-gatilho como "criar chamado", "abrir chamado" ou variações similares.
- **📥 Coletar informações**: Após a ativação, ele guia o usuário para fornecer o título e a descrição do chamado.
- **✅ Confirmar o chamado**: O bot exibe um resumo com o título e a descrição fornecidos para que o usuário possa confirmar as informações.
- **🔁 Responder em 'echo'**: Se a mensagem do usuário não iniciar o processo de criação de um chamado, o bot simplesmente repete a mensagem recebida.
- **💾 Gerenciar o estado da conversa**: O bot utiliza o `ConversationState` para manter o controle do fluxo da conversa, salvando e recuperando o estado do diálogo.

---

## 📂 Guia de Arquivos

- **`echo_bot.py`**: Contém a lógica principal do bot, implementando a classe `EchoBot`.  
  Ele herda de `ActivityHandler` e define os métodos para lidar com diferentes tipos de atividades, como mensagens de texto e a adição de novos membros à conversa.  
  Ele gerencia o fluxo de criação de chamados, armazenando o estado da conversa e as informações do chamado (título e descrição).

- **`app.py`**: Ponto de entrada da aplicação.  
  Configura o servidor web (usando `aiohttp`) para escutar as mensagens da Bot Framework.  
  Cria e configura o adaptador (`CloudAdapter`), o gerenciamento de estado (`ConversationState` e `MemoryStorage`) e a instância do bot (`EchoBot`).  
  Define a rota `/api/messages` que processa as requisições recebidas.

- **`config.py`**: Define a classe `DefaultConfig`, que armazena as configurações do bot, como a porta do servidor e as credenciais (`APP_ID` e `APP_PASSWORD`).

- **`__init__.py`**: Permite tratar o diretório `bots` como um pacote Python, possibilitando a importação da classe `EchoBot` em outros arquivos, como `app.py`.

---

## 🚀 Guia de Utilização

Siga os passos abaixo para configurar e executar o bot:

1. **Clonar o repositório**:  
   Baixe o código do projeto para sua máquina.
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio

2. **Criação de um Ambiente Virtual (`venv`)**:  
   É altamente recomendável criar um ambiente virtual para isolar as dependências do projeto.

   ```bash
   python -m venv venv
   ```

3. **Ativar o Ambiente Virtual**:

   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. **Instalar as dependências**:  
   Instale os pacotes necessários do SDK da Bot Framework.

   ```bash
   pip install "botbuilder-core==4.14.0"
   pip install "aiohttp"
   ```

5. **Executar a aplicação**:  
   Com o ambiente virtual ativado e as dependências instaladas, você pode iniciar o bot.
   ```bash
   python app.py
   ```

> **ℹ️ Dica:** O bot será executado localmente na porta `3978`, conforme definido no arquivo `config.py`.

---

💡 **Próximos passos:**

- Configurar variáveis de ambiente para `APP_ID` e `APP_PASSWORD` (caso necessário).
- Publicar o bot em um servidor ou serviço de hospedagem.
