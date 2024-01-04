function memoize(fn) {
    // Se declara un objeto 'cache' para almacenar los resultados de las llamadas anteriores.
    const cache = {};
    // Se declara un objeto 'callCount' para llevar la cuenta total de llamadas.
    const callCount = { count: 0 };
  
    // Se define la función memoizada que será retornada.
    function memoized(...args) {
      // Se crea una clave única para la combinación de argumentos de la llamada actual.
      const key = JSON.stringify(args);
  
      // Si la clave ya está en el caché, se retorna el resultado almacenado.
      if (cache.hasOwnProperty(key)) {
        return cache[key];
      }
  
      // Si la clave no está en el caché, se llama a la función original con los argumentos.
      const result = fn(...args);
      // Se almacena el resultado en el caché para futuras llamadas con los mismos argumentos.
      cache[key] = result;
      // Se incrementa el contador total de llamadas.
      callCount.count++;
  
      // Se retorna el resultado de la función original.
      return result;
    }
  
    // Se define una función adicional para obtener el número total de llamadas.
    function getCallCount() {
      return callCount.count;
    }
  
    // Se retorna un arreglo que contiene la función memoizada y la función para obtener el contador.
    return [memoized, getCallCount];
  }
  
  // Se definen las funciones originales sum, fib y factorial.
  const sum = (a, b) => a + b;
  const fib = (n) => (n <= 1 ? 1 : fib(n - 1) + fib(n - 2));
  const factorial = (n) => (n <= 1 ? 1 : factorial(n - 1) * n);
  
  // Se crean versiones memoizadas de las funciones sum, fib y factorial.
  const [memoizedSum, getSumCallCount] = memoize(sum);
  const [memoizedFib, getFibCallCount] = memoize(fib);
  const [memoizedFactorial, getFactorialCallCount] = memoize(factorial);
  
  // Se establece el nombre de la función actual (puede ser "sum", "fib" o "factorial").
  const fnName = "sum";
  // Se especifican las acciones a realizar en un conjunto de datos de entrada.
  const actions = ["call", "call", "getCallCount", "call", "getCallCount"];
  const values = [
    [2, 2],
    [2, 2],
    [],
    [1, 2],
    [],
  ];
  
  // Se declara un arreglo para almacenar los resultados de las acciones.
  const output = [];
  
  // Se itera sobre las acciones y se realiza la acción correspondiente para la función actual.
  for (let i = 0; i < actions.length; i++) {
    const action = actions[i];
    const args = values[i];
  
    switch (action) {
      case "call":
        switch (fnName) {
          case "sum":
            output.push(memoizedSum(...args));
            break;
          case "fib":
            output.push(memoizedFib(...args));
            break;
          case "factorial":
            output.push(memoizedFactorial(...args));
            break;
        }
        break;
      case "getCallCount":
        switch (fnName) {
          case "sum":
            output.push(getSumCallCount());
            break;
          case "fib":
            output.push(getFibCallCount());
            break;
          case "factorial":
            output.push(getFactorialCallCount());
            break;
        }
        break;
    }
  }
  
  // Se imprime la salida en la consola.
  console.log(output);