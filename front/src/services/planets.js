const getPlanets = async (setPlanets) => {
  const response = await fetch("https://www.swapi.tech/api/planets");
  const data = await response.json();
  setPlanets(data.results);
};

export default getPlanets;
