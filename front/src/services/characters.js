const getCharacters = async (setCharacter) => {
  const response = await fetch("https://www.swapi.tech/api/people");
  const data = await response.json();
  setCharacter(data.results);
};

export default getCharacters;
