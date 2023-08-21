const Details = ({ details, children, src }) => {
  return (
    <div className="container text-center">
      <div className="row row-cols-1 row-cols-lg-2 p-3">
        <div className="col my-3">
          <div className="ratio ratio-1x1">
            <img src={src} className="img-fluid object-fit-cover"></img>
          </div>
        </div>
        <div className="col my-3">
          <h1>{details.name}</h1>
          {children}
        </div>
      </div>
      <div className="row row-cols-2 row-cols-md-3 row-cols-lg-6 my-3 p-3 py-5 g-2 border-top border-danger text-danger">
        <div className="col">
          <h5>Name</h5>
          <p>{details.name}</p>
        </div>
        <div className="col">
          <h5>Birth Year</h5>
          <p>{details.birth_year}</p>
        </div>
        <div className="col">
          <h5>Gender</h5>
          <p>{details.gender}</p>
        </div>
        <div className="col">
          <h5>Height</h5>
          <p>{details.height}</p>
        </div>
        <div className="col">
          <h5>Skin Color</h5>
          <p>{details.skin_color}</p>
        </div>
        <div className="col">
          <h5>Eye color</h5>
          <p>{details.eye_color}</p>
        </div>
      </div>
    </div>
  );
};

export default Details;
