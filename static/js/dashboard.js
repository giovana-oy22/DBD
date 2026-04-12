async function getJson(url) {
  const response = await fetch(url, { headers: { Accept: "application/json" } });
  if (!response.ok) {
    throw new Error("Falha ao carregar " + url);
  }
  return response.json();
}

function createCard(container, title, subtitle, meta) {
  const template = document.getElementById("card-template");
  const node = template.content.cloneNode(true);

  node.querySelector(".card-title").textContent = title || "Sem titulo";
  node.querySelector(".card-subtitle").textContent = subtitle || "";
  node.querySelector(".card-meta").textContent = meta || "";

  container.appendChild(node);
}

function showEmpty(container, text) {
  container.innerHTML = "";
  const p = document.createElement("p");
  p.className = "empty";
  p.textContent = text;
  container.appendChild(p);
}

function showError(container, text) {
  container.innerHTML = "";
  const p = document.createElement("p");
  p.className = "error";
  p.textContent = text;
  container.appendChild(p);
}

async function loadRestaurantes() {
  const box = document.getElementById("restaurantes");
  box.innerHTML = "";

  try {
    const data = await getJson("/api/restaurantes/");
    if (!data.length) {
      showEmpty(box, "Nenhum restaurante cadastrado.");
      return;
    }

    data.forEach((r) => {
      createCard(
        box,
        r.nome,
        r.endereco,
        "Lat " + r.latitude + " | Lon " + r.longitude,
      );
    });
  } catch (error) {
    showError(box, "Erro ao carregar restaurantes.");
  }
}

async function loadProdutos() {
  const box = document.getElementById("produtos");
  box.innerHTML = "";

  try {
    const data = await getJson("/api/produtos/");
    if (!data.length) {
      showEmpty(box, "Nenhum produto cadastrado.");
      return;
    }

    data.forEach((p) => {
      createCard(
        box,
        p.nome,
        "Restaurante: " + p.restaurante,
        "Preco: R$ " + Number(p.preco).toFixed(2),
      );
    });
  } catch (error) {
    showError(box, "Erro ao carregar produtos.");
  }
}

async function loadPedidos() {
  const box = document.getElementById("pedidos");
  box.innerHTML = "";

  try {
    const data = await getJson("/api/pedidos/");
    if (!data.length) {
      showEmpty(box, "Nenhum pedido cadastrado.");
      return;
    }

    data.forEach((p) => {
      createCard(
        box,
        "Pedido #" + p.id,
        "Cliente: " + p.cliente + " | Restaurante: " + p.restaurante,
        "Total: R$ " + Number(p.total).toFixed(2),
      );
    });
  } catch (error) {
    showError(box, "Erro ao carregar pedidos.");
  }
}

async function initpainel() {
  await Promise.all([loadRestaurantes(), loadProdutos(), loadPedidos()]);
}

initpainel();
