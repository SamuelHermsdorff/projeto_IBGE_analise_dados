/* =====================================================
   CARREGAMENTO DOS DADOS
===================================================== */

async function carregarDados() {
  try {
    const caminhoDados = window.location.hostname.includes("github.io")
      ? "/Projeto-IBGE-Analise-Dados/dados/dados_ibge.json"
      : "../dados/dados_ibge.json";

    const resposta = await fetch(caminhoDados);

    if (!resposta.ok) {
      throw new Error("Não foi possível carregar os dados do IBGE.");
    }

    const dados = await resposta.json();

    atualizarIndicadores(dados.indicadores);

    criarGraficoEstados(dados.graficos.municipios_por_estado);

    criarGraficoRegioes(dados.graficos.municipios_por_regiao);

    preencherTabela(dados.graficos.municipios_por_estado);
  } catch (erro) {
    console.error("Erro ao carregar os dados:", erro);
  }
}

/* =====================================================
   INDICADORES
===================================================== */

function atualizarIndicadores(indicadores) {
  const totalMunicipios = document.getElementById("total-municipios");

  const estadoMaior = document.getElementById("estado-maior");

  const quantidadeMaior = document.getElementById("quantidade-maior");

  const estadoMenor = document.getElementById("estado-menor");

  totalMunicipios.textContent = indicadores.total_municipios;

  estadoMaior.textContent = indicadores.estado_maior_quantidade.nome;

  quantidadeMaior.textContent = indicadores.estado_maior_quantidade.quantidade;

  estadoMenor.textContent = indicadores.estado_menor_quantidade.nome;
}

/* =====================================================
   GRÁFICO POR ESTADO
===================================================== */

function criarGraficoEstados(dados) {
  const canvas = document.getElementById("grafico-estados");

  const estados = dados.map((item) => item.estado);

  const quantidades = dados.map((item) => item.quantidade);

  new Chart(canvas, {
    type: "bar",

    data: {
      labels: estados,

      datasets: [
        {
          label: "Quantidade de municípios",

          data: quantidades,

          borderWidth: 1,
        },
      ],
    },

    options: {
      responsive: true,

      maintainAspectRatio: false,

      plugins: {
        legend: {
          display: false,
        },
      },

      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });
}

/* =====================================================
   GRÁFICO POR REGIÃO
===================================================== */

function criarGraficoRegioes(dados) {
  const canvas = document.getElementById("grafico-regioes");

  const regioes = dados.map((item) => item.regiao);

  const quantidades = dados.map((item) => item.quantidade);

  new Chart(canvas, {
    type: "doughnut",

    data: {
      labels: regioes,

      datasets: [
        {
          label: "Municípios por região",

          data: quantidades,

          borderWidth: 1,
        },
      ],
    },

    options: {
      responsive: true,

      maintainAspectRatio: false,
    },
  });
}

/* =====================================================
   TABELA
===================================================== */

function preencherTabela(dados) {
  const tabela = document.getElementById("tabela-estados");

  tabela.innerHTML = "";

  dados.forEach((item) => {
    const linha = document.createElement("tr");

    const estado = document.createElement("td");

    const quantidade = document.createElement("td");

    estado.textContent = item.estado;

    quantidade.textContent = item.quantidade;

    linha.appendChild(estado);

    linha.appendChild(quantidade);

    tabela.appendChild(linha);
  });
}

/* =====================================================
   INICIALIZAÇÃO
===================================================== */

carregarDados();
