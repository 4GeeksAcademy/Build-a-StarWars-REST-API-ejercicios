import useAppContext from "../context/AppContext";
import { useNavigate } from "react-router-dom";

export const Dashboard = () => {
  const { actions, store } = useAppContext();

  return (
    <div className="container mt-5">
      <h1>Area Privada</h1>
      <p>Mi nickname</p>
      <p>{store.userData.nickname}</p>
      <p>Mi email</p>
      <p>{store.userData.email}</p>
      <button
        className="btn btn-danger"
        onClick={() => {
          actions.setIsLogin(false);
          actions.setToken(null);
        }}
      >
        Logaut
      </button>
    </div>
  );
};
