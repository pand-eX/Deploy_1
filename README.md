# Deploy de um Modelo de Machine Learning com Microsserviços, comunicação gRPC e Docker.

[![NPM](https://img.shields.io/npm/l/react)](https://github.com/pand-eX/Deploy_1/blob/main/LICENSE) 

# Sobre o Projeto.

Basicamente nós vamos desenvolver um modelo de Machine Learning que vai realizar previsões quando receber novos dados.
O Docker vai ser nossas ferramentas de Deploy, no docker nós vamos fazer a implementação de um modelo de machine learning para isso vamos usar python e Scikit-learn.
Uma vez que o modelo estiver pronto ele vai receber requisição, vamos passar dados para o modelo e ele vai devolver previsões como resposta, mas como vai ocorrer essa comunicação? Precisamos estabelecer um Protocolo para esse caso usaremos o gRPC que é um dos principais protocolos de comunicação em arquitetura de microsserviços. 


## E por que os modelos de Machine Learning devem ser implantados como Microsserviços?? 

Os Cientistas de Dados ou Engenheiros de Machine Learning precisam explorar e experimentar diferentes modelos antes de se estabelecerem em um modelo que funcione para seu caso de uso específico. Depois que um modelo é desenvolvido, há vantagens inerentes à implantação de modelos de aprendizado de máquina em um contêiner e a servi-lo como Microsserviço.

-Este projeto faz parte do meu portfólio pessoal, então ficarei feliz se você puder me fornecer qualquer feedback sobre o projeto, código, estrutura ou qualquer coisa que você possa relatar que possa me fazer um melhor engenheiro de dados!

Email-me: henricao_7@yahoo.com.br

Connect with me at [LinkedIn](https://www.linkedin.com/in/henrique-castro-484269203//).

![1](https://github.com/pand-eX/Deploy_1/blob/main/Deploy%20de%20modelo/assets/1.png)
Basicamente nós vamos desenvolver um modelo de Machine Learning que vai realizar previsões quando receber novos dados.
O Docker vai ser nossas ferramentas de Deploy, no docker nós vamos fazer a implementação de um modelo de machine learning para isso vamos usar python e Scikit-learn.
Uma vez que o modelo estiver pronto ele vai receber requisição, vamos passar dados para o modelo e ele vai devolver previsões como resposta, mas como vai ocorrer essa comunicação? Precisamos estabelecer um Protocolo para esse caso usaremos o gRPC que é um dos principais protocolos de comunicação em arquitetura de microsserviços. 
O Python oferece um pacote que facilita o desenvolvimento da comunicação via gRPC.
Atividades: Como não temos um cientista de dados a nossa disposição iremos fazer o trabalho. O foco desse projeto não é ter um modelo complexo, mas mostrar a infra-estrutura do Deploy com Docker.

O intuito é o Deploy e não a criação e treinamento do modelo de Machine Learning.

## Passos:
![2](https://github.com/pand-eX/Deploy_1/blob/main/Deploy%20de%20modelo/assets/2.png)

![3]![1](https://github.com/pand-eX/Deploy_1/blob/main/Deploy%20de%20modelo/assets/3.png)

Treinando nosso modelo, vamos oferecê-lo como Microsserviço a ser acessado Via gRPC em container Docker.

## Porque construir Microsserviços com gRPC?

As primeiras implementações de microsserviços usavam a arquitetura REST(Reresentation State Transfer) com a tecnologia de comunicação quase padrão. No entanto, os serviços RESTful constumam ser úteis para serviços externos, expostos diretamente aos consumidores. Como são baseados em mensagens convencionais em texto, JSON, XML e etc. Otimizadas para humanos, essas não são as escolhas ideias para a comunicação interna de serviço a serviço.

![4]![1](https://github.com/pand-eX/Deploy_1/blob/main/Deploy%20de%20modelo/assets/4.png)

Em vez disso, usando um protocolo de mensagens baseado em texto, podemos aproveitar um protocolo binário otimizado para comunicação entre serviços. o gRPC(Chamada de procedimento remoto) é uma escolha ideal para comunicação entre serviços, pois usa protocol, buffers como o formato de intercâmbio de dados binários para comunicação entre serviços.
Quando criamos vários microsserviços com diferentes tecnologias e linguagens de programação é importante ter uma maneira padrão de definir interfaces de serviço e formatos subjacentes de intercâmbio de mensagens. O gRPC oferece uma maneira limpa e poderosa de especificar comunicação de serviços usando protocol buffers. Portanto, o gRPC é provavelmente a solução mais viável para criar uma comunicação entre microsserviços internos.

![5]![1](https://github.com/pand-eX/Deploy_1/blob/main/Deploy%20de%20modelo/assets/5.png)

Nós precisaremos usar o gRPC porque eu vou cria um microsserviços para o servidor e outro para o cliente e eles vão se comunicar e essa comunicação existe via gRPC.

Os Protocol buffers são o mecanismo extensível, neutro em linguagem, neutro em plataforma e do Google para serializar dados estruturados - pense em XML, mas menor, mais rápido e mais simples. você define como deseja que seus dados sejam estruturados uma vez e, em seguida, pode usar código-fonte especial gerado para escrever e ler com facilidade seus dados estruturados de e para uma variedade de fluxos de dados e usando uma variedade de linguagens. Ou seja, uma espécie de grande padrão de comunicação criado pela equipe da Google. É um protocolo gratuito de comunicação totalmente neutro a linguagem, totalmente neutro em plataforma que permite comunicação fácil entre serviços totalmente heterógeno por isso e amplamente usado em infraestrutura de microsserviços não apenas para machine learning, mas para aplicações em modo geral.

![6]![1](https://github.com/pand-eX/Deploy_1/blob/main/Deploy%20de%20modelo/assets/6.png)

## gRPC e Protocol Buffers.

Com o gRPC, um clinte pode chamar métodos diretamente em uma aplicação servidor em uma máquina diferente, como se fosse um objeto local. o gRPC é baseado nos fundamentos da tecnologia RPC(Remote Procedure Call) convencional, mas implementando em cima das pilhas modernas de tecnologia, como HTTP2, protocol buffers, etc. para garantir a máxima interoperabilidade.

![7]![1](https://github.com/pand-eX/Deploy_1/blob/main/Deploy%20de%20modelo/assets/7.png)

O gRPC suporta nativamente a capacidade de definir um contrato de serviço usando a IDL(Interface Definition Language) do gRPC. Portanto, como a parte da definição de serviço, você pode especificar os métodos que podemos ser chamados remotamente e a estrutura de dados dos parâmetro e tipos de retorno.

![8]![1](https://github.com/pand-eX/Deploy_1/blob/main/Deploy%20de%20modelo/assets/8.png)

A figura ilustra o uso do gRPC com um aplicativo de varejo online como parte de um serviço de inventário e pesquisa de produtos.
O contrato para o serviço de inventário é definido usando o gRPC IDL, especificado no arquivo inventário.proto(criado com protocol buffers).
Portanto, um desenvolvedor do serviço de inventário deve primeiro definir todos os recursos de negócio usando o serviço e em seguida gerar o código do esqueleto do lado do serviço a partir do arquivo proto. Da mesma forma, o código do ado do cliente(Stub) pode ser gerado usando o mesmo arquivo proto.

![9]![1](https://github.com/pand-eX/Deploy_1/blob/main/Deploy%20de%20modelo/assets/9.png)

Como o gRPC é independente da linguagem de programação você pode usar linguagens heterogêneas para cria serviços e clientes.

## Iniciando o Projeto

Para iniciar cria um diretório para ter as coisas organizadas no meu caso chamei de deploy, nele tem o modelo de Machine Learning. 
A primeira etapa é definir o protocolo de comunicação do serviço utilizando exatamente o protocolo Buffers
Basicamente define o serviço com a requisição de entrada que são as variáveis preditoras para o meu modelo e então aquilo que será retornado pelo microsserviço que nada mais é que a previsão do nosso modelo.

![10]![1](https://github.com/pand-eX/Deploy_1/blob/main/Deploy%20de%20modelo/assets/10.png)

Agora temos que compila o protocolo de comunicação para gerar os arquivos em formato python como os exemplos acima ele é agnóstico, ou seja, ele não é voltado para 1 linguagem específica depois que você cria o arquivo .proto então você compila de acordo com a linguagem que vai ser utilizada.
Nós temos a importação do pacote protoc ele nós oferece a função main que basicamente vai fazer a leitura do iris.proto e vai gerar dois arquivos python como saída para isso precisamos instalar o grpcio e o grpcio.tools

![11]![1](https://github.com/pand-eX/Deploy_1/blob/main/Deploy%20de%20modelo/assets/11.png)

Vou abrir um arquivo para verificar a mensagem nele.

![12]![1](https://github.com/pand-eX/Deploy_1/blob/main/Deploy%20de%20modelo/assets/12.png)


Isso foi gerado no momento que fizemos a compilação. Nada mais é que um conjunto de código em python para executar realmente o microsserviço com gRPC.

O proxímo passo será definir um servidor gRPC para que possamos oferecer o microsserviço. O servidor gRPC vai receber conexões de um serviço cliente e vai repassar essas conexões para o modelo de Machine Learning então o modelo vai realizar seu processamento vai devolver uma resposta e então o servidor gRPC vai emitir a resposta para a chamada Cliente.

Dentro do script é apenas programação em python ele praticamente herda as propriedades daqueles 2 módulos criados durante a compilação do arquivo .proto e nós definimos uma sequência de operações.

Essa é um componente principal dessa infraestrutura para servir o modelo de Machine Learning. Portanto nossa classe que herda propriedades da classe mãe que foi gerada pelo Google na hora da compilação e nela criamos dois métodos o primeiro obtém o modelo de Machine Learning então vamos coletar o caminho completo e fazemos a leitura do modelo repare no script que estou usando o load do pacote joblib que vai carregar na memória do computador o modelo que estava gravado no arquivo em disco. Em disco o modelo não serve para nada eu tenho que carregar na memória do computador para que ele possa fazer o trabalho na sequência também definimos uma função, método para ler as variáveis que venha na request, na requisição de entrada, fazemos a leitura das variáveis e colocamos em 4 variável python e chamamos o modelo, a partir do modelo nós chamamos a função predict e então passamos as 4 variáveis como entrada gravo resultado e depois chamamos o método IrisPredicitReply para dar uma resposta, o servidor recebe a requisição de entrada e tem que responder aquela requisição ela não pode se perder no servidor. Precisamos ainda de uma função para servir, ou seja, abrir o serviço no sistema operacional.

Agora precisamos definir o cliente gRPC. Basicamente o script envia request para o servidor gRPC enviando as 4 variáveis preditoras que serão lidas pelo modelo essa requisição então espera uma resposta obtém uma resposta do gRPC e imprimi o resultado na tela 


Agora vamos colocar o servidor gRPC no conteiner Docker

![13]![1](https://github.com/pand-eX/Deploy_1/blob/main/Deploy%20de%20modelo/assets/13.png)

Agora a imagem está pronta para ser utilizada.
Se eu tentar chamar os módulos ele não vai ser executado por que eu não coloquei ele dentro do script do dockerfile precisamos fazer isso manualmente igual fizemos nas etapas acima pip install grpcio e o outro também pip install grpcio.tools e também o joblib para carregar o modelo de Machine Learning, eu poderia fazer isso automaticamente no script... 

Pronto agora sim o contêiner está perfeito. Ele está pronto para oferecer o modelo de Machine Learning.

Lembrando que no arquivo de cliente servidor que configuramos eu coloquei a conexão via localhost, mas no contêiner o localhost não será o contêiner tem seu próprio endereço IP então tenho que usar esse IP para eu fazer a conexão com minha máquina cliente nesse caso com minha requisição cliente. Você vai usar o comando sudo docker ps e pegar o id então colocar no comando sudo docker inspect “id” lá no final do arquivo tem o IP.

![14]![1](https://github.com/pand-eX/Deploy_1/blob/main/Deploy%20de%20modelo/assets/14.png)

Então esse é o commando que precisamos executar para chamada cliente python grpc_client.py --host “ID” --port 50052

![15](https://github.com/pand-eX/Deploy_1/blob/main/Deploy%20de%20modelo/assets/15.png)

E assim concluímos o deploy do modelo de Machine Learning usando microsserviços e Docker.
