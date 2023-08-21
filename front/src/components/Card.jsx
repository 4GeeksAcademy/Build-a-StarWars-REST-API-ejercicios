import React, { useEffect } from "react";
import { useState, useMemo } from "react";
import useAppContext from "../context/AppContext";
import { Link } from "react-router-dom";
export const Card = ({ title, children, id, url, src }) => {
  const [likeStatus, setLikeStatus] = useState(false);
  const { actions } = useAppContext();

  const switchStatus = (e) => {
    setLikeStatus((prev) => {
      return !prev;
    });
    return actions.handleAddFavoritesList(e);
  };

  

  const color = useMemo(() => {
    return likeStatus ? "text-danger" : "text-warning";
  }, [likeStatus]);

  return (
    <div className="card col-10 col-md-6 col-lg-2 mx-3 p-0">
      <img className="object-fit-contain" src={src} alt="img-default" />

      <div className="card-body">
        <h2 className="card-title">{title}</h2>
        {children}
      </div>
      <div className="card-footer d-flex justify-content-around">
        <Link className="btn btn-outline-primary" to={url}>
          Learn More!
        </Link>
        <button id={id} className={`btn btn-outline-warning ${color} p-0`}>
          <i
            id={id}
            className={` fa-solid fa-heart ${color} px-2 py-2 ${title}`}
            onClick={switchStatus}
          ></i>
        </button>
      </div>
    </div>
  );
};
