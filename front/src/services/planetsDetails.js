const getPlanetsDetails = async (planetID) => {
  const response = await fetch(
    `https://www.swapi.tech/api/planets/${planetID}`
  );
  const data = await response.json();
  const planet = await data.result.properties;
  return planet;
};

export default getPlanetsDetails;
