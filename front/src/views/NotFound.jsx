import { Link } from "react-router-dom"

export const NotFound = () => {
    return (
        <section className="container-fluid h-auto d-flex flex-column justify-content-center align-items-center">
           <h1 className="display-1 mt-5">Not Found</h1>
           <Link to='/' className="btn btn-primary"> Volver a Home</Link>
        </section>
    )
}