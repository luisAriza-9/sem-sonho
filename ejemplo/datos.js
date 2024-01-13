fetch("http://localhost:300/trainers", {
  method: "POST",
  body: JSON.stringify({
    "id": "3",
    "nombres": "luis",
    "apellidos": "ariza",
    "especialidad": "fullStack"
  }),
  headers: {
    "Content-Type": "application/json; charset=UTF-8",
  },
})
  .then(response => response.json())
  .then(json => console.log(json))
  .catch(error => console.error("Error!!!: " + error));