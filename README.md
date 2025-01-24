# Teste Técnico: Configuração e Execução de um Pipeline de Dados

Este repositório é parte de um teste técnico para avaliar a capacidade de resolver problemas comuns enfrentados por um Engenheiro de Dados. Siga as instruções abaixo para configurar o ambiente, implementar as soluções e submeter o resultado.

## Requisitos do Ambiente

### Ferramentas Necessárias

- Docker

### Configuração do Ambiente

1. **Clonar o Repositório:**

   ```bash
   git clone https://github.com/arrudafdc/teste-engenheiro-de-dados-observatorio-da-industria.git
   cd teste-engenheiro-de-dados-observatorio-da-industria
   ```

2. **Construir e Inicializar o Ambiente:**

   ```bash
   docker-compose up --build -d
   ```

3. **Limpar Imagens Intermediárias:**

   ```bash
   docker image prune -f
   ```

4. **Acessar a Interface Web do Airflow:**

   [http://localhost:11000](http://localhost:11000)

   Credenciais de acesso padrão:

   - **Usuário:** `airflow`
   - **Senha:** `airflow`

## Implementação

1. **Execução da DAG:**
   A DAG `pesquisa_industrial_anual_empresas` deve ser executada na interface do Airflow. O resultado final será salvo na pasta `resultado`.

## Considerações Importantes

- **Neste projeto, optei por incluir o arquivo .env no repositório com o objetivo de facilitar a avaliação do teste técnico. Reconheço que, em situações reais, essa prática não é recomendada devido a questões de segurança e proteção de informações sensíveis, como chaves de API, credenciais e configurações específicas de ambiente.**
