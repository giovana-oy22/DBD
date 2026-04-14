let todosProdutos = [];
let todosRestaurantes = [];

async function getJson(url) {
  const response = await fetch(url);
  return response.json();
}

function createCard(container, title, subtitle, meta) {
  const template = document.getElementById("card-template");
  const node = template.content.cloneNode(true);

  node.querySelector(".card-title").textContent = title;
  node.querySelector(".card-subtitle").textContent = subtitle;
  node.querySelector(".card-meta").textContent = meta;

  container.appendChild(node);
}

function renderProdutos(lista) {
  const box = document.getElementById("produtos");
  box.innerHTML = "";

  if (!lista.length) {
    box.innerHTML = "<p>Nenhum produto encontrado</p>";
    return;
  }

  lista.forEach(p => {
    createCard(
      box,
      p.nome,
      "Restaurante: " + p.restaurante,
      "R$ " + Number(p.preco).toFixed(2)
    );
  });
}

function renderRestaurantes(lista) {
  const box = document.getElementById("restaurantes");
  box.innerHTML = "";

  if (!lista.length) {
    box.innerHTML = "<p>Nenhum restaurante encontrado</p>";
    return;
  }

  lista.forEach(r => {
    createCard(
      box,
      r.nome,
      r.endereco,
      "Lat: " + r.latitude + " | Lon: " + r.longitude
    );
  });
}

async function loadProdutos() {
  const data = await getJson("/api/produtos/");
  todosProdutos = data;
  renderProdutos(data);
}

async function loadRestaurantes() {
  const data = await getJson("/api/restaurantes/");
  todosRestaurantes = data;
  renderRestaurantes(data);
}

async function loadPedidos() {
  const data = await getJson("/api/pedidos/");
  const box = document.getElementById("pedidos");
  box.innerHTML = "";

  data.forEach(p => {
    createCard(
      box,
      "Pedido #" + p.id,
      p.cliente + " | " + p.restaurante,
      "Total: R$ " + Number(p.total).toFixed(2)
    );
  });
}

function configurarBuscaProduto() {
  const input = document.getElementById("busca-produto");

  input.addEventListener("input", () => {
    const termo = input.value.toLowerCase();

    const filtrados = todosProdutos.filter(p =>
      p.nome.toLowerCase().includes(termo)
    );

    renderProdutos(filtrados);
  });
}

function configurarBuscaRestaurante() {
  const input = document.getElementById("busca-restaurante");

  input.addEventListener("input", () => {
    const termo = input.value.toLowerCase();

    const restaurantesFiltrados = todosRestaurantes.filter(r =>
      r.nome.toLowerCase().includes(termo)
    );

    const produtosFiltrados = todosProdutos.filter(p =>
      p.restaurante.toLowerCase().includes(termo)
    );

    renderRestaurantes(restaurantesFiltrados);
    renderProdutos(produtosFiltrados);
  });
}

async function init() {
  await Promise.all([
    loadProdutos(),
    loadRestaurantes(),
    loadPedidos()
  ]);

  configurarBuscaProduto();
  configurarBuscaRestaurante();
}

init();