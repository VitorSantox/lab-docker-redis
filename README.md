
# Lab Docker Redis

Este projeto consiste em um laboratório para demonstrar a utilização da conteinerização com Docker, focando na criação e gerenciamento de contêineres Redis. O objetivo é fornecer um ambiente prático para experimentar com contêineres e compreender como o Redis pode ser empregado em um contexto de conteinerização.

## Configuração do Ambiente

### Máquina Host

Antes de iniciar o laboratório, é necessário configurar sua máquina host:

1. **Windows Subsystem for Linux (WSL)**: Caso esteja utilizando o Windows, é recomendável instalar o WSL para uma melhor integração com ferramentas do Linux.

2. **Docker**: Instale o Docker na máquina host. O Docker é a plataforma de conteinerização que possibilita a criação e execução dos contêineres.

3. **Redis Insight**: Instale o Redis Insight na máquina host para monitorar e gerenciar os contêineres Redis de forma gráfica.

### Visual Studio Code (VSCode)

Utilize o Visual Studio Code para uma experiência de desenvolvimento mais eficiente:

1. **Extensões do VSCode**:
   - Docker: Essa extensão facilita a gestão de contêineres diretamente do VSCode.
   - Remote - Containers: Permite desenvolver dentro de um contêiner, garantindo um ambiente consistente.

## Executando o Projeto

Para executar o projeto, siga os passos abaixo:

1. **Docker Image Redis**: Verifique se você possui a imagem do Redis baixada. Caso contrário, execute o seguinte comando para baixar a imagem:
   
   ```bash
   docker pull redis
   ```

2. **Arquivo docker-compose.yml**: Utilize o arquivo `docker-compose.yml` para configurar e iniciar os contêineres Redis. O arquivo contém detalhes sobre a rede, volumes e configurações necessárias para o laboratório.

3. **Executando o Projeto**: Execute o seguinte comando para iniciar os contêineres de acordo com a configuração no `docker-compose.yml`:

   ```bash
   docker-compose up -d
   ```

## Estrutura do Projeto

O projeto é organizado nos seguintes arquivos:

- **Dockerfile**: Descreve a construção da imagem Docker personalizada, se necessário.
- **docker-compose.yml**: Define a configuração dos contêineres e sua interação, permitindo iniciar e gerenciar todos os componentes facilmente.
- **Outros arquivos**: Podem incluir configurações específicas ou scripts auxiliares, dependendo das necessidades do projeto.

## Próximos Passos

Após a execução do projeto, você terá um ambiente de laboratório funcional para experimentar e explorar a conteinerização com Docker e o uso do Redis. Você pode aprimorar o projeto adicionando mais recursos, explorando diferentes configurações de contêineres ou até mesmo integrando outros serviços.

Aproveite essa oportunidade para adquirir conhecimentos práticos em conteinerização e Redis, além de fortalecer suas habilidades de desenvolvimento com ferramentas modernas como o Docker e o VSCode.

## Conclusão

Este laboratório é uma excelente maneira de entender os princípios básicos de conteinerização, bem como aprender a configurar, executar e gerenciar contêineres Redis. Use esse projeto como base para suas explorações futuras e continue aprimorando suas habilidades em desenvolvimento de software e gerenciamento de infraestrutura.
![image](https://user-images.githubusercontent.com/88788394/232904675-bb9fa23c-9921-4ad1-b975-45a9f970636c.png)
