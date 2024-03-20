



# VoiceGPT
  
Envie um áudio e receba os dados conforme template criado no VoiceGPT.  
  
![banner](imgs/Banner-VoiceGPT.jpg)

## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Descrição do comando

### Obter o template do audio
  
Obtém os dados indicados no modelo VoiceGPT de um áudio
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|API Key|Chave gerada na seção Perfil do VoiceGPT.|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.ey...|
|ID do Template|O ID do modelo a ser ocupado. Pode ser obtido no URL https//voicegpt.rocketbot.com/#/template/{template}|83540b69bb195851896cd3881555c222|
|Selecione o áudio|URL do local e nome do áudio a ser enviado|C:/Users/user/Downloads/file.mp3|
|Atribuir resultado à variável|Variável onde o resultado será armazenado.|Variável|
