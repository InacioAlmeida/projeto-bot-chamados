# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, MessageFactory, TurnContext, ConversationState
from botbuilder.schema import ChannelAccount

lista = ["criar chamado","abrir chamado","criar um chamado","abrir um chamado"]

class EchoBot(ActivityHandler):
    def __init__(self, conversation_state: ConversationState):
        self.conversation_state = conversation_state
        # Criamos "acessadores de propriedade" para o estado da conversa.
        # Eles são como chaves para guardar e pegar nossas informações.
        self.flow_state_accessor = self.conversation_state.create_property("DialogFlow")
        self.title_state_accessor = self.conversation_state.create_property("TicketTitle")
        self.description_state_accessor = self.conversation_state.create_property("TicketDescription")

    async def on_turn(self, turn_context: TurnContext):
        # Sobrescrevemos o on_turn para garantir que o estado seja salvo no final de cada turno.
        await super().on_turn(turn_context)
        await self.conversation_state.save_changes(turn_context)

    async def on_members_added_activity(
        self, members_added: [ChannelAccount], turn_context: TurnContext
    ):
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Olá! Se precisar, posso criar um chamado para o NATI.")

    async def on_message_activity(self, turn_context: TurnContext):
        # Pega o estado atual do fluxo da conversa. O padrão é 'None'.
        flow = await self.flow_state_accessor.get(turn_context, None)
        user_message = turn_context.activity.text

        if flow is None:
            # Lista de frases que iniciam o diálogo para criar um chamado.
            trigger_phrases = ["criar chamado", "abrir chamado", "criar um chamado", "abrir um chamado"]
            user_message_lower = user_message.lower()

            # Usamos any() que funciona como um 'for' otimizado.
            # Ele verifica se ALGUMA das frases da lista está contida na mensagem do usuário.
            if any(phrase in user_message_lower for phrase in trigger_phrases):
                # Inicia o fluxo e pede o título.
                await self.flow_state_accessor.set(turn_context, "waiting_for_title")
                await turn_context.send_activity("Entendido. Por favor, informe o título do seu chamado.")
            else:
                # Se não, apenas responde com o eco.
                await turn_context.send_activity(MessageFactory.text(f"Echo: {user_message}"))

        elif flow == "waiting_for_title":
            # O bot estava esperando pelo título, então salvamos a mensagem do usuário como título.
            await self.title_state_accessor.set(turn_context, user_message)
            # Avança o fluxo para o próximo passo.
            await self.flow_state_accessor.set(turn_context, "waiting_for_description")
            await turn_context.send_activity("Obrigado. Agora, por favor, descreva o problema ou solicitação.")

        elif flow == "waiting_for_description":
            # O bot estava esperando pela descrição, então salvamos a mensagem.
            await self.description_state_accessor.set(turn_context, user_message)
            # Pega o título que guardamos no passo anterior.
            title = await self.title_state_accessor.get(turn_context)
            description = user_message  # a descrição é a mensagem atual

            # Monta a mensagem de confirmação.
            confirmation_message = (
                "Este é o chamado que deseja abrir?\n\n"
                f"**Título:** {title}\n\n"
                f"**Descrição:** {description}"
            )
            await turn_context.send_activity(MessageFactory.text(confirmation_message))

            # Limpa o estado para que a próxima mensagem comece um novo fluxo.
            await self.flow_state_accessor.delete(turn_context)
            await self.title_state_accessor.delete(turn_context)
            await self.description_state_accessor.delete(turn_context)