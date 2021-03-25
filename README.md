# Mooney - Desafio Backend

## Requisitos

Crie um endpoint que retorne sugestões para autocompletar cidades do Brasil.

- o endpoint deve ser exposto em /suggestions
- o termo de pesquisa parcial (ou completo) é passado como um query param `q`
- a localização de quem chama o endpoint pode ser fornecida opcionalmente por meio de query params `lat` e `lon` para ajudar a melhorar as pontuações relativas
- o endpoint retorna uma resposta JSON com uma lista de correspondências sugeridas pontuadas
  - as sugestões devem ser ordenadas por pontuação decrescente
  - cada sugestão deve ter uma pontuação entre 0 e 1 (inclusive), indicando confiança na sugestão (1 é o mais confiante)
  - cada sugestão tem um nome que pode ser usado para eliminar a ambigüidade entre locais com nomes semelhantes
  - cada sugestão tem uma latitude e longitude
- todos os testes funcionais devem passar (testes adicionais podem ser implementados conforme necessário)
- recomendamos que o deploy do aplicativo final seja feito no [Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) pela facilidade
- sinta-se à vontade para adicionar mais recursos, se desejar!

## Exemplo de Resposta

Essas respostas têm o objetivo de fornecer orientação. Os valores exatos podem variar com base na fonte de dados e no algoritmo de pontuação.

### Quase partida

GET /suggestions?q=Londo&latitude=43.70011&longitude=-79.4163
```json
{
  "suggestions": [
    {
        // TODO:
    ]
}
```

### Sem correspondência

GET /suggestions?q=UmaCidadeAleatoriaNoMeioDoNada
```
{
  "suggestions": []
}
```

## Requisitos não funcionais

- Todo o código deve ser escrito em Python.
- Devem ser implementadas mitigações para lidar com altos níveis de tráfego.
- O desafio deve ser enviado como solicitação pull contra este repo (faça um fork e criar um pull request).
- Documentação e facilidade de manutenção são uma vantagem.

## Dados

Você pode encontrar os dados necessários junto com sua descrição e documentação no diretório de [`data`](data/).

## Avaliação

Usaremos os seguintes critérios para avaliar sua solução:

- Capacidade de seguir instruções
- Experiência do desenvolvedor (como é fácil executar sua solução localmente, quão clara é sua documentação, etc)
- Correção da solução
- Desempenho
- Monitoramento (métricas de engenharia e de negócio)
- Testes (qualidade e cobertura)
- Estilo e limpeza do código
- Atenção aos detalhes
- Capacidade de fazer suposições sensatas

Não há problema em nos fazer perguntas!

Sabemos que o tempo para este projeto é limitado e é difícil criar uma solução "perfeita", por isso vamos considerar isso junto com sua experiência ao avaliar o envio.

## Começando

### Pré-requisitos

Você vai precisar de:

- Git
- python3

### Configurando seu ambiente

Comece criando um fork deste repositório e clonando seu fork. O GitHub possui aplicativos para Mac e Windows que facilitam isso.

Instale o python3.

### Configurando o projeto

// TODO: intruções de como configurar o projeto python

### Executando os testes

O conjunto de testes pode ser executado com:

// TODO: instruções de como rodar os testes

### Iniciando o aplicativo

Para iniciar um servidor local, execute:

// TODO: instruções de como rodar local