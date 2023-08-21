import { useEffect } from "react";
import useAppContext from "../context/AppContext";
import { useNavigate } from "react-router-dom";

export const NeedValidation = ({ children }) => {
  const { actions, store } = useAppContext();
  const navigate = useNavigate();

  useEffect(() => {
    if (store.isLogin) {
      return <div>{children}</div>;
    } else {
      navigate("/login");
    }
  },[])

 
};
