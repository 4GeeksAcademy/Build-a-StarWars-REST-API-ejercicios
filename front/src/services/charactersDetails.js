const getCharactersDetails = async (characterID) => {
  const response = await fetch(
    `https://www.swapi.tech/api/people/${characterID}`
  );
  const data = await response.json();
  const character = await data.result.properties;
  return character;
};

export default getCharactersDetails;
