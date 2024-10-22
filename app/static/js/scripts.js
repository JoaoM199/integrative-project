function validateInput(input) {
    document.querySelector('form').addEventListener('submit', function(event) {
        event.preventDefault();
        let valores = document.getElementById('sequencia').value.split(',').map(Number);
        console.log(valores);
      });      
}