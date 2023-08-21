import { useParams } from "react-router";
import useAppContext from "../context/AppContext";

import Planets from "../components/Planets";
import LoadingSpinner from "../components/LoadingSpinner";

export const PlanetsView = () => {
  const params = useParams();
  const { actions, store } = useAppContext();

  const planet = store.planets.find((planet) => planet.uid === params.id);
  const details = store.planetsDetails.find(
    (detail) => detail.name === planet.name
  );

  if (store.loading) {
    return <LoadingSpinner />;
  }

  return (
    <Planets
      details={details}
      src={`https://starwars-visualguide.com/assets/img/planets/${planet.uid}.jpg`}
    >
      <p>
        Voluptate laborum laborum adipisicing occaecat cupidatat aliqua Lorem
        tempor do nulla. Magna pariatur minim aliqua esse pariatur Lorem
        cupidatat aute amet. Exercitation ipsum eiusmod cupidatat ex cillum duis
        reprehenderit exercitation sit cupidatat ad magna elit laboris. Quis
        nisi laborum ea nulla proident commodo. Cillum officia magna excepteur
        ullamco labore. Magna Lorem enim amet officia. Ea eu incididunt
        excepteur quis ipsum ipsum veniam consequat reprehenderit laborum
        ullamco.
      </p>
    </Planets>
  );
};
