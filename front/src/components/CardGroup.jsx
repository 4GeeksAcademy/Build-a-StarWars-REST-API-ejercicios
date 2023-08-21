const CardGroup = ({ children }) => {
  return (
    <div className="row d-flex flex-nowrap overflow-x-scroll w-100 h-25 p-3">
      {children}
    </div>
  );
};

export default CardGroup;
