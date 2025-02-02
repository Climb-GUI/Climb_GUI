import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import HomePage from "./Homepage";
import Estimate from "./Estimate";

function App() {
	return (
		<Router>
			<Routes>
				<Route path="/" element={<HomePage />} />
				<Route path="/estimate" element={<Estimate />} />
			</Routes>
		</Router>
	);
}

export default App;
