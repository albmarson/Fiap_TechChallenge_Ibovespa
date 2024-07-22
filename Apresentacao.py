import streamlit as st
from PIL import Image


# Configurações iniciais
st.set_page_config(page_title="Modelagem Preditiva IBOVESPA", page_icon=":book:", layout="wide")

# Função para mostrar o Propósito
def show_propósito():
    # Título principal
    st.markdown('<h1 style="text-align: center;">Modelagem Preditiva da IBOVESPA</h1>', unsafe_allow_html=True)
    
    # Subtítulo
    st.markdown('<h5 style="text-align: center; font-style: italic;">Construção e Avaliação de um Modelo de Previsão de Fechamento Diário</h5><br>', unsafe_allow_html=True)

    # Créditos
    st.markdown("""
    <div style="font-size: 12px; text-align: right; max-width: 490px; margin-left: auto; display: block;">
        Elaborado por Alberto M. Marques Marson, Técnico em Informática, Analista e Desenvolvedor de Sistemas, atualmente cursando pós-graduação em Data Analytics.<br><br>
    </div>
    """, unsafe_allow_html=True)

    # Descrição do estudo
    st.markdown('''
    <div style="display: flex; justify-content: center; align-items: center; margin: 0 auto;">
        <div style="border-left: 5px solid white; height: 100%; padding-left: 20px; text-align: justify;">
            O presente estudo, proposto pela FIAP como parte do projeto de conclusão do segundo trimestre do curso de pós-graduação em Data Analytics, realiza uma análise, construção e avaliação de um modelo para a previsão do fechamento diário do Ibovespa - <i>Índice da Bolsa de Valores de São Paulo</i>.
        </div>
    </div><br>
    ''', unsafe_allow_html=True)

    # Carregar e exibir a imagem
    imagem = "Img/Home.jpg"
    try:
        img = Image.open(imagem)
        st.image(img, caption="", use_column_width=True)
    except FileNotFoundError:
        st.error("Imagem não encontrada. Verifique o caminho para a imagem.")

# Chame a função para mostrar o Propósito
show_propósito()

def show_intro():
# Seções do conteúdo
    st.header("Introdução")

st.markdown("""
Antes de adentrar em qualquer análise, é crucial compreender profundamente o tema em questão, explorando suas nuances e contextos específicos. Esta abordagem não apenas estabelece uma base sólida de entendimento, mas também possibilita uma interpretação mais informada e precisa dos dados, além de facilitar a formulação de hipóteses.

No dinâmico e complexo ambiente do mercado financeiro, onde a precisão na previsão dos movimentos futuros dos ativos é decisiva para tomadas de decisão eficazes, este estudo se propõe a desenvolver um modelo preditivo baseado em dados históricos da IBOVESPA, a principal bolsa de valores do Brasil. O objetivo é criar uma série temporal capaz de prever diariamente o fechamento do índice, utilizando técnicas avançadas de análise de dados.

Para alcançar esse fim, os dados históricos da IBOVESPA foram obtidos de maneira automatizada, simplificando a extração de informações do mercado financeiro. A escolha pelo uso de métodos automatizados foi motivada pela necessidade de reduzir o trabalho manual na coleta de dados, garantindo maior eficiência e precisão. O processo envolveu etapas detalhadas de limpeza, transformação e seleção das variáveis relevantes para o modelo, seguidas pela aplicação de técnicas de análise exploratória para identificar padrões temporais e relações entre os dados.

A modelagem preditiva adotada baseia-se em séries temporais, uma abordagem adequada dada a natureza dos dados financeiros, que frequentemente apresentam comportamentos temporais e sazonalidades distintas. O modelo foi treinado e ajustado meticulosamente para maximizar a precisão na previsão do fechamento diário da IBOVESPA. Espera-se que o modelo desenvolvido alcance uma acurácia superior a 70%, medida por métricas robustas de desempenho. Este estudo não só visa contribuir para uma compreensão mais profunda dos movimentos do mercado financeiro brasileiro, mas também demonstrar a aplicação prática de técnicas analíticas avançadas em um contexto de investimentos dinâmico e desafiador.
""")
def show_ibovespa():
    st.header("IBOVESPA: O Pilar do Mercado Financeiro Brasileiro")

st.markdown("""
A IBOVESPA, principal índice da bolsa de valores brasileira, é um indicador crucial do mercado financeiro do país. Criada em 1968, a IBOVESPA reflete a performance das ações mais significativas e influentes, servindo como barômetro das condições econômicas e políticas do Brasil. Com uma composição diversificada que abrange setores como financeiro, commodities e tecnologia, a IBOVESPA desempenha um papel fundamental na orientação de investidores e na formulação de estratégias de mercado, tanto a nível nacional quanto internacional.
""")
def show_fonte_dados():
    st.header("Fonte de Dados")

st.markdown("""
A base de dados utilizada foi extraída de maneira automatizada, fornecendo informações detalhadas sobre os preços de abertura, fechamento, máximos, mínimos e volumes negociados ao longo do período analisado. Esse processo automatizado contribuiu significativamente para reduzir o tempo de extração dos dados, evitando a necessidade de extração manual, que poderia ser mais demorado e propenso a erros. 

Visando trazer uma maior acurácia durante a análise, o período analisado compreende desde 01/01/2001 até 30/06/2024, permitindo capturar uma ampla gama de eventos, tendências e mudanças relevantes para o estudo em questão.
""")
def show_preparacao_analise():
    st.header("Preparação e Análise da Base de Dados")

st.markdown("""
Para iniciar nossa análise, é necessário realizar um processo de pré-processamento de dados, a fim de analisar de maneira precisa e direcionada os dados relativos ao desempenho histórico da IBOVESPA. Nosso objetivo principal é obter uma visão abrangente das tendências e variações do índice ao longo dos anos.

Após o processamento inicial, identificamos as seguintes observações:

- **Variação diária:** A extração automática dos dados não inclui diretamente a porcentagem de variação diária dos preços, um indicador crucial para entender as oscilações do mercado. Utilizamos os preços de fechamento diários para calcular essa métrica.

- **Redefinição do índice temporal:** O índice do DataFrame foi redefinido para garantir a precisão na análise temporal dos dados. Isso é fundamental para realizar análises sequenciais e identificar padrões ao longo de períodos específicos.

- **Integridade dos dados:** Garantimos que não há dados duplicados na base. A ausência de valores duplicados é crucial para manter a consistência e a confiabilidade das análises.

- **Ausência de valores nulos:** Não foram identificados dados faltantes na maioria das colunas, exceto na coluna de Volume. Isso é fundamental para evitar viéses e garantir que todas as informações relevantes estejam disponíveis para análise.

- **Porcentagem de valores zerados no volume de negociações:** Aproximadamente 25.24% dos registros na coluna de volume de negociações apresentam valores zerados. Isso indica períodos de baixa atividade de mercado ou ausência de transações.
""")
def show_analise_retorno():    
    st.header("Análise dos Retornos Diários do Ibovespa")

st.markdown("""
Para compreender as variações históricas do índice Ibovespa, calculamos os retornos diários utilizando os dados de fechamento. O gráfico apresenta visualmente as flutuações nos retornos ao longo do tempo, destacando momentos significativos de crescimento e declínio. A análise dos picos positivos e negativos revela períodos de alta volatilidade e pode indicar eventos econômicos e financeiros impactantes que influenciaram o mercado brasileiro.

Observamos variações significativas no gráfico de retornos diários do Ibovespa, destacando períodos como entre 2008 e 2010 e mais recentemente entre 2020 e 2024, que fogem um pouco do padrão histórico. É crucial investigar os motivos que podem ter impactado essas variações.

Entre 2008 e 2010, o mundo enfrentou uma crise financeira global severa, conhecida como a ‘Crise Financeira de 2008’, desencadeada pela crise no mercado imobiliário dos EUA. Esta crise teve um efeito dominó nos mercados financeiros globais, causando queda nos preços das ações, aumento do desemprego e uma recessão econômica global. No Brasil, o impacto foi sentido com a redução do crescimento econômico, aumento da inflação e desvalorização do Real, afetando diretamente o desempenho do Ibovespa.

Entre 2020 e 2024, mais especificamente a partir de 2020, a pandemia de COVID-19 emergiu como uma crise de saúde global sem precedentes. As medidas de lockdown para conter a propagação do vírus levaram a paralisações na atividade econômica global, interrupções nas cadeias de suprimentos, e uma profunda incerteza nos mercados financeiros. No Brasil, as consequências da pandemia incluíram volatilidade nos preços das ações, oscilações cambiais e uma desaceleração econômica significativa.
""")

# Carregar a imagem
imagem_retornos = "Img/Retornos_Diarios_Ibovespa.png"
try:
    img = Image.open(imagem_retornos)
    
   
    largura_max = 1000  
    altura_max = 700   
    
    img.thumbnail((largura_max, altura_max))  
    
    
    col1, col2, col3 = st.columns([1, 3, 1])  
    
    with col2:
        st.image(img, caption="", use_column_width=True)  

except FileNotFoundError:
    st.error("Imagem não encontrada. Verifique o caminho para a imagem.")
def show_volatilidade():
    st.header("Volatilidade")

st.markdown("""
A volatilidade histórica anualizada de 27.32% calculada para o Ibovespa representa a medida das flutuações diárias dos retornos das ações ao longo do período analisado, equivalente a um ano de negociação. Este valor indica a intensidade das variações nos preços das ações, refletindo um mercado onde os retornos diários variaram em média 27.32% ao ano. Tal volatilidade evidencia um ambiente de investimento mais instável e imprevisível, aumentando a incerteza em relação aos retornos esperados e influenciando decisões estratégicas de alocação de ativos e gestão de portfólio.
""")

# Carregar a imagem
imagem_votalidade = "Img/Votalidade_Historica.png"
try:
    img = Image.open(imagem_votalidade)
    
   
    largura_max = 1000  
    altura_max = 700   
    
    img.thumbnail((largura_max, altura_max))  
    
    
    col1, col2, col3 = st.columns([1, 3, 1])  
    
    with col2:
        st.image(img, caption="", use_column_width=True)  

except FileNotFoundError:
    st.error("Imagem não encontrada. Verifique o caminho para a imagem.")
def show_padroes_preco():
    st.header("Padrões de Preço do Ibovespa")

st.markdown("""
O gráfico de Candlestick aplicado aos dados da Ibovespa oferece uma representação visual detalhada dos preços de abertura, fechamento, máxima e mínima de cada período analisado. Cada candlestick mostra claramente a diferença entre abertura e fechamento (corpo) e as variações entre máxima e mínima (sombras). Os candles de cor azul indicam que o fechamento ocorreu acima da abertura, enquanto os candles vermelhos indicam o contrário. Essa representação gráfica é essencial para identificar tendências de alta ou baixa, reversões de mercado e períodos de indecisão no cenário financeiro.
""")

# Carregar a imagem
imagem_candlestick = "Img/Candlestick.png"
try:
    img = Image.open(imagem_candlestick)
    
   
    largura_max = 1000  
    altura_max = 700   
    
    img.thumbnail((largura_max, altura_max))  
    
    
    col1, col2, col3 = st.columns([1, 3, 1])  
    
    with col2:
        st.image(img, caption="", use_column_width=True)  

except FileNotFoundError:
    st.error("Imagem não encontrada. Verifique o caminho para a imagem.")

st.header("Variação Percentual Anual")

st.markdown("""
A análise da variação percentual anual revela como os índices analisados evoluíram ao longo dos últimos anos, oferecendo insights sobre as tendências econômicas e sociais. A tabela a seguir mostra a média da variação percentual para cada ano, calculada a partir dos dados mensais disponíveis:

- **2020:** 1,01% - O ano de 2020 foi marcado por um crescimento médio de 1,01% na variação percentual. Esse aumento ocorreu em meio à pandemia global de COVID-19, que trouxe uma série de desafios econômicos e sociais. Apesar das dificuldades, alguns setores conseguiram se adaptar rapidamente e até prosperar, especialmente aqueles envolvidos em tecnologia e saúde.

- **2021:** -0,98% - Em 2021, a variação percentual média caiu para -0,98%, indicando uma leve retração. Esse ano foi marcado por desafios contínuos relacionados à pandemia, incluindo a escassez de suprimentos e dificuldades na cadeia de suprimentos global.

- **2022:** -2,48% - O ano de 2022 apresentou uma variação percentual média de -2,48%, refletindo um ambiente econômico desafiador. A inflação elevada e a instabilidade política contribuíram para uma diminuição geral no desempenho do índice.

- **2023:** -1,21% - A variação percentual média foi de -1,21% em 2023, demonstrando uma leve recuperação em relação ao ano anterior, mas ainda enfrentando desafios econômicos persistentes.

- **2024:** -1,30% - Para 2024, a variação percentual média foi de -1,30%, indicando um possível novo desafio ou desaceleração. A análise de dados mais recentes pode revelar fatores específicos que contribuíram para essa variação negativa.
""")

# Carregar a imagem
imagem_vpercentual = "Img/Variacao_Percentual.png"
try:
    img = Image.open(imagem_vpercentual)
    
   
    largura_max = 1000  
    altura_max = 700   
    
    img.thumbnail((largura_max, altura_max))  
    
    
    col1, col2, col3 = st.columns([1, 3, 1])  
    
    with col2:
        st.image(img, caption="", use_column_width=True)  

except FileNotFoundError:
    st.error("Imagem não encontrada. Verifique o caminho para a imagem.")

st.header("Construção e Avaliação dos Modelos de Previsão")

st.markdown("""
    Neste estágio da análise, vamos explorar e comparar três diferentes modelos de previsão para determinar qual deles oferece o melhor desempenho para nossa série temporal. Os modelos que serão avaliados incluem:
    
    - **Média Móvel (Moving Average):** Um modelo simples que calcula a média dos valores passados para fazer previsões futuras. A Média Móvel é útil para capturar padrões de curto prazo e suavizar flutuações na série temporal.
    
    - **Modelo ARIMA (AutoRegressive Integrated Moving Average):** O modelo ARIMA é uma das abordagens mais amplamente utilizadas para a modelagem de séries temporais. Ele combina três componentes: Autoregressivo (AR), Diferenciação (I) e Média Móvel (MA). O componente AR utiliza a relação entre uma observação e várias observações anteriores, enquanto o componente MA modela o erro da previsão como uma combinação linear dos erros de previsões anteriores. A diferenciação é utilizada para tornar a série temporal estacionária.
    
    - **Prophet:** Um modelo de previsão avançado desenvolvido pelo Facebook, projetado para lidar com séries temporais que apresentam tendências e sazonalidades. O Prophet é capaz de capturar padrões sazonais e mudanças de tendência, tornando-o uma ferramenta poderosa para previsões de longo prazo.
    """)

st.markdown("""
    **Estacionaridade**

    Antes de iniciarmos a criação dos modelos, é importante ter em mente o conceito de estacionaridade, que é uma característica crucial em séries temporais. A estacionaridade refere-se à propriedade de uma série temporal em que suas características estatísticas, como média, variância e autocorrelação, permanecem constantes ao longo do tempo. Em outras palavras, uma série temporal estacionária não apresenta tendências de longo prazo, sazonalidades ou mudanças estruturais significativas que afetem suas características estatísticas.
    """)

st.markdown("""
    **Teste de Dickey-Fuller**

    O Teste de Dickey-Fuller Aumentado (ADF) é uma ferramenta estatística usada para verificar a estacionaridade de uma série temporal. O teste avalia se uma série temporal possui uma raiz unitária, o que indicaria que a série é não estacionária. A ideia é testar a hipótese nula de que a série tem uma raiz unitária (não estacionária) contra a hipótese alternativa de que a série é estacionária.

    De forma bem resumida, podemos ter duas hipóteses, sendo:
    - **Hipótese Nula (H0):** A série temporal tem uma raiz unitária (não é estacionária).
    - **Hipótese Alternativa (H1):** A série temporal é estacionária.

    Aplicando esse teste na nossa base de dados, podemos dizer que a série temporal analisada não é estacionária. O Teste de Dickey-Fuller Aumentado (ADF) foi utilizado para verificar a estacionaridade da nossa série temporal. A hipótese nula do teste é que a série possui uma raiz unitária, o que indicaria que a série é não estacionária.

    Os resultados obtidos foram os seguintes:
    - **Estatística ADF:** −0.885
    - **Valor-p:** 0.793

    **Valores Críticos:**
    - **1%:** -3.431
    - **5%:** -2.862
    - **10%:** -2.567
    """)

st.markdown("""
    **Média Móvel**

    O modelo da Média Móvel é uma técnica simples e amplamente utilizada para previsão de séries temporais. Seu funcionamento é baseado na ideia de suavizar flutuações e padrões da série temporal para facilitar a identificação de tendências e a realização de previsões.
    """)


imagem_mmoveis = "Img/Medias_Moveis.png"
try:
    img = Image.open(imagem_mmoveis)
    
   
    largura_max = 1000  
    altura_max = 700   
    
    img.thumbnail((largura_max, altura_max))  
    
    
    col1, col2, col3 = st.columns([1, 3, 1])  
    
    with col2:
        st.image(img, caption="", use_column_width=True)  

except FileNotFoundError:
    st.error("Imagem não encontrada. Verifique o caminho para a imagem.")

st.markdown("""
    No gráfico acima, observamos que as médias móveis de 15 e 30 dias apresentam padrões similares à série original de valores de fechamento. Essa observação inicial sugere que as médias móveis fornecem uma representação útil das tendências gerais dos dados. No entanto, uma análise mais detalhada revela que a performance das médias móveis não pode ser plenamente avaliada apenas com base em uma visualização abrangente que cobre um longo período, como de 2021 a 2024.

    Para realizar uma avaliação mais precisa da performance das médias móveis, é crucial focar em um intervalo de tempo mais restrito. Portanto, vamos segmentar e analisar os dados do ano mais recente completado, 2023, a fim de obter uma compreensão mais clara do comportamento das médias móveis e sua eficácia na previsão dos valores futuros. Essa abordagem permitirá uma avaliação mais refinada da capacidade das médias móveis em capturar as nuances e tendências dos dados em um período de tempo mais recente e relevante.
    """)

# Carregar a imagem
imagem_mmoveis2023 = "Img/Medias_Moveis_2023.png"
try:
    img = Image.open(imagem_mmoveis2023)
    
   
    largura_max = 1000  
    altura_max = 700   
    
    img.thumbnail((largura_max, altura_max))  
    
    
    col1, col2, col3 = st.columns([1, 3, 1])  
    
    with col2:
        st.image(img, caption="", use_column_width=True)  

except FileNotFoundError:
    st.error("Imagem não encontrada. Verifique o caminho para a imagem.")

st.markdown("""
    Mesmo após segmentar os dados para o ano de 2023, a análise gráfica revela uma discrepância significativa entre os valores reais de fechamento e as médias móveis de 15 e 30 dias. Essa divergência substancial sugere que o modelo de médias móveis não apresentou um desempenho adequado para o período em questão.

    A falta de alinhamento entre as médias móveis e os valores reais pode ser atribuída a várias razões. Em primeiro lugar, as médias móveis suavizam os dados e podem não capturar adequadamente as flutuações de curto prazo ou os eventos pontuais que influenciam os preços de fechamento. Além disso, a escolha de períodos fixos para as médias móveis pode não ser ideal para todos os contextos ou padrões de dados específicos. A incapacidade das médias móveis em refletir com precisão os valores reais sugere que o modelo pode não estar adequadamente ajustado para captar a dinâmica temporal específica do conjunto de dados de 2023.
    """)

st.markdown("""
    **ARIMA**

    - **Aplicação da Média Móvel:** Iniciamos nossa análise aplicando uma média móvel de 12 meses à série temporal original para suavizar os dados e revelar as tendências subjacentes. Este processo ajudou a eliminar ruídos de curto prazo e a identificar padrões mais estáveis ao longo do tempo.
    
    - **Aplicação do Logaritmo:** Para lidar com a variabilidade dos dados, aplicamos uma transformação logarítmica à série temporal. Isso ajudou a estabilizar a variância e facilitou a identificação de tendências. Em seguida, suavizamos novamente a série logarítmica com uma média móvel de 12 meses.
    
    - **Remoção da Média Móvel e Teste de Estacionaridade:** Após a transformação logarítmica, removemos a média móvel para obter uma série estacionária. Aplicamos o teste de Dickey-Fuller Aumentado (ADF) para confirmar a estacionaridade da série. O teste ADF indicou que a série tratada era estacionária, um requisito fundamental para a modelagem ARIMA.
    
    - **Análise por Diferenciação:** Para reforçar a estacionaridade, aplicamos a diferenciação à série temporal. Calculamos a média móvel e o desvio padrão da série diferenciada para verificar a estacionaridade visualmente. Reaplicamos o teste ADF, que confirmou a estacionaridade da série diferenciada.
    
    - **Análise de Autocorrelação e Autocorrelação Parcial:** Utilizamos as funções de autocorrelação (ACF) e autocorrelação parcial (PACF) para identificar a ordem apropriada do modelo ARIMA. Essas funções nos ajudaram a entender a dependência dos dados ao longo do tempo e a determinar os parâmetros do modelo.
    
    - **Construção do Modelo ARIMA:** Com base nas análises de ACF e PACF, instanciamos e ajustamos um modelo ARIMA (1, 1, 1) aos dados diferenciados. As previsões geradas foram comparadas com os valores reais da série temporal. O MAPE (Erro Absoluto Médio Percentual) calculado foi de 944,72%, indicando que o modelo não capturou adequadamente a dinâmica dos dados. Esse valor alto de MAPE sugere que o modelo ARIMA, nesta configuração, não é adequado para prever essa série temporal específica.
    """)

# Carregar a imagem
imagem_arima = "Img/Modelo_Arima.png"
try:
    img = Image.open(imagem_arima)
    
   
    largura_max = 1000  
    altura_max = 700   
    
    img.thumbnail((largura_max, altura_max))  
    
    
    col1, col2, col3 = st.columns([1, 3, 1])  
    
    with col2:
        st.image(img, caption="", use_column_width=True)  

except FileNotFoundError:
    st.error("Imagem não encontrada. Verifique o caminho para a imagem.")

st.markdown("""
    **💡Projeções Futuras com Prophet💡**

    O Prophet é uma ferramenta desenvolvida pelo Facebook para previsões de séries temporais, oferecendo uma abordagem simples e eficaz para lidar com dados que apresentam padrões complexos. Seu objetivo é proporcionar previsões precisas, mesmo quando os dados têm tendências e sazonalidades variadas.

    O modelo Prophet divide a série temporal em três componentes principais:
    - **Tendência:** Identifica a direção geral dos dados ao longo do tempo, seja de crescimento ou declínio. O Prophet ajusta a tendência com modelos lineares ou logísticos para refletir mudanças ao longo do período analisado.
    - **Sazonalidade:** Captura padrões que se repetem em ciclos regulares, como variações diárias ou anuais. O Prophet permite ajustar sazonalidades diversas, adaptando-se a diferentes tipos de padrões sazonais.
    - **Efeitos de Festividades:** Inclui ajustes para datas especiais e eventos que podem impactar os dados. Isso ajuda a refinar as previsões, considerando influências externas específicas.

    Matematicamente, o modelo Prophet pode ser expresso pela fórmula:
    $$y(t)=g(t)+s(t)+h(t)+ϵ(t)$$
    """)

st.markdown("""
    **Divisão dos Dados para Treinamento e Validação**

    Para avaliar a precisão das previsões geradas pelo modelo Prophet, é essencial dividir o conjunto de dados em dois subconjuntos distintos: um para treinamento e outro para teste. Essa divisão permite que o modelo seja ajustado e treinado com uma parte dos dados, enquanto a outra parte é reservada para validar o desempenho do modelo em dados não vistos durante o treinamento.

    Neste estudo, os dados foram divididos da seguinte forma:
    1. **Conjunto de Treinamento:** A amostra de treinamento foi composta por 90% dos dados originais, resultando em um total de 5.234 registros. Este subconjunto é utilizado para ajustar os parâmetros do modelo e ensinar o Prophet a identificar tendências, sazonalidades e efeitos de festividades.
    2. **Conjunto de Teste:** Os 10% restantes dos dados foram reservados para o conjunto de teste, totalizando 582 registros. Este subconjunto é usado para avaliar a capacidade do modelo de generalizar e fazer previsões precisas em dados que não foram utilizados durante o treinamento.

    A divisão dos dados foi realizada de maneira aleatória, garantindo uma representação adequada dos padrões e variações presentes no conjunto original. A seguir, o modelo Prophet será ajustado com o conjunto de treinamento e validado utilizando o conjunto de teste para verificar sua eficácia e precisão nas previsões.
    """)

st.markdown("""
    **Instanciação e Treinamento do Modelo Prophet**

    Para realizar as previsões, o modelo Prophet foi inicialmente configurado com daily_seasonality=True, permitindo que o modelo capturasse padrões sazonais diários nos dados. Após o treinamento do modelo com o conjunto de dados de treinamento, foi gerado um DataFrame para prever os próximos 30 dias. O gráfico a seguir mostra as previsões feitas pelo modelo Prophet (em azul) comparadas aos valores reais (em vermelho) do conjunto de teste.
    """)
# Carregar a imagem
imagem_prophet = "Img/Modelo_Prophet.png"
try:
    img = Image.open(imagem_prophet)
    
   
    largura_max = 1000  
    altura_max = 700   
    
    img.thumbnail((largura_max, altura_max))  
    
    
    col1, col2, col3 = st.columns([1, 3, 1])  
    
    with col2:
        st.image(img, caption="", use_column_width=True)  

except FileNotFoundError:
    st.error("Imagem não encontrada. Verifique o caminho para a imagem.")

st.markdown("""
    **Métricas de Performance:**
    - **Erro Percentual Absoluto Médio (MAPE):** O MAPE foi de 7,28%, indicando a precisão das previsões em relação aos valores reais.
    - **Acurácia:** A acurácia do modelo foi de 92,72%, refletindo a capacidade do modelo em prever com precisão os dados.

    Em seguida, o modelo Prophet foi ajustado para incorporar feriados nacionais brasileiros. A configuração seasonality_mode='additive' foi utilizada, e o modelo foi treinado com a adição de feriados para captar possíveis efeitos sazonais específicos. O gráfico abaixo mostra as previsões do modelo Prophet com feriados (em azul) em comparação com os valores reais (em vermelho) do conjunto de teste.
    """)

# Carregar a imagem
imagem_prophetferiados = "Img/Modelo_Prophet_Feriados.png"
try:
    img = Image.open(imagem_prophetferiados)
    
   
    largura_max = 1000  
    altura_max = 700   
    
    img.thumbnail((largura_max, altura_max))  
    
    
    col1, col2, col3 = st.columns([1, 3, 1])  
    
    with col2:
        st.image(img, caption="", use_column_width=True)  

except FileNotFoundError:
    st.error("Imagem não encontrada. Verifique o caminho para a imagem.")

st.markdown("""
    **Métricas de Performance:**
    - **Erro Percentual Absoluto Médio (MAPE):** O MAPE foi de 7,29%, indicando uma leve alteração na precisão das previsões com a inclusão dos feriados.
    - **Acurácia:** A acurácia do modelo foi de 92,71%, refletindo a eficácia da inclusão dos feriados na previsão dos dados.

    Ambos os modelos mostram um desempenho robusto, com MAPE e acurácia indicando que o modelo Prophet é eficaz na previsão dos dados. A inclusão de feriados não trouxe uma melhora significativa na precisão das previsões, mas forneceu um ajuste mais refinado para os dados sazonais.
    """)