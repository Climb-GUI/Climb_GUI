import React from "react";
import { Link } from "react-router-dom";

function NavBar() {
	return (
		<nav className="bg-gray-800 shadow-md">
			<div className="container mx-auto flex justify-between items-center py-3 px-4">
				<Link to="/" className="text-white text-2xl font-bold">
					Climb GUI
				</Link>
				<ul className="flex space-x-6">
					<li>
						<Link
							to="/estimate"
							className="text-white text-lg hover:text-blue-400 transition duration-300"
						>
							Estimate
						</Link>
					</li>
				</ul>
			</div>
		</nav>
	);
}

export default NavBar;
