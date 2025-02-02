import NavBar from "../components/NavBar";
import "../index.css";

function HomePage() {
	return (
		<>
			<NavBar />
			<div className="bg-gray-100 min-h-screen flex flex-col items-center py-12">
				<section className="w-full bg-blue-500 text-white py-16 px-8 text-center">
					<div className="container mx-auto">
						<h1 className="text-4xl font-bold mb-4">Welcome to Climb GUI!</h1>
						<p className="text-lg mb-8">
							Analyze climbing routes and find the most efficient paths for your
							bouldering sessions. Upload your image and let us do the rest!
						</p>
						<a
							href="/estimate"
							className="bg-white text-blue-500 px-6 py-3 rounded-lg font-semibold shadow hover:bg-blue-100 transition"
						>
							Get Started
						</a>
					</div>
				</section>

				<section className="container mx-auto py-16 px-8 text-center">
					<h2 className="text-3xl font-bold text-gray-800 mb-8">
						What Can You Do?
					</h2>
					<div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
						<div className="bg-white shadow-lg rounded-lg p-6">
							<h3 className="text-xl font-semibold mb-4">Upload Your Image</h3>
							<p className="text-gray-600">
								Upload an image of your climbing wall, and our system will
								identify and process the best routes for you.
							</p>
						</div>
						<div className="bg-white shadow-lg rounded-lg p-6">
							<h3 className="text-xl font-semibold mb-4">Customize Paths</h3>
							<p className="text-gray-600">
								Choose specific colors to analyze and focus on certain holds for
								a more tailored experience.
							</p>
						</div>
						<div className="bg-white shadow-lg rounded-lg p-6">
							<h3 className="text-xl font-semibold mb-4">Visualize Results</h3>
							<p className="text-gray-600">
								Get a clear visualization of the best climbing routes directly
								overlaid on your uploaded image.
							</p>
						</div>
					</div>
				</section>

				<section className="w-full bg-blue-500 text-white py-12 text-center">
					<div className="container mx-auto">
						<h2 className="text-3xl font-bold mb-4">Ready to Improve?</h2>
						<p className="text-lg mb-6">
							Start analyzing your routes today and climb smarter.
						</p>
						<a
							href="/estimate"
							className="bg-white text-blue-500 px-6 py-3 rounded-lg font-semibold shadow hover:bg-blue-100 transition"
						>
							Try It Now
						</a>
					</div>
				</section>
			</div>
		</>
	);
}

export default HomePage;
