Objetivos secundários


### Configuração Adequada do Docker-Compose
#### Windows 11

Durante o processo de configuração do Docker-Compose no sistema operacional Windows 11, encontrei diversas dificuldades. Ao tentar executar o Docker-Compose pelo WSL, fui enviado para uma tela que apenas funcionaria ao utilizar o WSL2 com default. Percebi que isso exigiria um tempo adicional para ser resolvido.

Buscando alternativas, optei por utilizar o Docker Desktop e o PowerShell do Windows. No entanto, encontrei várias incompatibilidades ao tentar subir o Docker-Compose, especialmente ao definir a variável de ambiente com o comando `echo -e "AIRFLOW_UID=$(id -u)" > .env`.

Mesmo após conseguir subir o Airflow corretamente, percebi que a configuração de um ambiente no Windows exigiria muito esforço, considerando que estou mais acostumado ao universo Linux


#### Linux
####  1. Construir e Iniciar os Containers
```
docker-compose up -d
```

Durante a execução, recebi um `WARNING` que por si só não quebrava o ambiente, mas indicava possíveis problemas a serem resolvidos posteriormente. Além disso, um `ERROR` foi informado, indicando que a imagem necessária não foi encontrada.

![[Pasted image 20240710133120.png]]

#### 2. Construir a imagem local-cluster-airflow
`docker build -t local-cluster-airflow:1.0.0 .`

O build foi finalizado com sucesso so apresentou alguns `warnings` apos isso realizar o `docker-compose up -d` para subir todos os containers.

![[Pasted image 20240710135537.png]]

`docker-compose up -d`
Houve um problema indicando que o serviço `airflow-init` não conseguia ler. Isso ocorreu porque meu ambiente utiliza uma distribuição Linux, e o módulo SELinux bloqueia esse tipo de operação ao mapear as pastas do contêiner com as da minha máquina.

Obs.: Esta parte foi especialmente difícil de corrigir. Precisei eliminar várias possibilidades, como permissões do próprio contêiner, até descobrir essa particularidade do SELinux. Para desabilitar temporariamente e corrigir esse problema, use o comando `setenforce 0`.

![[Pasted image 20240709183419.png]]

Apos isso funcionou corretamente.

![[Pasted image 20240710135831.png]]

#### 3. Validadando se o ambiente está executando corretamente
`docker-compose ps`
O contêiner `airflow-init` não iniciou corretamente, como indica o estado `exit 1`. Isso mostra que houve um problema durante a inicialização dos contêineres. Vamos renovar todos os volumes para zerar o status e iniciar um ambiente limpo.

![[Pasted image 20240710140140.png]]

Troubleshoot:
```
docker compose down --volumes --remove-orphans
docker rm $(docker ps -a -q)

```
Seguir a documentação do airflow para ver algo que precisa ser feito 
https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html

```
# Set a variavel para construçãode permissão dos containers nas pastas
echo -e "AIRFLOW_UID=$(id -u)" > .env

# Inicialiar o databse primeiro para realizar do migrate
docker compose up airflow-init

# Rodar os conatainers
docker compose up -d
```

![[Pasted image 20240710141157.png]]

Apos o *troubleshot* mostra que todos os containers estão rodando. Vamos iniciar o ambiente do airflow no browser em http://localhost:11000. Funcionando perfeitamente.

![[Pasted image 20240710143244.png]]

![[Pasted image 20240710141254.png]]

Apos executar todos os passos corretamente e resolver problemas que foram aparecendo e todos os containers sendo executado corretamente algo na aplicação não subiu.
![[Pasted image 20240710141739.png]]

Para otimizar e esclarecer que este passo não inclui a intervenção no container para corrigir possíveis problemas no *nginx* ou no *gunicorn* que estão servindo a aplicação, eu preferi consultar a documentação. Ela fornece as imagens e serviços necessários para executar o Airflow. Veja mais detalhes em: [https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html)"

Após consultar a documentação e subir com a imagem estabelecida por lá  os serviços estão funcionando corretamente. Chuto aqui dizer que isso possa de funcionar o primeiro e não funcionar na máquina a questão da incompatibilidade com a versão do linux.

![[Pasted image 20240710142552.png]]
![[Pasted image 20240710142619.png]]

Subiu na porta *8080* vou realizar alternação para porta 11000 para validar e concluir essa parte do problema proposto.

![[Pasted image 20240710143354.png]]

![[Pasted image 20240710143340.png]]

## Extrair as informações da Pesquisa Industrial Anual - Empresas do ibge


Ao entrar na aplicação com *usuario: airflow* e *senha: airflow* mostra que houve um problema de importação devido o *ModuleNotFound* no pacote chamado *airflow.providers.papermil*

![[Pasted image 20240710150529.png]]

**Troubleshoot**: 
Preciso realizar o build novamente da imagem do `local-cluster-airflow:1.0.0.1`  utilizando a image base `apache/airflow:2.9.2` para instalar o novo pacote. Como os contêineres Docker permanecem em estado de execução, é necessário criar a imagem novamente com o novo pacote instalado.

![[Pasted image 20240710154442.png]]

## Conclusão

Apesar de ter progredido até o passo anterior, deparei-me com diversos desafios na ambientação com o Airflow. Minha inexperiência com a ferramenta me levou a buscar materiais introdutórios para compreendê-la melhor. No entanto, minha familiaridade com o Python e Linux se mostrou um ponto forte nesse processo.

