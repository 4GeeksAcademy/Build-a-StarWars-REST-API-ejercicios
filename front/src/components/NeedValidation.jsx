import { useEffect } from "react";
import useAppContext from "../context/AppContext";
import { useNavigate } from "react-router-dom";

export const NeedValidation = ({ children }) => {
  const { store } = useAppContext();
  const navigate = useNavigate();

  useEffect(() => {
    if (!store.isLogin) {
      navigate("/login");
    }
  }, [store.isLogin, navigate]);

  // Renderizar el contenido solo si está autenticado
  return store.isLogin ? <div>{children}</div> : null;
};
