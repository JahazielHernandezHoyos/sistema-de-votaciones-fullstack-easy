const dominio = "http://172.18.224.1:8000/"
const apiUrl = dominio+"estadisticas/";
let selectedTopicId;

// Función para hacer una petición GET a la API
async function fetchData(url) {
  try {
    const response = await fetch(url, {
      mode: 'cors',
    });
    const data = await response.json();
    console.log(data)
    return data;
  } catch (error) {
    console.log(error);
  }
}

// Función para mostrar la gráfica con los datos obtenidos
function drawChart(data) {
  const chartData = [    {      x: [data.votos_a_favor, data.votos_en_contra],
      y: ['Votos a favor', 'Votos en contra'],
      type: 'bar',
      orientation: 'h',
      marker: {
        color: ['#36A2EB', '#FF6384']
      }
    }
  ];

  const layout = {
    title: {
      text: data.titulo
    },
    xaxis: {
      title: 'Número de votos',
      automargin: true
    },
    yaxis: {
      automargin: true
    }
  };

  Plotly.newPlot('chart', chartData, layout);
}


// Función para mostrar los temas disponibles
async function showTopics() {
  const topicsContainer = document.getElementById('topics');

  // Obtenemos los temas desde la API
  const topics = await fetchData(dominio+'temas');

  // Creamos una lista con los temas
  const list = document.createElement('ul');
  topics.forEach(topic => {
    const item = document.createElement('li');
    const link = document.createElement('a');
    link.href = '#';
    link.textContent = topic.titulo;
    // add class bootstrap
    link.classList.add('list-group-item', 'list-group-item-action');
    link.addEventListener('click', async () => {
      selectedTopicId = topic.id;
      const data = await fetchData(apiUrl + selectedTopicId);
      drawChart(data);
    });
    item.appendChild(link);
    list.appendChild(item);
  });

  topicsContainer.appendChild(list);
}

// Función principal para mostrar los temas y la gráfica
async function main() {
  // Obtenemos los temas desde la API
  const topics = await fetchData(dominio+'temas');
  // Obtenemos el ultimo elemento de la lista de temas
  const lastTopic = topics[topics.length - 1];
  console.log(lastTopic)
  // Obtenemos los datos del último tema
  const data = await fetchData(apiUrl + lastTopic.id);
  // Mostramos la gráfica
  drawChart(data);
  await showTopics();
}

// Llamada a la función principal
main();

