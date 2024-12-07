$('.form-control').select2({
    placeholder: "Seleccione una opción",
    allowClear: true,
    width: '100%',
    minimumInputLength: 1,  // Mínimo de caracteres para empezar a buscar
    language: {
        noResults: function() {
            return "No se encontraron resultados";
        }
    }
});
