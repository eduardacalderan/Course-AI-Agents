# 1. Corretor de Imóveis

**Descrição:** Este agente é responsável por obter as preferências do cliente (como tipo de imóvel, faixa de preço, etc.) e buscar imóveis compatíveis em um banco de dados (arquivo CSV). Ele é especializado no mercado imobiliário e faz isso através da ferramenta CSVSearchTool.  
**Objetivo:** Encontrar as melhores opções de imóveis com base nas preferências do cliente.  
**Ferramenta utilizada:** CSVSearchTool (para buscar imóveis em um arquivo CSV).  

# 2. Analista de Mercado Imobiliário

**Descrição:** Este agente analisa as tendências de preços de imóveis em diferentes cidades, ajudando a prever a valorização ou desvalorização do mercado. Ele utiliza um conjunto de dados simulados para obter informações sobre as tendências de preço (aumento, queda ou estabilidade).  
**Objetivo:** Analisar o histórico de preços e fornecer insights sobre a valorização ou desvalorização dos imóveis.  
**Ferramenta utilizada:** TendenciaPrecosImoveisTool (para analisar a tendência de preços em uma cidade específica).  

# 3. Analista de Notícias Imobiliárias

**Descrição:** Este agente busca notícias recentes sobre o mercado imobiliário, analisando fatores externos, como mudanças econômicas ou eventos que podem impactar os preços dos imóveis.  
**Objetivo:** Obter informações relevantes sobre o mercado imobiliário por meio de notícias e tendências externas.  
**Ferramenta utilizada:** DuckDuckGoSearchResults (para buscar notícias sobre imóveis e economia).  

# 4. Consultor Financeiro

**Descrição:** O consultor financeiro ajuda a analisar a renda do cliente e sugerir opções de financiamento viáveis para a compra de imóveis, considerando as taxas de juros e prazos oferecidos pelas instituições financeiras.  
**Objetivo:** Oferecer opções de financiamento com base nas condições financeiras do cliente.  
**Ferramenta utilizada:** Nenhuma ferramenta externa é usada diretamente, mas o agente pode fornecer análises e sugestões.  

# 5. Redator de Relatórios

**Descrição:** Este agente gera relatórios persuasivos e bem estruturados sobre os imóveis recomendados ao cliente. Ele considera as análises de mercado, as tendências de preços e as opções de financiamento para criar um relatório final.  
**Objetivo:** Criar um relatório detalhado sobre o imóvel escolhido, incluindo análise de mercado e opções financeiras.  
**Ferramenta utilizada:** Nenhuma ferramenta externa é usada diretamente, mas ele integra informações dos outros agentes para elaborar o relatório.  

# Objetivo geral do programa

O programa em questão simula uma consultoria imobiliária completa, na qual o cliente recebe uma análise detalhada sobre imóveis disponíveis, tendências de mercado, notícias relevantes e opções de financiamento. O fluxo de trabalho é organizado e estruturado em várias tarefas e agentes, que colaboram entre si para fornecer ao cliente as melhores opções baseadas em dados e análises detalhadas.  

O processo final é gerido por um Crew, que é um conjunto de agentes que colaboram para cumprir as tarefas relacionadas à busca e recomendação de imóveis, análise de tendências de preços e financiamento. O sistema executa esse processo através de uma série de interações entre os agentes e gera o resultado desejado.  
