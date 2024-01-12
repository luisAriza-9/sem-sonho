
const main = document.querySelector("main");


//prueba
// UTILIZANDO ASYNC AWAIT
async function pokeApi(numPers) {
    const url = `https://rickandmortyapi.com/api/character/${numPers}`;

    const respuesta = await fetch(url);

    //si la respuesta no fue exitosa
    if (!respuesta.ok)
        throw new Error("Error.  no existe ningun personaje ");

    const json = await respuesta.json();
    // retornar el link de la imagen del personaje 
    return [json.sprites.front_default, json.name, json.id];
}
RickyMortiApi("1")
    .then(nombre => console.log(nombre))
    .catch(error => console.error(error.message));

//funcion que se ejecuta inmediatamente 
 
async function siguiente() {
    const poke1 = Math.floor(Math.random() * (1000 - 0 + 1) + 0)
    const poke2 = Math.floor(Math.random() * (1000 - 0 + 1) + 0)
    
    try {
        let [Hp, Attack, Defense, Speed] = await pokeApi(`${poke1}`);
        let  = await pokeApi(`${poke2}`);
        cuerpoTabla.innerHTML = `
    <tr class="Pokemons">
        <td><img src="${listaPokemon[0]}"</td>
        <td><img src="${listaPokemon2[0]}"</td>
    <tr class="Pokemons">
        <td>${listaPokemon[2]}</td>
        <td>${listaPokemon2[2]}</td>
    <tr class="Pokemons">    
        <td>${listaPokemon[1]}</td>
        <td>${listaPokemon2[1]}</td>
    </tr>`

    } catch (error) {
        console.error(error.message);
    
    }
    
}

siguiente()