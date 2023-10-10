PERGUNTAS EM ENTREVISTAS DE FULLSTACK.

1.
Como um desenvolvedor Full Stack, nos diga quais são as tecnologias que você mais gosta de utilizar e por quais razões.

Esconder resposta
Esta pergunta em entrevistas de desenvolvedor full stack visa avaliar seu conhecimento e o quão proficiente você é com diferentes tipos de tecnologias. Ao responder, certifique-se de adicionar sua experiência pessoal com as linguagens. Em uma entrevista de desenvolvedor full stack, falar sobre seus projetos te ajudará bastante.

Lembre-se, estas são algumas das competências que você deve mostrar com sua resposta:

Linguagens de programação: um desenvolvedor full stack deve dominar diversas linguagens de programação, como Java, Python, Ruby, C++, etc. Com base na linguagem de programação, você também deve estar familiarizado com várias abordagens para planejar, desenvolver, implementar e testar o projeto que utiliza tais linguagens.
Front-end: também é necessário que você conheça algumas tecnologias front-end, como HTML5, CSS3, Angular e outras. Compreender as bibliotecas de terceiros, como jQuery, será um bom diferencial que vale a pena ser mostrado.
Frameworks: proficiência com diferentes frameworks de desenvolvimento , como Spring, Spring Boot, MyBatis, Django, Hibernate e outros, é fundamental.
Bancos de dados: Você deve compreender pelo menos um tipo de banco de dados. Estar familiarizado com MySQL, Oracle ou MongoDB, já é o suficiente para demonstrar suas capacidades.
Habilidade de design: Experiência com práticas comuns de design, como design de interface do usuário e UX, é obrigatório para desenvolvedores e te pode te ajudar a se destacar da competição.
2.
Quais as diferenças entre MVC e MVP? No que são similares? Onde diferem?

Esconder resposta
Model View Controller (MVC)

Model View Controller, ou MVC, é um paradigma de arquitetura de software para aplicações da Java Enterprise. Ele divide o programa em três partes lógicas: Model, View e Controller (Modelo, Visualização e Controlador). Isto isola a camada de visualização (view component) da lógica comercial específica para a aplicação (model component).

Dados e lógica ficam contidos nos componentes do Modelo. Objetos do Modelo (model objects) são mostrados na interface do usuário com o componente de Visualização. O Controller (Controlador) aceita inputs e chama objetos do modelo no mapeamento do handler. Isto transfere os objetos do modelo para visualizações e mostra os resultados dentro da camada de visualização (view layer).

Model View Presenter (MVP)

MVP é a sigla para Model View Presenter. Este modelo de arquitetura de software foi inspirado pelo MVC. Ele adiciona uma camada extra ao padrão da arquitetura de software (conhecido como indirection) que divide o View e Controller em View e Presenter. O Presenter assume a posição do Controller. No MVC, ele está no mesmo nível que o View. Isto inclui a lógica comercial da UI no View. O Presenter recebe chamados diretamente do View. Mantendo, assim, as ações (eventos) que acontecem entre o View e o Model. O View não é diretamente comunicado pelo Presenter, ele conecta o usuário através da interface.

Tratando-se das similaridades e diferenças do MVC e MVP, eles não são nem um pouco parecidos. A principal diferença entre os dois padrões de arquitetura de software é que com o MVC os dados do Model não são enviados para o View através do Controller. Ele simplesmente dá instruções para o View obter os dados do Model.

Já no MVP, as camadas View e Model estão conectadas. Os dados do Model são recebidos pelo Presenter, que então os transmite para o View e gera a visualização. Outra distinção importante é que o MVC é comumente utilizado em frameworks para web, enquanto o MVP é mais utilizado no desenvolvimento de apps.

3.
O que é tempo de carregamento? Diga 5 modos diferentes para diminuir o load time de uma aplicação web.

Esconder resposta
O tempo médio que uma página leva para carregar na tela é chamado de tempo de carregamento da página (load time). Ele é calculado desde o início (quando você clica em um link de página ou o insere na barra de endereço) até o fim (quando a página é totalmente carregada no navegador).

Existem muitas maneiras de reduzir e otimizar o tempo de carregamento de um aplicativo. Algumas delas são:

Otimizar o tamanho e o formato das imagens;
Evitar redirecionamentos;
Minimizar as solicitações HTTP;
Colocar a referência ao script na parte inferior (footer);
Colocar JavaScript e CSS externamente.
4.
Como funciona a função callback do JavaScript?

Esconder resposta
A função callback é um parâmetro para outra função. A função Callback é executada dentro da função para a qual ela foi inserida. Você pode usar as funções Callback no JavaScript de forma sincronizada ou assíncrona. As interfaces de programação de aplicações do Node são, todas, criadas para suportar callback.

5.
Como funciona a two-phase commit (2PC) em um banco de dados?

Esconder resposta
Quando uma circunstância de erro acontece, a two-phase commit (2PC) é uma funcionalidades de processamento de sistemas que permite que os bancos de dados sejam restaurados para o estado anterior ao erro.

6.
Como a implantação verde/azul é diferente da implantação rolling?

Esconder resposta
Em uma implantação Azul/Verde, há dois ecossistemas completos. O ambiente Azul é o operacional naquele momento e o Verde é o ambiente para o qual você quer atualizar. Quando você faz a mudança do ambiente Azul para o Verde, o tráfego é direcionado para o novo ambiente Verde. Você pode, então, deletar ou guardar seu ambiente Azul como backup até que o ambiente Verde esteja completamente formado.

Em uma implantação do tipo “rolling”, há apenas um ambiente completo. Antes de realocar para outro subset, o código é implantado em um subset das mesmas instâncias do ambiente.

7.
Quais são algumas desvantagens do GraphQL?

Esconder resposta
Você deve transmitir as queries a partir do cliente; você pode enviar strings, se deseja caching e maior conveniência, mas precisará usar uma biblioteca do cliente;
Você precisa definir os schemas antes de implementá-los, logo precisará de mais esforço antes de ver qualquer resultado;
Você deve ter um endpoint do GraphQL no seu servidor, o que significa que você precisará se familiarizar com mais bibliotecas;
Queries do GraphQL exigem mais espaço do que visitar uma API REST;
O servidor precisará realizar processamento adicional para realizar parsing do query e checar os argumentos.
8.
Null e undefined são a mesma coisa no Java Script?

Esconder resposta
Não, null não é nem um pouco parecido com undefined no JavaScript.

Null: é um valor que foi atribuído à uma variável. Quando usado com o operador typeof, o resultado é um objeto. Como o programador utiliza o null para representar uma variável sem valor, nunca devemos definir uma variável como null. Vale a pena mencionar que JavaScript nunca definirá um valor como null, por padrão.

Undefined: é quando uma variável é declarada, mas não lhe é dada um valor. É possível que a variável nem exista. Quando o operador typeof é usado, o resultado torna-se undefined. No JSON, isto não é válido.

9.
O que você entende por MEAN Stack?

Esconder resposta
O MEAN stack é um framework de código aberto e user-friendly do JavaScript, que serve para criar páginas e aplicativos online dinâmicos. O MEAN stack tem a vantagem de rodar precisando de apenas uma linguagem em todas as camadas da aplicação, a JavaScript, fazendo com que seja um stack mais eficiente.

O MEAN stack é composto pelas seguintes tecnologias:

Banco de dados: MongoDB
Framework web: Express.js
Framework front-end: AngularJS
Plataforma de servidor: Node.js
10.
Como evitar um deadlock no Java?

Esconder resposta
O deadlock acontece quando duas ou mais threads tentam acessar os mesmos recursos simultaneamente no Java. Estas threads, eventualmente, não conseguirão acessar os recursos e ficarão em status de espera indefinidamente.

Há diversos modos para evitar um deadlock. Alguns deles são:

Evitar locks desnecessários: Devemos apenas utilizar locks em membros que precisam deles. Locks usados desnecessariamente levam a um impasse. É sugerido que você utilize uma estrutura de dados que esteja liberada. Mantenha seu código o mais “lock-free” possível. Invés de utilizar uma ArrayList sincronizada, considere usar uma ConcurrentLinkedQueue.

Evitar locks aninhados: Para evitar deadlocks, uma técnica é prevenir locks aninhados. Locks aninhados ocorrem quando uma thread adquire vários locks de maneira aninhada. Se uma thread já recebeu uma trava, deve-se ter cuidado ao atribuir travas adicionais à mesma thread ou a outras threads.

Utilizar o método Thread.join(): Podemos ter um deadlock se duas threads esperarem ao mesmo tempo e eternamente que a outra termine. É recomendável que o join seja utilizado com o máximo de tempo que você deseja que uma thread espere pela outra para finalizar o processo.

Utilizar a ordenação de locks: Cada lock deve ter um valor numérico associado ao mesmo. Obter o lock com menor valor numérico antes dos com valores numéricos maiores poderá evitar o deadlock.

Usar um Time-out para os locks: Podemos especificar o tempo para que uma thread obtenha um lock. Se a thread falhar ao obter um lock, ela deverá esperar um tempo estipulado anteriormente antes de tentar adquirir um lock novamente.

11.
Qual é a diferença entre o desenvolvimento 'front-end' e 'back-end'?

Esconder resposta
Front-end e back-end são dois termos comuns usados na indústria de desenvolvimento de software para se referir a diferentes partes de um aplicativo ou sistema.

O desenvolvimento front-end é responsável por construir e projetar a interface voltada para o usuário, o que inclui layout e aparência, mas também a interação do usuário com o aplicativo. O desenvolvedor front-end trabalha principalmente com tecnologias web, como HTML, CSS e JavaScript, para criar páginas da web e aplicativos que possam ser acessados ​​por meio de navegadores.

Já o desenvolvimento back-end é responsável pela lógica do aplicativo e do servidor, geralmente trabalhando com bancos de dados, scripts e linguagens de programação para lidar com solicitações de usuários, autenticação, segurança e outros aspectos do aplicativo que não são diretamente visíveis para o usuário final.

12.
Quais são os benefícios de usar um framework no desenvolvimento full stack?

Esconder resposta
O uso de um framework no desenvolvimento full stack oferece diversos benefícios, tais como:

Acelera o desenvolvimento: frameworks fornecem componentes e funcionalidades prontas, permitindo que os desenvolvedores possam se concentrar em soluções específicas para o problema em questão, ao invés de ter que reescrever código genérico.
Melhora a manutenção: frameworks têm estruturas e padrões definidos, o que torna a manutenção do código mais fácil e menos propensa a erros.
Segurança: muitos frameworks incluem recursos de segurança integrados, como proteção contra injeção de SQL e ataques CSRF, o que ajuda a proteger a aplicação de vulnerabilidades.
Comunidade: frameworks populares têm grandes comunidades de desenvolvedores e usuários, o que significa que há muitos recursos disponíveis, como documentação, tutoriais, fóruns de suporte, etc.
Escalabilidade: frameworks geralmente são projetados com escalabilidade em mente, permitindo que as aplicações cresçam de maneira organizada e gerenciável.
Padronização: frameworks fornecem padrões e convenções para o desenvolvimento, o que ajuda a manter o código limpo e organizado, além de facilitar o trabalho em equipe.
13.
Como você melhora os recursos de segurança de um site com desenvolvimento full stack?

Esconder resposta
Há várias práticas e técnicas que podem ser usadas para melhorar os recursos de segurança de um site desenvolvido com tecnologias full stack. Algumas delas são:

Validação de entrada: Certificar-se de validar todas as entradas de dados para evitar ataques de injeção de SQL, XSS, CSRF e outros tipos de ataques de injeção de código. Isso pode ser feito por meio de filtragem, validação e sanitização de entrada de dados.
Autenticação e autorização: Implementar um sistema de autenticação seguro, como o uso de criptografia forte para senhas, hashes salgados, tokens de autenticação e gerenciamento adequado de sessões. Além disso, verificar se apenas usuários autorizados têm acesso a recursos confidenciais e sensíveis, definindo papéis e permissões apropriados.
Proteção contra vulnerabilidades conhecidas: Manter as bibliotecas e frameworks utilizados atualizados, pois as atualizações geralmente incluem correções de vulnerabilidades de segurança conhecidas. Além disso, verificar se o código não contém vulnerabilidades conhecidas de segurança.
Gerenciamento de erros e logs: Certificar-se de gerenciar adequadamente as exceções e erros, evitando a exposição de informações sensíveis ao usuário. Isso pode ser feito através do uso de tratamento de exceções, registro de erros em logs e monitoramento de atividades suspeitas.
Proteção contra ataques de DDoS: Implementar técnicas de proteção contra ataques de negação de serviço distribuído (DDoS), como limitação de taxa, filtragem de tráfego malicioso e balanceamento de carga.
Criptografia de dados: Certificar-se de que as informações confidenciais, como senhas e dados pessoais, sejam criptografadas tanto em trânsito quanto em repouso. Isso pode ser feito usando protocolos seguros, como SSL/TLS e HTTPS.
Testes de segurança: Realizar regularmente testes de segurança no aplicativo, incluindo testes de penetração e varreduras de vulnerabilidades. Isso pode ajudar a identificar quaisquer vulnerabilidades de segurança antes que elas possam ser exploradas por um invasor.
14.
Qual é a diferença entre Git Pull e Git Merge?

Esconder resposta
Tanto o comando git pull quanto o git merge são usados para mesclar alterações de um ramo (branch) para outro, mas eles trabalham de maneiras diferentes.

O comando git pull mescla as alterações de um branch remoto para o branch local atual, e faz isso em duas etapas: primeiro ele executa o comando git fetch para buscar as alterações mais recentes do branch remoto e em seguida, ele executa o comando git merge para mesclar essas alterações com o branch local atual.

O comando git merge é usado para mesclar as alterações de um branch para outro branch local, sem envolver um branch remoto. Quando o comando git merge é executado, o Git combina as alterações do branch de origem (source) no branch de destino (destination).

Procurando por trabalhos remotos em empresas dos EUA?
Trabalhe em empresas da Fortune 500 e startups em rápido crescimento do conforto da sua casa.

Candidate-se Agora
CONCLUSÃO
Se você chegou até aqui, agora pode responder ou formular várias novas perguntas para uma entrevista bem-sucedida de desenvolvedor full stack. As perguntas acima cobriram vários tópicos, alguns fundamentais e outros avançados, que podem te ajudar na hora de uma entrevista de desenvolvedor full stack. No entanto, este não é o fim. Apenas saber como responder ou preparar perguntas para entrevistas não é suficiente, pois a segunda ferramenta mais importante necessária em seu arsenal são habilidades interpessoais e de gerenciamento de equipes, também conhecidas como soft skills.

Como candidato à procura de um trabalho online de desenvolvedor full stack, para maximizar suas chances de superar qualquer entrevista técnica, você precisa ter certeza de que está pronto para responder quaisquer perguntas sobre suas soft skills. Para isso, é bom mencionar seus projetos, sejam eles colaborativos ou pessoais, e falar sobre como você administra seu tempo e sua equipe, ou o trabalho junto a uma.

Agora que você está pronto para responder às perguntas técnicas da entrevista do desenvolvedor full stack e às perguntas sobre habilidades interpessoais, inscreva-se na Turing e garanta uma vaga de trabalho remoto. Se você é um desenvolvedor brasileiros que deseja trabalhar para empresas dos EUA, enquanto colabora com os melhores profissionais do setor e recebe em dólar, candidate-se hoje mesmo.

Agora, se você é um recrutador procurando expandir a sua equipe com um talentosos desenvolvedor full stack, a Turing pode te ajudar. Entre em contato conosco e tenha acesso a alguns dos melhores programadores remotos do mundo.