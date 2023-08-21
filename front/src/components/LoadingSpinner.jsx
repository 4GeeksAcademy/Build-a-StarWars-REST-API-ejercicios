const LoadingSpinner = () => {
  return (
    <>
      <div className="row gap-3 vh-100 flex flex-col justify-content-center align-content-center">
        <div className="spinner-border" role="status"></div>
        <h1 className="text-center">Loading...</h1>
      </div>
    </>
  );
};

export default LoadingSpinner;
