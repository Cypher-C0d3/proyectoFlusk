const seleccionModo = $(`#modo-oscuro`);
console.log(seleccionModo);

// Iterar sobre cada elemento del dropdown
seleccionModo.on(`click`, function (event) {
  const selectedValue = event.target.id;
  if (selectedValue == "oscuro") {
    document.documentElement.setAttribute("data-bs-theme", "dark");
  } else if (selectedValue == "claro") {
    document.documentElement.setAttribute("data-bs-theme", "light");
  }
});
