export const Dashboard = () => {
  return (
    <div className="container mt-5">
      <h1 className="text-center display-4 fw-semibold">User Space</h1>
      <section className="row w-100 d-flex gap-2">
        <div className="col-4 card p-4 shadow">
          <ul className="mt-5">
            <li>nickname</li>
            <li>email</li>
          </ul>

          <article className="card shadow w-75 bg-primary text-white d-flex flex-columns align-items-center justify-content-center mt-5">
            <p className="fs-4 fw-semibold text-center m-0">Total Favoritos</p>
            <span className="display-6 fw-semibold text-center">8</span>
          </article>
        </div>

        <div className="col-7 card shadow p-3">
          <article className="card col-4">
            <img className="img-card-top" src="" alt="img" />
            <div className="card-body">
              <p className="car-text">
                Lorem ipsum, dolor sit amet expedita cupiditate unde odio.
              </p>
            </div>
          </article>
        </div>
      </section>
    </div>
  );
};
